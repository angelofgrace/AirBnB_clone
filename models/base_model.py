#!/usr/bin/python3
"""PRACTICE FILE - psudo set up for base_model"""

from uuid import uuid4
from datetime import datetime

class BaseModel: 
    """practice psudo for BaseModel"""
    def __init__(self):
        self.id = uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        """__str__ method represents the class BaseModel"""
        string = "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
        return string

    def save(self):
        """ updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()

       
    def to_dict(self):
        """  return a dictionary conatining all keys/value """
        self.__dict__['__class__'] = self.__class__.__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__
    # def to_json():
