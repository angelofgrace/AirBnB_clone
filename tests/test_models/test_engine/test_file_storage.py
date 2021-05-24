#!/usr/bin/python3
"""unit tests"""


from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
import datetime
import os


class Test_file_storage(unittest.TestCase):

    """ Test FileStorage class with unit tests """

    def test__file_path(self):
        storage1 = FileStorage()
        if os.path.exists("file.json"):
            os.remove("file.json")
        storage1.save()
        self.assertTrue(os.path.exists("file.json"))

    def test__objects(self):
        storage2 = FileStorage()
        self.assertIsInstance(storage2._FileStorage__objects, dict)

    def test_all(self):
        storage3 = FileStorage()
        self.assertIsInstance(storage3.all(), dict)

    def test_new(self):
        storage4 = FileStorage()
        tmpDict = storage4.all().copy()
        model1 = BaseModel()
        self.assertNotEqual(storage4.all(), tmpDict)

    def test_all_new(self):
        model5 = BaseModel()
        storage2 = FileStorage()
        self.assertIn(
            "{}.{}".format(model5.__class__.__name__,
                           model5.id),
            storage2.all().keys())
        self.assertIn(model5, storage2.all().values())

    def test_save(self):
        model6 = BaseModel()
        storage3 = FileStorage()
        storage3.save()
        os.remove(storage3.all())
        storage3.reload()
        self.assertIn(
            "{}.{}".format(model6.__class__.__name__,
                           model6.id),
            storage3.all().keys())
