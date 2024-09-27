#!/usr/bin/python3
"""BaseModel class module doc"""

import uuid
from datetime import datetime

class BaseModel:
	"""BaseModel class"""
	def __init__(self):
		"""Initializes a new instance (public instance/constructor)"""
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()

	def __str__(self):
		"""Returns a string representation of the instance"""
		return "[{}] ({}) {}".format(
			self.__class__.__name__,)
	
	def save(self):
		"""Updates the public instance attributes updated_at to the current datetime"""
		self.updated_at = datetime.now()