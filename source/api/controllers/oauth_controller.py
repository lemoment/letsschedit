"""
Handles the verification of calendar sync requests from Google and Outlook.

@author: Elias Gabriel
@revision: v1.0
"""
from google.oauth2 import id_token
from google.auth.transport import requests
from os import getenv
from flask import abort


GOOGLE_SECRET = getenv("GOOGLE_CLIENT_ID")


def veriauth_google(token):
	""" Verifies the allegedly authenticated Google user by submitted token. If the
	authentication is truthful, the user's email address is returned. """
	# Verify the oauth token with Google
	dinfo = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_SECRET)

	# Ensure that the cerificate issuer is Google, to prevent forgery
  if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
		raise InvalidISSError("Invalid ISS")

  # ID token is valid. Get the user's Google Account ID from the decoded token
  return idinfo['email']


class InvalidISSError(Exception):
	""" Defines an error that is raised whenever an invalid certificate is encountered. """
	pass
