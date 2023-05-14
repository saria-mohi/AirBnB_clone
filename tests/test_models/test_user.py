#!/usr/bin/python3
"""Test cases for User class"""

import unittest
import time
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models import user
import inspect
User = user.User


class TestUser(unittest.TestCase):
    """tests for the Class User"""

    def setUp(self):
        """Set up test methods"""
        pass

    def tearDown(self):
        """Tear Down test methods"""
        pass

    def test_User_pep8(self):
        """pep8 test"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_User_pep8(self):
        """pep8 test"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_user_module_docstring(self):
        """Test for the user.py module docstring"""
        self.assertIsNot(User.__doc__, None,
                         "user.py without docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "user.py without docstring")

    def test_review_class_docstring(self):
        """Test for the User class docstring"""
        self.assertIsNot(User.__doc__, None,
                         "User class without docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class without docstring")

    def test_class_User(self):
        """test for the class"""
        obj_user = User()
        self.assertIsInstance(obj_user, User)

    def test_subclass_BaseModel(self):
        """Test the user class is subclass of BaseModel"""
        obj_user = User()
        self.assertIsInstance(obj_user, BaseModel)
        self.assertTrue(hasattr(obj_user, "id"))
        self.assertTrue(hasattr(obj_user, "created_at"))
        self.assertTrue(hasattr(obj_user, "updated_at"))

    def test_attributes_user(self):
        """Test user attributes"""
        attributes_user = {"email": str,
                           "password": str,
                           "first_name": str,
                           "last_name": str}
        obj_user = User()
        for key, value in attributes_user.items():
            self.assertTrue(hasattr(obj_user, key))
            self.assertEqual(type(getattr(obj_user, key, None)), value)

    def test_str(self):
        """Test str method"""
        obj_user = User()
        string = "[User] ({}) {}".format(
                 obj_user.id, obj_user.__dict__)
        self.assertEqual(string, str(obj_user))

    def test_to_dict_user_attributes(self):
        """Test to_dict method creates a dictionary with expected attributes"""
        obj_user = User()
        new_dict = obj_user.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attributes in obj_user.__dict__:
            self.assertTrue(attributes in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_to_dict_user_values(self):
        """Test dictionary values"""
        obj_user = User()
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        new_dict = obj_user.to_dict()
        self.assertEqual(new_dict["__class__"], "User")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         obj_user.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"],
                         obj_user.updated_at.strftime(t_format))

    def test_save(self):
        """Test save method"""
        obj_user = User()
        before = obj_user.updated_at
        obj_user.save()
        time.sleep(2)
        self.assertLess(before, obj_user.updated_at)
        with open("file.json", "r") as file:
            self.assertIn("User." + obj_user.id, file.read())

if __name__ == "__main__":
    unittest.main()
