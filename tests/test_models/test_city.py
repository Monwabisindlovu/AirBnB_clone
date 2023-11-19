#!/usr/bin/python3
""" Unittest for Test for city """

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ Unit test for city model """
    def test_attributes(self):
        """ Testing for city model """
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
