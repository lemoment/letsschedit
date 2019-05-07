# == Schema Information
#
# Table name: appointments
#
#  idx                                :integer          not null, primary key
#  calendar                           :integer
#  author                             :varchar
#  email                              :varchar(254)
#  block_start                        :integer
#  block_end                          :integer
#
from peewee import *
from . import BaseModel, Calendar


class Appointment(BaseModel):
	""" Defines the Appointment model for the database. Table schema is commented above. """
	idx = BigAutoField()
	
	# Defines a one-to-many table relation. A single Calendar holds references
	# to many appointments, but not the other way around. `backref` indicates that
	# the list of appointments can be accessed via that variable from a Calendar
	# instance 
	calendar = ForeignKeyField(Calendar, backref='appointments')	
	author = CharField()
	email = CharField(max_length=254) # as standardized by RFC 2821
	block_start = IntegerField()
	block_end = IntegerField()

	class Meta:
		table_name = "appointments"
