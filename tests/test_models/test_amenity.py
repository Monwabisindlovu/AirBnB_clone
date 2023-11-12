#!/usr/bin/python3
""" Unittest for Test for Amenity """

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ This is the unittest for amenity """

    def test_attributes(self):
        """ Testing for amenity """
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
