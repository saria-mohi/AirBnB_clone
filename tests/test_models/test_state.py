#!/usr/bin/python3
"""Test cases for State class"""

import unittest
import time
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models import state
import inspect
State = state.State


class TestState(unittest.TestCase):
    """tests for the Class State"""

    def setUp(self):
        """Set up test methods"""
        pass

    def tearDown(self):
        """Tear Down test methods"""
        pass

    def test_State_pep8(self):
        """pep8 test"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/state.py'])
        self.assertEqual(result.total_errors, 0)

    def test_State_pep8(self):
        """pep8 test"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0)

    def test_state_module_docstring(self):
        """Test for the state.py module docstring"""
        self.assertIsNot(State.__doc__, None,
                         "state.py without docstring")
        self.assertTrue(len(State.__doc__) >= 1,
                        "state.py without docstring")

    def test_state_class_docstring(self):
        """Test for the State class docstring"""
        self.assertIsNot(State.__doc__, None,
                         "State class without docstring")
        self.assertTrue(len(State.__doc__) >= 1,
                        "State class without docstring")

    def test_class_State(self):
        """test for the class"""
        obj_state = State()
        self.assertIsInstance(obj_state, State)

    def test_subclass_BaseModel(self):
        """Test the state class is subclass of BaseModel"""
        obj_state = State()
        self.assertIsInstance(obj_state, BaseModel)
        self.assertTrue(hasattr(obj_state, "id"))
        self.assertTrue(hasattr(obj_state, "created_at"))
        self.assertTrue(hasattr(obj_state, "updated_at"))

    def test_attributes_state(self):
        """Test state attributes"""
        attributes_state = {"name": str}
        obj_state = State()
        for key, value in attributes_state.items():
            self.assertTrue(hasattr(obj_state, key))
            self.assertEqual(type(getattr(obj_state, key, None)), value)

    def test_str(self):
        """Test str method"""
        obj_state = State()
        string = "[State] ({}) {}".format(
                 obj_state.id, obj_state.__dict__)
        self.assertEqual(string, str(obj_state))

    def test_to_dict_state_attributes(self):
        """Test to_dict method creates a dictionary with expected attributes"""
        obj_state = State()
        new_dict = obj_state.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attributes in obj_state.__dict__:
            self.assertTrue(attributes in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_to_dict_state_values(self):
        """Test dictionary values"""
        obj_state = State()
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        new_dict = obj_state.to_dict()
        self.assertEqual(new_dict["__class__"], "State")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         obj_state.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"],
                         obj_state.updated_at.strftime(t_format))

    def test_save(self):
        """Test save method"""
        obj_state = State()
        before = obj_state.updated_at
        time.sleep(2)
        obj_state.save()
        self.assertLess(before, obj_state.updated_at)
        with open("file.json", "r") as file:
            self.assertIn("State." + obj_state.id, file.read())

if __name__ == "__main__":
    unittest.main()
