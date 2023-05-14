#!/usr/bin/python3
"""Test cases for Place class"""

import unittest
import time
import pep8
import os
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import place
import inspect
Place = place.Place


class TestPlace(unittest.TestCase):
    """tests for the Class Place"""

    def setUp(self):
        """Set up test methods"""
        pass

    def tearDown(self):
        """Tear Down test methods"""
        pass

    def test_Place_pep8(self):
        """pep8 test"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/place.py'])
        self.assertEqual(result.total_errors, 0)

    def test_Place_pep8(self):
        """pep8 test"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0)

    def test_place_module_docstring(self):
        """Test for the place.py module docstring"""
        self.assertIsNot(place.__doc__, None,
                         "place.py without docstring")
        self.assertTrue(len(place.__doc__) >= 1,
                        "place.py without docstring")

    def test_place_class_docstring(self):
        """Test for the Place class docstring"""
        self.assertIsNot(Place.__doc__, None, "Place class without docstring")
        self.assertTrue(len(Place.__doc__) >= 1,
                        "Place class without docstring")

    def test_class_Place(self):
        """test for the class"""
        obj_place = Place()
        self.assertIsInstance(obj_place, Place)

    def test_subclass_BaseModel(self):
        """Test the place class is subclass of BaseModel"""
        obj_place = Place()
        self.assertIsInstance(obj_place, BaseModel)
        self.assertTrue(hasattr(obj_place, "id"))
        self.assertTrue(hasattr(obj_place, "created_at"))
        self.assertTrue(hasattr(obj_place, "updated_at"))

    def test_attributes_place(self):
        """Test place attributes"""
        attributes_place = {"city_id": str,
                            "user_id": str,
                            "name": str,
                            "description": str,
                            "number_rooms": int,
                            "number_bathrooms": int,
                            "max_guest": int,
                            "price_by_night": int,
                            "latitude": float,
                            "longitude": float,
                            "amenity_ids": list}
        obj_place = Place()
        for key, value in attributes_place.items():
            self.assertTrue(hasattr(obj_place, key))
            self.assertEqual(type(getattr(obj_place, key, None)), value)

    def test_str(self):
        """Test str method"""
        obj_place = Place()
        string = "[Place] ({}) {}".format(
                 obj_place.id, obj_place.__dict__)
        self.assertEqual(string, str(obj_place))

    def test_to_dict_place_attributes(self):
        """Test to_dict method creates a dictionary with expected attributes"""
        obj_place = Place()
        new_dict = obj_place.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attributes in obj_place.__dict__:
            self.assertTrue(attributes in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_to_dict_place_values(self):
        """Test dictionary values"""
        obj_place = Place()
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        new_dict = obj_place.to_dict()
        self.assertEqual(new_dict["__class__"], "Place")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         obj_place.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"],
                         obj_place.updated_at.strftime(t_format))

    def test_save(self):
        """Test save method"""
        obj_place = Place()
        before = obj_place.updated_at
        time.sleep(2)
        obj_place.save()
        self.assertLess(before, obj_place.updated_at)
        with open("file.json", "r") as file:
            self.assertIn("Place." + obj_place.id, file.read())

if __name__ == "__main__":
    unittest.main()
