"""
Hosts the main application, routing endpoints to their desired controller.

@author: Elias Gabriel
@revision: v1.4
"""
from os import getenv as env
from flask import Flask, render_template, request
from werkzeug.exceptions import HTTPException
from models import BaseModel
from controllers import *
from responses import ISOAwareEncoder


##
## CONFIGURATION
##
## Defines and configures the web server,
## database connection, and data models.
##

app = Flask("letsschedit")
app.json_encoder = ISOAwareEncoder
db = BaseModel.get_database()
db.init(
    env('DATABASE'),
    user=env('DB_USERNAME'),
    password=env('DB_PASSWORD')
)

@app.before_request
def _db_connect():
    """ Ensures that whenever a HTTP request is comming in, a db connection is dispatched
    from the pool. This is required as MySQL oftens kills idle connections, so we want
    a hot new fresh one every time. """
    db.connect()

@app.teardown_request
def _db_close(exc):
    """ Ensures that whenever a request is finished being processed, the open connection is
    closed and returned to the pool for reuse. """ 
    if not db.is_closed(): db.close()

@app.errorhandler(HTTPException)
def _request_failed(e):
    """ Displays an error page if something goes wrong somewhere, either on purpose or
    accidentally. Error message and codes are automatically passed to the status page. """
    return render_template("status.html", name=e.name, message=e.description, code=e.code), e.code

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'

    if request.method == 'OPTIONS':
	response.headers['Access-Control-Allow-Methods'] = "GET, POST, PUT, DELETE"
	headers = request.headers.get('Access-Control-Request-Headers')
	if headers: response.headers['Access-Control-Allow-Headers'] = headers

    return response


##
## ROUTING
##
## Define the application URLs and connect
## each URL to a specific controller, so that
## the API responds with specific actions.
##

app.add_url_rule('/cal/<string:UUID>', 'get-cal', CalendarController.get, methods=["GET"])
app.add_url_rule('/cal/<string:UUID>/sync', 'sync-cal', CalendarController.sync, methods=["POST"])
app.add_url_rule('/create/cal', 'create-cal', CalendarController.new, methods=["PUT"])


## REQUIRED FOR CLI RUN ##
if __name__ == '__main__': app.run()
