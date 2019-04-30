"""
Defines the controlling methods for the various calendar endpoints.

@author: Elias Gabriel
@revision: v1.0
"""
from flask_restful import Resource, reqparse
from iso8601 import parse_date
from ..models import Calendar
from playhouse.shortcuts import model_to_dict
from ..core import errors

class CalendarController(Resource):
	"""
	Handles GET, POST, and PUT requests made to the registered URLs.
	"""
	# Defines the namespace to be used later when generating Calendar UUIDs
	DOMAINSPACE = "letsschedit.com"


	def __init__(self, db):
		# Reference the connected database
		self.database = db
		self.arguments = []

		# Create an argument parser to be used in the PUT handler
		# - All arguments are required
		# - All arguments must be passed via the JSON body
		# - All arguments are trimmed
		# - Errors are bundled together
		self.arguments.append(reqparse.RequestParser(bundle_errors=True, trim=True))
		self.arguments[0].add_argument('event_name', type=str, required=True, location='json')
		self.arguments[0].add_argument('start_date', type=str, required=True, location='json')
		self.arguments[0].add_argument('end_date', type=str, required=True, location='json')


	def get(self, UUID):
		""" Pulls the given Calendar from the database using its designated UUID. If
		no Calendar is found, the client is redirected to a 404 page indicating that
		an invalid request was made.
		"""
		try:
			# Retrieve calendar from the database
			cal = model_to_dict(Calendar.get(Calendar.uuid == UUID))
			return errors.success(errors.CAL_GET_SUCCESS, calendar=cal)
		# Return a "you-bad" JSON if a calendar isn't found
		except: return errors.failure(errors.CAL_GET_FAILURE)

	def post(self, UUID):
		""" Resyncs the given Calendar with the given list of appointments. """
		pass


	def put(self):
		""" Accepts an expected JSON body containing the parameters required to define
		a new Calendar. If all verifications pass, a new Calendar is created and its
		UUID is sent back to the client.
		"""
		# Parse the incoming request arguments, and be strict about it
		args = self.arguments[-1].parse_args(strict=True)

		try:
			# Collect all the required calendar fields
			cal_uuid = uuid5(uuid.NAMESPACE_DNS, DOMAINSPACE)
			event_name = args['name']
			start_date = parse_date(args['start_date'])
			end_date = parse_date(args['end_date'])
			
			# Ensure that this operation happens atomically, as in nothing else is
			# happening when we create a new entry
			with self.database.atomic():
				# Create a new Calendar entry with the passed properties
				cal = Calendar.create(
					uuid=cal_uuid,
					name=event_name,
					start=start_date,
					end=end_date
				)

			# Return a jsonified version of the new calendar
			return errors.success(errors.CAL_CREATE_SUCCESS, calendar=model_to_dict(cal))
		# Return a "tisk-tisk" JSON error
		except: return errors.failure(errors.CAL_CREATE_FAILURE)
