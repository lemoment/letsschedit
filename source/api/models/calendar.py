# == Schema Information
#
# Table name: calendars
#
#  idx                                :integer          not null, primary key
#  uuid                               :varchar(40)      unique
#  created                            :datetime
#  start_date                         :datetime
#  end_date                           :datetime
#  del_date                           :datetime
#  interval                           :integer          default(7)
#  days                               :varchar(7)       default('su,m,t,w,th,f,sa')
#
from peewee import *
from .base import BaseModel
from datetime import datetime


class Calendar(BaseModel):
    """ Defines the Calendar model for the database. Table schema is commented above. """
    idx = BigAutoField()
    uuid = UUIDField(unique=True)
    created_at = DateTimeField(default=datetime.utcnow)
    start_date = DateTimeField()
    end_date = DateTimeField()
    interval = IntegerField(default=15)
    days = CharField(max_length=16, default="su,m,t,w,th,f,sa")

    class Meta:
	table_name = "calendars"
