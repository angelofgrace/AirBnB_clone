#!/usr/bin/python3
"""Module creates State class"""

from models.base_model import BaseModel
from datetime import datetime


class Place(BaseModel):

    """Place s a child class of BaseModel with its own class attributes"""

    city_id = ""  # will be City.id
    user_id = ""  # will be User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = [""]  # will be the amenity.id

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
