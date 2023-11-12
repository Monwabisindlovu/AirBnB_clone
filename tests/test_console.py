#!/usr/bin/python3
"""Unittests for console.py"""

import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """ Test for all console file
    This test case checks whether the 'quit' feature in the console
        produces the expected output. It uses the unittest.mock.patch
        to temporarily replace sys.stdout for capturing the console output.
    """

    def test_quit(self):
        """ testing for quit feature """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual('', f.getvalue().strip())

    def test_help(self):
        """ Testing for help feature """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIn('Documented commands', f.getvalue())

    def test_create(self):
        """ Testing for create feature """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            instance_id = f.getvalue().strip()
            self.assertTrue(instance_id.isalnum())

    def test_show(self):
        """ Testing for show feature """
        instance_id = "some_valid_instance_id"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {instance_id}")
            self.assertIn(instance_id, f.getvalue().strip())

    def test_destroy(self):
        """ Testing for destroy feature """
        instance_id = "some_valid_instance_id"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User {instance_id}")
            self.assertIn('destroyed', f.getvalue().strip())

    def test_update(self):
        """ Testing for update feature """
        instance_id = "some_valid_instance_id"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {instance_id} attribute value")
            self.assertIn('updated', f.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
