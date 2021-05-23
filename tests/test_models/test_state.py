#!/usr/bin/python3
"""unit tests"""


from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage
import unittest
import datetime


class Test_state(unittest.TestCase):
    """ Test the existence of State class """

    def test_state(self):
        state1 = State()
        self.assertIsNotNone(state1.name)
