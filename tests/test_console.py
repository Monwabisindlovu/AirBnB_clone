#!/usr/bin/python3
"""Unittests for console.py"""

import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """ Test for all console file """
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
        """ testingt for creatye feature """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            # Add assertions based on your create command behavior
            self.assertIn('created', f.getvalue())

    def test_show(self):
        """ Assuming you have an existing instance ID """
        instance_id = "some_valid_instance_id"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {instance_id}")
            # Add assertions based on your show command behavior
            self.assertIn(instance_id, f.getvalue())

    def test_destroy(self):
        """ Assuming you have an existing instance ID """
        instance_id = "some_valid_instance_id"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User {instance_id}")
            # Add assertions based on your destroy command behavior
            self.assertIn('destroyed', f.getvalue())

    def test_update(self):
        """ Assuming you have an existing instance ID """
        instance_id = "some_valid_instance_id"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {instance_id} attribute value")
            # Add assertions based on your update command behavior
            self.assertIn('updated', f.getvalue())


if __name__ == '__main__':
    unittest.main()
