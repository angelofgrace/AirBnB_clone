#!/usr/bin/python3
"""unit tests"""


from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
import unittest
import datetime


class Test_city(unittest.TestCase):
    """ Test the existence of City class """

    def test_city(self):
        city1 = City()
        self.assertIsInstance(city1, City)
