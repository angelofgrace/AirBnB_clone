#!/usr/bin/python3
"""unit tests"""


from models.base_model import BaseModel
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import unittest
import datetime


class Test_amenity(unittest.TestCase):
    """ Test the existence of Amenity class """

    def test_amenity(self):
        amenity1 = Amenity()
        self.assertIsInstance(amenity1, Amenity)
