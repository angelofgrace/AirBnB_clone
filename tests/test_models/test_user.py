#!/usr/bin/python3
"""unit tests"""


from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
import unittest
import datetime


class Test_user(unittest.TestCase):
    """ Test user attribute presence """

    def test_user_email(self):
        """ Prove existence of user email attribute """
        user1 = User()
        self.assertIsNotNone(user1.email)

    def test_user_password(self):
        """ Prove existence of user email attribute """
        user2 = User()
        self.assertIsNotNone(user2.password)

    def test_user_first_name(self):
        """ Prove existence of user first name attribute """
        user3 = User()
        self.assertIsNotNone(user3.first_name)

    def test_user_last_name(self):
        """ Prove existence of user last name attribute """
        user4 = User()
        self.assertIsNotNone(user4.last_name)
