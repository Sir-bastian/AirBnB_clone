#!/usr/bin/python3

"""
Console Testing: Verify Console Functionality
"""

import unittest
import console
from console import HBNBCommand


class test_console(unittest.TestCase):
    """
    Test Class: Console Functionality
    """

    def create(self):
        """
        Create an Instance of the User Class
        """
        return HBNBCommand()

    def test_quit(self):
        """ 
        Test the 'quit' Method
        """
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        """
        Test the 'EQF' Method (Explanation Function)
        """
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))

