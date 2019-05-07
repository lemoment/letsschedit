"""
Defines the controlling methods for the various calendar endpoints.

@author: Elias Gabriel
@revision: v1.5
"""
from flask_restful import reqparse
from models import *
from responses import Responses, enlang
import uuid
from datetime import datetime, timedelta
import controllers.oauth_controller as oauth
from peewee import DoesNotExist
from playhouse.shortcuts import model_to_dict
from math import floor, ceil


class CalendarController():
	"""
	Handles GET, POST, and PUT requests made to the registered URLs. GET requests provided with an
	adequate UUID return serialized Calendar objects. POST requests provided with a UUID and a list
	of required event data will sync the Calendar instance. PUT requests create new Calendars when
	given the required data.
	"""


	def new():
		""" Accepts an expected JSON body containing the parameters required to define
		a new Calendar. If all verifications pass, a new Calendar is created and its
		UUID is sent back to the client.
		"""
		# TODO: Port to custom package
		# Create an argument parser
		# - All arguments are required
		# - All arguments must be passed via the JSON body
		# - All arguments are trimmed
		# - Errors are bundled together
		argreq = reqparse.RequestParser(bundle_errors=True, trim=True)
		argreq.add_argument('event_name', type=str, required=True, location='json')
		argreq.add_argument('start_date', type=str, required=True, location='json')
		argreq.add_argument('end_date', type=str, required=True, location='json')
		# Parse the incoming request arguments, and be strict about it
		args = argreq.parse_args(strict=True)

		try:
			# Collect all the required calendar fields
			cal_uuid = str(uuid.uuid4())
			name = args['event_name']
			start = datetime.fromisoformat(args['start_date'])
			end = datetime.fromisoformat(args['end_date'])
			interval = 1

			# Round the start and end times to the closest interval
			start = CalendarController._intervalize(interval, start)
			end = CalendarController._intervalize(interval, end)
	
			# Ensure that this operation happens atomically, as in nothing else is
			# happening when we create a new entry
			with BaseModel.get_database().atomic():
				# Create a new Calendar entry with the passed properties
				cal = Calendar.create(
					uuid=cal_uuid,
					name=name,
					interval=interval,
					start_date=start,
					end_date=end
				)
				
			# Return a jsonified version of the new calendar
			return Responses.success(enlang.CAL_CREATE_SUCCESS, calendar=CalendarController._serialize(cal))
		except Exception as e:
			# Return a "tisk-tisk" JSON error
			return Responses.failure(enlang.CAL_CREATE_FAILURE)

	
	def get(UUID):
		""" Pulls the given Calendar from the database using its designated UUID. If
		no Calendar is found, the client is redirected to a 404 page indicating that
		an invalid request was made.
		"""
		try:
			# Retrieve calendar from the database
			cal = Calendar.get(Calendar.uuid == UUID)

			return Responses.success(enlang.CAL_GET_SUCCESS, calendar=CalendarController._serialize(cal))
		# Return a "you-bad" JSON if a calendar isn't found
		except: return Responses.failure(enlang.CAL_GET_FAILURE)


	def sync(UUID):
		""" Syncs the given Calendar with the given list of appointments. """
		# Create an argument parser
		# - All arguments are required
		# - All arguments must be passed via the JSON body
		# - All arguments are trimmed
		# - Errors are bundled together
		argreq = reqparse.RequestParser(bundle_errors=True, trim=True)
		argreq.add_argument('provider', type=str, required=True, location='json', choices=("Google", "Outlook"))
		argreq.add_argument('token', type=str, required=True, location='json')
		argreq.add_argument('events', type=dict, required=True, location='json', action='append')
		# Parse the incoming request arguments, and be strict about it
		args = argreq.parse_args(strict=True)

		try:
			cal = Calendar.get(Calendar.uuid == UUID)
			token = args['token']
			provider =  args['provider']
			events = args['events']
			flag = True
			email = "eliasfgabriel@gmail.com"
			author = "Elias Gabriel"
	
			# Verify the token with the right provider
			if not flag and provider == "Google":
				email = oauth.veriauth_google(token)

			if flag:
				then = datetime.now()
				# Sync the calendar appointments with voodoo majyc
				CalendarController._handle_sync(cal, email, author, events)
				# If it actually worked, send the success JSON
				return Responses.success(enlang.CAL_SYNC_SUCCESS, calendar=CalendarController._serialize(cal))
			else:
				# If a request is sent with an invalid provider, throw an error
				return Responses.failure(enlang.SYNC_INVALID_PROVIDER)
		except DoesNotExist:
			# The given calendar does not exist, return the appropriate error
			return Responses.failure(enlang.CAL_GET_FAILURE)
		except Exception as e:
			# If something is wrong with the request, send an error
			return Responses.failure(enlang.CAL_SYNC_FAILURE)


	@classmethod
	def _intervalize(cls, interval, dt):
		""" Rounds the given datetime to the given minute interval. Second and microseconds
		are chopped off, and minutes are rounded to the nearest possible chunk. """
		return dt - timedelta(minutes=dt.minute % interval, seconds=dt.second, microseconds=dt.microsecond)


	@classmethod
	def _serialize(cls, model):
		""" Converts a Calendar instance into a JSON-able dictionary, omitting DB-specific
		fields and correctly parsing stored appointments. """
		# Get this calendar's info and list of appointments
		sd = model.start_date
		interval = model.interval
		iappts = model.appointments
		appts = []

		# For each appointment
		for appt in iappts:
			# Get the author's name and email
			author = appt.author
			email = appt.email
			# Convert the start and end blocks to times
			s_offset = (appt.block_start - 1) * interval
			e_offset = appt.block_end * interval
			# Adjust the start time by the offset minutes to find the region end and starts
			start_time = sd + timedelta(hours=0, minutes=s_offset, seconds=0, microseconds=0)
			end_time = sd + timedelta(hours=0, minutes=e_offset, seconds=0, microseconds=0)
	
			# Add the appointment, as a dict, to the array to be serialized
			appts.append({ "name": author, "email": email, "start_time": start_time, "end_time": end_time })

		# Convert the calendar to what we want
		cal = model_to_dict(model, exclude=[ Calendar.idx, Calendar.appointments, Calendar.created_at ])
		cal['appointments'] = appts
	
		return cal


	@classmethod
	def _handle_sync(cls, cal, email, author, events):
		""" Called when a sync request is verified and authenticated. All previous appointments associated
		with the user are removed and replaced by the new ones. """
		# Get calendar definitions
		sd = cal.start_date
		ed = cal.end_date
		interval = cal.interval

		# We only care about the unique blocks we add to the taken times, so we define
		# a set. Sets are like lists but only add elements if they are unique in the set.
		# Even if we added duplicate elements, the set would only store one of them.
		busy_blocks = set()

		for event in events:
			# Parse the event start and end times, stripping timezone data
			event_start = datetime.fromisoformat(event['start'].rstrip('Z'))
			event_end = datetime.fromisoformat(event['end'].rstrip('Z'))

			# Find the event's start block, flooring the result to assume if some part
			# of a given block is taken, the entire block is taken. We add one because
			# our block range is exclusive-inclusive (we start at 1 not 0)
			block_start = floor((event_start - sd).total_seconds() / 60 / interval) + 1

			# Find the event's end block, ceiling the result for the same reason as above. We
			# do not need to add 1 because the end block is within the range by default
			block_end = ceil((event_end - sd).total_seconds() / 60 / interval)
			# Add the unique busy blocks to the list
			busy_blocks.update(range(block_start, block_end + 1))

		# Find the total number of blocks in the given calendar range
		total_blocks = ceil((ed - sd).total_seconds() / 60 / interval)
		blockset = set(range(1, total_blocks + 1))

		# Set theory! Only keep the blocks that are not contained within the busy set. Subtracting
		# the sets to give us unique elements yields all the free times! Sort the remaining set
		# to ensure that we count in the correct order, and append -1 for the appointment
		# partitioning algorithm.
		free_blocks = sorted(blockset - busy_blocks)
		free_appointments = []
		# Set the current block start to the first in the list
		cbs = free_blocks[0]

		for i in range(len(free_blocks)):
			current_block = free_blocks[i]
			next_block = current_block
			
			# If we are not at the end of the line, set the next block
			if i + 1 < len(free_blocks): next_block = free_blocks[i + 1]

			# Check to see if the current and next blocks are sequential. If they aren't
			# we know that we've reached a gap and need to create an appointment.
			if next_block - current_block != 1:
				# Don't create an appointment outright, add the data to a list and then create them
				# in bulk once we are done parsing. This reduces the time complexity from O(n), where
				# n is the number of events in a given day, to O(1). This is because we will
				# execute 1 SQL query rather than `n` SQL queries.
				free_appointments.append({
					"calendar": cal,
					"author": author,
					"email": email,
					"block_start": cbs,
					"block_end": current_block
				})
			
				# Update the current start block
				cbs = next_block
				# Increment the loop to start at the next block to be checked, excluding the start
				# block because we already know it is in the new range
				i += 1

		# Wrap it all in a transaction because we want the data switch to be as quick as possible
		with BaseModel.get_database().atomic():
			# Ahh! Delete all the existing calendar events and create all the new ones
			Appointment.delete().where(Appointment.email == email).execute()
			Appointment.insert_many(free_appointments).execute()
