#!/usr/bin/python3
""" Test for state """

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def test_attributes(self):
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertEqual(state.name, "")

if __name__ == '__main__':
    unittest.main()
