#!/usr/bin/python3
"""unit tests"""


from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
import datetime

class Test_base_model(unittest.TestCase):
    """Test BaseModel class with unit tests"""

    def test_id(self):
        model1 = BaseModel()
        self.assertNotEqual(model1.id, "")

    def test_created_at(self):
        model1 = BaseModel()
        self.assertNotEqual(model1.created_at, "")

    def test_str(self):
        model2 = BaseModel()
        self.assertIn(model2.id, model2.__str__())
        self.assertIn(str(model2.__dict__), model2.__str__())
        self.assertIn(model2.__class__.__name__, model2.__str__())

    def test_to_dict(self):
        model3 = BaseModel()
        self.assertIn("__class__", model3.to_dict())
        
    def test_save(self):
        model4 = BaseModel()
        time1 = model4.updated_at
        model4.save()
        time2 = model4.updated_at
        self.assertNotEqual(time1, time2)

class Test_file_storage(unittest.TestCase):
    """ Test FileStorage class with unit tests """

    def test__file_path(self):
        storage1 = FileStorage()
        storage1.save()
        self.assertNotEqual("file.json", "")

    def test__objects(self):
        model5 = BaseModel()
        storage2 = FileStorage()
        self.assertIn("{}.{}".format(model5.__class__.__name__, model5.id), storage2.all().keys())
        self.assertIn(model5, storage2.all().values())   
