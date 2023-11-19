#!/usr/bin/python3
""" Unittest for Test for user """

import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """ Test for testuser """

    def test_user_initialization(self):
        """ Test for user initialization """
        user = User()
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_attribute_assignment(self):
        """ Test for user attribute assignemnt """
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_user_to_dict(self):
        """ Test for user to dict """
        user = User()
        user.id = "test-id"
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"
        user.created_at = datetime.utcnow()
        user.updated_at = datetime.utcnow()

        user_dict = user.to_dict()

        self.assertEqual(user_dict['id'], "test-id")
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['password'], "password123")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)


if __name__ == '__main__':
    unittest.main()
