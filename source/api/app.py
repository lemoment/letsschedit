"""
Hosts the main application, routing endpoints to their desired controller.

@author: Elias Gabriel
@revision: v1.0
"""
from os import getenv as env
from flask import Flask, jsonify
from flask_restful import Api
from models import BaseModel
from controllers import *


##
## CONFIGURATION
##
## Defines and configures the web server,
## database connection, and data models.
##

api = Api(Flask("letsschedit"))
db = BaseModel.get_database()
db.init(
	env('DATABASE'),
	user=env('DB_USERNAME'),
	password=env('DB_PASSWORD')
)

@api.app.before_request
def _db_connect():
	""" Ensures that whenever a HTTP request is comming in, a db connection is dispatched
	from the pool. This is required as MySQL oftens kills idle connections, so we want
	a hot new fresh one every time. """
	db.connect()

@api.app.teardown_request
def _db_close(exc):
	""" Ensures that whenever a request is finished being processed, the open connection is
	closed and returned to the pool for reuse. """ 
	if not db.is_closed(): db.close()


##
## ROUTING
##
## Define the application URLs and connect
## each URL to a specific controller, so that
## the API responds with specific actions.
##

api.add_resource(CalendarController, '/cal/<string:UUID>', '/cal/<string:UUID>/sync', '/cal/new', resource_class_args=(db,))


## REQUIRED FOR CLI RUN ##
if __name__ == '__main__': api.app.run()
