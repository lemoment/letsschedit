from flask import jsonify
from flask.json import JSONEncoder
from datetime import datetime


__all__ = [ "Responses", "ISOAwareEncoder"]


class Responses():
	"""
	Contains methods to simplify responding to client requests, specifically failure and
	success JSONs.
	"""
	
	def success(msg, **kwargs):
		""" Generates a dictionary response with the given message indicating an API success. """
		return jsonify({ "status": "success", "message": msg, **kwargs }), 200

	def failure(msg, **kwargs):
		""" Generates a dictionary response with the given message indicating an API failure. """
		return jsonify({ "status": "failure", "message": msg, **kwargs }), 400


class ISOAwareEncoder(JSONEncoder):
	"""
	Extends Flask's default JSON encoder to convert datetime objects to ISO strings
	rather than human-readable strings. While not strictly required when returning datetimes,
	it standardizes how datetimes are sent between the client and server.
	"""

	def default(self, obj):
		""" Determines how objects are serialized to JSON-representable objects. This overrides
		the method inherited from the `JSONEncoder` parent. """
		# If the object is a datime object, return it's ISO 8601 representation
		if isinstance(obj, datetime): return obj.isoformat() + 'Z'
		# If not, call the superclass encoder
		return JSONEncoder.default(self, obj)

