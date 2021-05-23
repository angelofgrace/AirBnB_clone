#!/usr/bin/python3
"""unit tests"""


from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
import datetime


class Test_file_storage(unittest.TestCase):
    """ Test FileStorage class with unit tests """

    def test__file_path(self):
        storage1 = FileStorage()
        storage1.save()
        self.assertNotEqual("file.json", "")

    def test__objects(self):
        """ works for all() and new() """
        model5 = BaseModel()
        storage2 = FileStorage()
        self.assertIn("{}.{}".format(model5.__class__.__name__, model5.id), storage2.all().keys())
        self.assertIn(model5, storage2.all().values())

    def test_save(self):
        model6 = BaseModel()
        storage3 = FileStorage()
        FileStorage.save(model6)
        storage3.all().clear()
        storage3.reload()
        self.assertIn("{}.{}".format(model6.__class__.__name__, model6.id), storage3.all().keys())
