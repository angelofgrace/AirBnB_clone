#!/usr/bin/python3
"""unit test"""


from models.base_model import BaseModel
import unittest
import datetime

class Test_base_model(unittest.TestCase):
    """Test_base_model class for unit tests"""

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
        self.assertIsInstance(model3.to_dict(), dict)
        
    def test_save(self):
        model4 = BaseModel()
        self.assertNotEqual(model4, model4.save())
       
