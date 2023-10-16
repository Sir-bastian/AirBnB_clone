#!/usr/bin/python3

""" 
Unittest for State class 
"""
import unittest
import pep8
from models.state import State

class State_testing(unittest.TestCase):
    """ Checks if user is instance of base_model """

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/state.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_doc(self):
        """test module documentation"""
        doc = __import__('models.state').__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """test class documentation"""
        doc = State.__doc__
        self.assertGreater(len(doc), 1)
