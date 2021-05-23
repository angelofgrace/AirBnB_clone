#!/usr/bin/python3
"""unit tests"""


from models.base_model import BaseModel
from models.place import Place
from models.engine.file_storage import FileStorage
import unittest
import datetime


class Test_place(unittest.TestCase):
    """ Test the existence of Place class """

    def test_place(self):
        place1 = Place()
        self.assertIsNotNone(place1.name)
