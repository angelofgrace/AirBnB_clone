#!/usr/bin/python3
"""unit tests"""


from models.base_model import BaseModel
from models.review import Review
from models.engine.file_storage import FileStorage
import unittest
import datetime


class Test_review(unittest.TestCase):
    """ Test the existence of Review class """

    def test_review(self):
        review1 = Review()
        self.assertIsInstance(review1, Review)
