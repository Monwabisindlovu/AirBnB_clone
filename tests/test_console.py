#!/usr/bin/python3
"""Tests for the HBNBCommand class"""

import unittest
from io import StringIO
import os
from unittest.mock import patch
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class"""

    """Define a string indicating that a class doesn't exist"""
    class_unfound = "** class doesn't exist **\n"

    def setUp(self):
        """Set up for basic tests"""
        self.cmd = HBNBCommand()
        self.file_path = "console.py"

    def tearDown(self):
        """Clean up after testing"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_quit(self):
        """Test the quit command"""
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("quit")
            self.assertEqual('', stdout.getvalue())

    def test_empty_line(self):
        """Test handling empty input"""
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("\n")
            self.assertEqual('', stdout.getvalue())

    def test_all(self):
        """Test the all command"""
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("all octopus")
            self.assertEqual(TestHBNBCommand.class_unfound,
                             stdout.getvalue())
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("all State")
            self.assertEqual("[]\n", stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
