"""
Hosts the main application, routing endpoints to their desired controller.

@author: Elias, Dieter, Riya, Maal
@revision: v1.0
"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

# more end points here!

if __name__ == '__main__': app.run()
