"""
A simple script to create the environment database and tables.

@author: Elias Gabriel
@revision: v1.0
"""
from dotenv import load_dotenv
from os import getenv
import pymysql
from models import BaseModel, Calendar, Appointment


if __name__ == "__main__":
	load_dotenv()
	database = getenv('DATABASE')
	host = getenv('DB_HOST')
	user = getenv('DB_USERNAME')
	pwd = getenv('DB_PASSWORD')
	
	# Connect to the database server and create a new database
	conn = pymysql.connect(host=host, user=user, password=pwd)
	conn.cursor().execute("CREATE DATABASE {}".format(database))
	conn.close()

	# Connect to the new database and create the tables
	db = BaseModel._meta.database
	db.init(database, host=host, user=user, password=pwd)
	db.create_tables([Calendar, Appointment])
	db.close()
