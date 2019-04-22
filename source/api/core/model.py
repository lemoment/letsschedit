"""
Defines a simple base model to be used by all db models. The Meta inner class is
configured on application run to hold a reference variable to the used database.

@author: Elias Gabriel
@revision: v1.0
"""
from peewee import Model

class BaseModel(Model):
	class Meta: pass
