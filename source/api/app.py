"""
Hosts the main application, routing endpoints to their desired controller.

@author: Elias Gabriel, Dieter Brehm, Riya Aggarwal, Maalvika Bhat
@revision: v1.0
"""
from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api
from controllers import *


##
## CONFIGURATION
##
## Load enviornment configuration variables
## and initialize the application instance.
##

load_dotenv()
api = Api(Flask(__name__))


##
## ROUTING
##
## Define the application URLs and connect
## each URL to a specific controller, so that
## the API responds with specific actions.
##

# home, the index page
api.add_resource(HomeController, '/')

 
if __name__ == '__main__': api.app.run()
