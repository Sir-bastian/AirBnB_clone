#!/usr/bin/python3

"""
Module for testing the City class
"""
import unittest
import json
import pep8
import datetime

from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Unit Testing: City Class Implementation
    """
    def test_doc_module(self):
        """Module documentation"""
        doc = City.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_city(self):
        """
        PEP8 Compliance Check for models/city.py
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_doc(self):
        """test module documentation"""
        doc = __import__('models.city').__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """test class documentation"""
        doc = City.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_test_city(self):
        """
        PEP8 Compliance Check for tests/test_models/test_city.py
        """
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """
        Constructor Documentation for MyClass
        """
        doc = City.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """
        Attribute Type Validation in Class
        """
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(City, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(City.name, str)
            self.assertIsInstance(City.state_id, str)


if __name__ == '__main__':
    unittest.main()
