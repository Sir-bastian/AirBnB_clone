#!/usr/bin/python3
"""Amenity Class Testing Module"""
import unittest
import json
import pep8
import datetime

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Validate State Class Functionality
    """
    def test_doc_module(self):
        """Module documentation"""
        doc = Amenity.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_amenity(self):
        """
        Check PEP 8 Compliance for models/amenity.py
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

<<<<<<< HEAD
     def test_module_doc(self):
        """test module documentation"""
        doc = __import__('models.amenity').__doc__
        self.assertGreater(len(doc), 1)
=======
    def test_pep8_conformance_test_amenity(self):
        """
        Verify PEP 8 Compliance in tests/test_models/test_state.py
        """
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = Amenity.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """
        Attribute Type Validation in Class
        """
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Amenity, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Amenity.name, str)

if __name__ == '__main__':
    unittest.main()
>>>>>>> 64999a53527c19229b2938550cca989d1ce86976

    def test_class_doc(self):
        """test class documentation"""
        doc = Amenity.__doc__
        self.assertGreater(len(doc), 1)
