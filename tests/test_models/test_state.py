#!/usr/bin/python3

import unittest
from models.user import storage
models import storage


class TestUser(unittest.TestCase):
    def test_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_save_and_reload(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"
        user.save()

        # Ensure the user is in the storage
        user_key = f"User.{user.id}"
        self.assertIn(user_key, storage.all())

        # Create a new storage instance to clear the existing objects
        new_storage = storage.FileStorage()
        new_storage.reload()

        # Ensure the reloaded user has the same attributes
        reloaded_user = new_storage.all()[user_key]
        self.assertEqual(reloaded_user.email, "test@example.com")
        self.assertEqual(reloaded_user.password, "password123")
        self.assertEqual(reloaded_user.first_name, "John")
        self.assertEqual(reloaded_user.last_name, "Doe")


if __name__ == '__main__':
    unittest.main()
