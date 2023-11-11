#!/usr/bin/python3
""" Test for all """

import unittest
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class TestState(unittest.TestCase):
    def test_attributes(self):
        """Test State class attributes"""
        state = State()
        self.assertEqual(state.name, "")

    def test_inheritance(self):
        """Test State inherits from BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)


class TestCity(unittest.TestCase):
    def test_attributes(self):
        """Test City class attributes"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_inheritance(self):
        """Test City inherits from BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)


class TestAmenity(unittest.TestCase):
    def test_attributes(self):
        """Test Amenity class attributes"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_inheritance(self):
        """Test Amenity inherits from BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)


class TestPlace(unittest.TestCase):
    def test_attributes(self):
        """Test Place class attributes"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_inheritance(self):
        """Test Place inherits from BaseModel"""
        place = Place()
        self.assertIsInstance(place, BaseModel)


class TestReview(unittest.TestCase):
    def test_attributes(self):
        """Test Review class attributes"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_inheritance(self):
        """Test Review inherits from BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)


if __name__ == "__main__":
    unittest.main()
