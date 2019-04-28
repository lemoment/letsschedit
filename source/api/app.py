"""
Hosts the main application, routing endpoints to their desired controller.

@author: Elias Gabriel
@revision: v1.0
"""
from flask import Flask
from core import RESTfulServer
from playhouse.pool import PooledMySQLDatabase
from controllers import *


##
## CONFIGURATION
##
## Defines and configures the web server,
## database connection, and data models.
##

app = Flask("letsschedit")
database = PooledMySQLDatabase()
BaseModel.Meta.database = database

@app.before_request
def db_connect():
	""" Ensures that whenever a HTTP request is comming in, a db connection is dispatched
	from the pool. This is required as MySQL oftens kills idle connections, so we want
	a hot new fresh one every time. """
	database.connect()

@app.teardown_request
def _db_close(exc):
	""" Ensures that whenever a request is finished being processed, the open connection is
	closed and returned to the pool for reuse. """ 
	if not database.is_closed(): database.close()


##
## ROUTING
##
## Define the application URLs and connect
## each URL to a specific controller, so that
## the API responds with specific actions.
##

# home, the index page
app.add_resource(HomeController, '/')


## REQUIRED FOR CLI RUN ##
if __name__ == '__main__': app.run()
