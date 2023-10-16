#!/usr/bin/python3

"""Module for testing the User class"""

import unittest
import json
import pep8
import datetime

from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Unit Testing: User Class Implementation
    """
    def test_doc_module(self):
        """Module documentation"""
        doc = User.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_base_model(self):
        """
        PEP8 Compliance Check for models/user.py
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

<<<<<<< HEAD
     def test_module_doc(self):
        """test module documentation"""
        doc = __import__('models.user').__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """test class documentation"""
        doc = User.__doc__
        self.assertGreater(len(doc), 1)
=======
    def test_pep8_conformance_test_base_model(self):
        """
        PEP8 Compliance Check for tests/test_models/test_user.py
        """
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """
        Constructor Documentation for User Class
        """
        doc = User.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """
        Attribute Type Validation in Class
        """
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(User, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(User.email, str)
            self.assertIsInstance(User.password, str)
            self.assertIsInstance(User.first_name, str)
            self.assertIsInstance(User.last_name, str)

if __name__ == '__main__':
    unittest.main()

>>>>>>> 64999a53527c19229b2938550cca989d1ce86976
