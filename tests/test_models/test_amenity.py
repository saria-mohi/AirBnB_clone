#!/usr/bin/python3
"""Test cases for Amenity class"""

import unittest
import time
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models import amenity
import inspect
Amenity = amenity.Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def setUp(self):
        """Set up test methods"""
        pass

    def tearDown(self):
        """Tear Down test methods"""
        pass

    def test_Amenity_pep8(self):
        """pep8 test"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/amenity.py'])
        self.assertEqual(result.total_errors, 0)

    def test_Amenity_pep8(self):
        """pep8 test"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0)

    def test_amenity_module_docstring(self):
        """Test for the amenity.py module docstring"""
        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py without docstring")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "amenity.py without docstring")

    def test_amenity_class_docstring(self):
        """Test for the Amenity class docstring"""
        self.assertIsNot(Amenity.__doc__, None, "amenity.py without docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "amenity.py without docstring")

    def test_class_Amenity(self):
        """class test"""
        obj_amenity = Amenity()
        self.assertIsInstance(obj_amenity, Amenity)

    def test_subclass_BaseModel(self):
        """Test the Amenity class is subclass of BaseModel"""
        obj_amenity = Amenity()
        self.assertIsInstance(obj_amenity, BaseModel)
        self.assertTrue(hasattr(obj_amenity, "id"))
        self.assertTrue(hasattr(obj_amenity, "created_at"))
        self.assertTrue(hasattr(obj_amenity, "updated_at"))

    def test_attributes_Amenity(self):
        """Test amenity attributes"""
        attributes_amenity = {"name": str}
        obj_amenity = Amenity()
        for key, value in attributes_amenity.items():
            self.assertTrue(hasattr(obj_amenity, key))
            self.assertEqual(type(getattr(obj_amenity, key, None)), value)

    def test_str(self):
        """Test str method"""
        obj_amenity = Amenity()
        string = "[Amenity] ({}) {}".format(
                 obj_amenity.id, obj_amenity.__dict__)
        self.assertEqual(string, str(obj_amenity))

    def test_to_dict_amenity_attributes(self):
        """Test to_dict method creates a dictionary with expected attributes"""
        obj_amenity = Amenity()
        new_dict = obj_amenity.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attributes in obj_amenity.__dict__:
            self.assertTrue(attributes in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_to_dict_amenity_values(self):
        """Test dictionary values"""
        obj_amenity = Amenity()
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        new_dict = obj_amenity.to_dict()
        self.assertEqual(new_dict["__class__"], "Amenity")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         obj_amenity.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"],
                         obj_amenity.updated_at.strftime(t_format))

    def test_save(self):
        """Test save method"""
        obj_amenity = Amenity()
        before = obj_amenity.updated_at
        time.sleep(2)
        obj_amenity.save()
        self.assertLess(before, obj_amenity.updated_at)
        with open("file.json", "r") as file:
            self.assertIn("Amenity." + obj_amenity.id, file.read())

if __name__ == "__main__":
    unittest.main()
