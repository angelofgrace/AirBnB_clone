#!/usr/bin/python3
"""Module creates User class"""

from datetime import datetime
from models.base_model import BaseModel


class User(BaseModel):

    """User is child class of BaseModel with additional class attributes"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        if not kwargs:
            super().__init__()
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
