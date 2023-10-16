#!/usr/bin/python3

""" 
Testing the User class. 
"""
import unittest
import pep8
from models.user import User

class User_testing(unittest.TestCase):

    """ Examining the BaseModel class."""

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/user.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

     def test_module_doc(self):
        """test module documentation"""
        doc = __import__('models.user').__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """test class documentation"""
        doc = User.__doc__
        self.assertGreater(len(doc), 1)
