"""
Provides a wrapper class for hosting a RESTful server.

@author: Elias Gabriel
@revision: v1.0
"""
from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api


class RESTfulServer(Api):
	"""
	A wrapper class for instantiating a RESTful Flask API.
	"""

	def __init__(self, name, **kwargs):
		# Load environment variables from the ENV file
		load_dotenv(**kwargs)
		self.app = Flask(name, **kwargs)
		super().__init__(self, self.app, **kwargs)
