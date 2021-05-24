#!/usr/bin/python3
"""Module creates State class"""

from models.base_model import BaseModel
from datetime import datetime


class State(BaseModel):

    """State is a child class of BaseModel with relevante class attributes"""

    name = ""

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
