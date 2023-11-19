#!/usr/bin/python3
""" This is my unnittest basemodel """

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Unit tests for the BaseModel class

     This test class contains unit tests for the methods and behavior
    of the BaseModel class (replace with your actual class name).

    Test Cases:
    1. test_initialization: Test the initialization of a BaseModel instance.
    2. test_to_dict: Test the to_dict method of the BaseModel class.
    3. test_from_dict: Test the from_dict method of the BaseModel class.
    4. test_str_representation: Test the string representation of the Base.
    """
    def test_str_method(self):
        """ Test the initialization of a BaseModel instance """
        my_model = BaseModel()
        expected_output = "[BaseModel] ({}) {}".format(my_model.id,
                                                       my_model.__dict__)
        self.assertEqual(str(my_model), expected_output)

    def test_save_method(self):
        """ Test unittest second """
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(my_model.updated_at, original_updated_at)

    def test_to_dict_method(self):
        """ Test uniitest third """
        my_model = BaseModel()
        model_dict = my_model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertTrue("created_at" in model_dict)
        self.assertTrue("updated_at" in model_dict)

    def test_to_dict_from_dict(self):
        """ Test unittest fourth """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)

        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.created_at.isoformat(),
                         my_new_model.created_at.isoformat())
        self.assertEqual(my_model.updated_at.isoformat(),
                         my_new_model.updated_at.isoformat())
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.my_number, my_new_model.my_number)
        self.assertEqual(my_model.__class__.__name__,
                         my_new_model.__class__.__name__)


if __name__ == '__main__':
    unittest.main()
