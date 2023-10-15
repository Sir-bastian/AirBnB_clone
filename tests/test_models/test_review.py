#!/usr/bin/python3

""" Unittest for Review class """

import unittest
import pep8
from models.review import Review

class Review_testing(unittest.TestCase):
    """ Checks if user is instance of base_model """

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/review.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

