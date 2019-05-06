from flask import jsonify

class Responses():
	"""
	Contains methods to simplify responding to client requests.
	"""
	
	def success(msg, **kwargs):
		""" Generates a dictionary response with the given message indicating an API success. """
		return jsonify({ "status": "success", "message": msg, **kwargs })

	def failure(msg, **kwargs):
		""" Generates a dictionary response with the given message indicating an API failure. """
		return jsonify({ "status": "failure", "message": msg, **kwargs })
