"""
Defines a simple base model to be used by all db models. A Meta inner class is
defined at runtime to hold a reference variable to the configured database.

@author: Elias Gabriel
@revision: v1.0
"""
from peewee import Model
from playhouse.pool import PooledMySQLDatabase


class BaseModel(Model):
    """
    A base Model class to be used as a subclass for all database models.
    """
    @classmethod
    def get_database(cls):
	return BaseModel._meta.database

    class Meta:
	database = PooledMySQLDatabase(None, autorollback=True)
