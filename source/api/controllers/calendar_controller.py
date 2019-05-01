"""
Defines the controlling methods for the various calendar endpoints.

@author: Elias Gabriel
@revision: v1.0
"""
from flask_restful import reqparse
from models import Calendar, BaseModel
from playhouse.shortcuts import model_to_dict
from requests import Responses, enlang
import uuid
from datetime import datetime



class CalendarController():
	"""
	Handles GET, POST, and PUT requests made to the registered URLs.
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
			
			# Ensure that this operation happens atomically, as in nothing else is
			# happening when we create a new entry
			with BaseModel.get_database().atomic():
				# Create a new Calendar entry with the passed properties
				cal = Calendar.create(
					uuid=cal_uuid,
					name=name,
					start_date=start,
					end_date=end
				)
				
			# Return a jsonified version of the new calendar
			return Responses.success(enlang.CAL_CREATE_SUCCESS, calendar=model_to_dict(cal))
		except Exception as e:
			print(e)
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

			return Responses.success(enlang.CAL_GET_SUCCESS, calendar=model_to_dict(cal))
		# Return a "you-bad" JSON if a calendar isn't found
		except: return Responses.failure(enlang.CAL_GET_FAILURE)


	def sync(UUID):
		""" Resyncs the given Calendar with the given list of appointments. """
		pass
