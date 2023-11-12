#!/usr/bin/python3
""" This is the unittest for review """

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ This is the unittest for Review """

    def test_attributes(self):
        """ Test for Review """
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
