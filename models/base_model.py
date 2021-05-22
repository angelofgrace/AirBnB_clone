#!/usr/bin/python3
"""PRACTICE FILE - psudo set up for base_model"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:

    """practice psudo for BaseModel"""

    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for k in kwargs.keys():
                # iterating through keys/value pairs k = keys
                if k == 'created_at' or k == 'updated_at':
                    kwargs[k] = datetime.strptime(
                        kwargs[k],
                        '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, k, kwargs[k])
                # everything except for class attr are set
                elif k != '__class__':
                    setattr(self, k, kwargs[k])

    def __str__(self):
        """__str__ method represents the class BaseModel"""
        string = "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__)
        return string

    def save(self):
        """ updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """  return a dictionary conatining all keys/value """
        self.__dict__['__class__'] = self.__class__.__name__
        attr_dict = self.__dict__.copy()
        attr_dict["created_at"] = attr_dict["created_at"].isoformat()
        attr_dict["updated_at"] = attr_dict["updated_at"].isoformat()
        return attr_dict

