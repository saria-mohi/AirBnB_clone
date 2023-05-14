#!/usr/bin/python3
"""Test cases for City class"""

import unittest
import time
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models import city
import inspect
City = city.City


class TestCity(unittest.TestCase):
    """tests for the Class City"""

    def setUp(self):
        """Set up test methods"""
        pass

    def tearDown(self):
        """Tear Down test methods"""
        pass

    def test_City_pep8(self):
        """pep8 test"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/city.py'])
        self.assertEqual(result.total_errors, 0)

    def test_City_pep8(self):
        """pep8 test"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0)

    def test_city_module_docstring(self):
        """Test for the city.py module docstring"""
        self.assertIsNot(city.__doc__, None,
                         "city.py without docstring")
        self.assertTrue(len(city.__doc__) >= 1,
                        "city.py without docstring")

    def test_city_class_docstring(self):
        """Test for the City class docstring"""
        self.assertIsNot(City.__doc__, None,
                         "City class without docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City class without docstring")

    def test_class_City(self):
        """test of the class"""
        obj_city = City()
        self.assertIsInstance(obj_city, City)

    def test_subclass_BaseModel(self):
        """Test the city class is subclass of BaseModel"""
        obj_city = City()
        self.assertIsInstance(obj_city, BaseModel)
        self.assertTrue(hasattr(obj_city, "id"))
        self.assertTrue(hasattr(obj_city, "created_at"))
        self.assertTrue(hasattr(obj_city, "updated_at"))

    def test_attributes_city(self):
        """Test city attributes"""
        attributes_city = {"state_id": str,
                           "name": str}
        obj_city = City()
        for key, value in attributes_city.items():
            self.assertTrue(hasattr(obj_city, key))
            self.assertEqual(type(getattr(obj_city, key, None)), value)

    def test_str(self):
        """Test str method"""
        obj_city = City()
        string = "[City] ({}) {}".format(
                 obj_city.id, obj_city.__dict__)
        self.assertEqual(string, str(obj_city))

    def test_to_dict_city_attributes(self):
        """Test to_dict method creates a dictionary with expected attributes"""
        obj_city = City()
        new_dict = obj_city.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attributes in obj_city.__dict__:
            self.assertTrue(attributes in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_to_dict_city_values(self):
        """Test dictionary values"""
        obj_city = City()
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        new_dict = obj_city.to_dict()
        self.assertEqual(new_dict["__class__"], "City")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         obj_city.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"],
                         obj_city.updated_at.strftime(t_format))

    def test_save(self):
        """Test save method"""
        obj_city = City()
        before = obj_city.updated_at
        time.sleep(2)
        obj_city.save()
        self.assertLess(before, obj_city.updated_at)
        with open("file.json", "r") as file:
            self.assertIn("City." + obj_city.id, file.read())

if __name__ == "__main__":
    unittest.main()
