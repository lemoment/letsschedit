"""
Provides functionality that allows controlling methods to expect data parameters.
This serves as a lightweight yet versatile alternative to Flask-RESTful's deprecated
`reqparse` module.

@author: Elias Gabriel
@revision: v1.0
"""
from flask import request


class params(object):
    def __init__(self, ):
      self.arg1 = arg1

    def __call__(self, f):
      def wrapped_f(*args):
				f(*args)
			return wrapped_f	
