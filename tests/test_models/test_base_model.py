#!/usr/bin/python3
""" module for the tests cases for the BaseModels class
"""
import unittest
import pep8
import time
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class for the project
    """

    def setUp(self):
        """ sets up the initial conditions for the test"""
        self.b1 = BaseModel()
        self.b2 = BaseModel()
        self.basedict = BaseModel()
        self.bsave = BaseModel()
        self.bmain = BaseModel()

    # attributes tests
    def test_uuid(self):
        """ checks if every id is unique """
        self.assertIsInstance(self.b1, BaseModel)
        self.assertTrue(hasattr(self.b1, "id"))
        self.assertNotEqual(self.b1, self.b2)
        self.assertIsInstance(self.b1.id, str)

    def test_created_updated(self):
        """ checks if the instance for created_at and updated_at
        are datetime objects """
        self.assertIsInstance(self.b2, BaseModel)
        self.assertTrue(hasattr(self.b2, "created_at"))
        self.assertTrue(hasattr(self.b2, "updated_at"))
        self.assertIsInstance(self.b2.created_at, datetime)
        self.assertIsInstance(self.b2.updated_at, datetime)
        self.assertNotEqual(self.b2.created_at, self.b2.updated_at)

    # methods tests
    def test_todict(self):
        """ checks if the values in dictionary are strings  """
        self.assertTrue(type(self.basedict.to_dict()) is dict)
        dictionary = self.basedict.to_dict()
        self.assertIsInstance(dictionary['created_at'], str)
        self.assertIsInstance(dictionary['updated_at'], str)
        self.assertIsInstance(dictionary['__class__'], str)
        self.assertIsInstance(dictionary['id'], str)

    def test_save(self):
        """ checks if updated_at is updated  """
        olddate = self.bsave.updated_at
        time.sleep(2)
        self.bsave.save()  # update
        self.assertNotEqual(olddate, self.bsave.updated_at)
        self.assertIsInstance(self.bsave.updated_at, datetime)

    def test_str(self):
        """ checks if __str__ returns a string  """
        self.assertIsInstance(self.b1.__str__(), str)

    def test_main(self):
        """ checks if new attributes are added to the dictionarry  """
        dictionary1 = self.bmain.to_dict()
        self.bmain.name = "Holberton"
        self.bmain.my_number = 89
        dictionary2 = self.bmain.to_dict()
        self.assertNotEqual(len(dictionary1), len(dictionary2))

    def test_kwargs(self):
        """ checks if an instance is created from a dictionary """
        dictionary = self.b1.to_dict()
        b1_copy_test = BaseModel(**dictionary)
        self.assertIsInstance(b1_copy_test, BaseModel)

    def test_dict_not_same_object(self):
        """ checks if an instance and its copy are different objects """
        dictionary = self.b1.to_dict()
        b1_copy_test = BaseModel(**dictionary)
        self.assertIsNot(self.b1, b1_copy_test)
        self.assertEqual(b1_copy_test.id, self.b1.id)
        self.assertEqual(b1_copy_test.created_at, self.b1.created_at)
        self.assertEqual(b1_copy_test.updated_at, self.b1.updated_at)

    def test_empty_dict(self):
        """ checks if a new instance is created from an empty dictionary """
        my_instance = BaseModel({})
        self.assertIsInstance(my_instance, BaseModel)

    def test_docstring_BaseModel(self):
        """ checks if docstrings are present """
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)

    def test_basemodel_pep8(self):
        """ checks for pep8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base_model.py'])
        self.assertEqual(result.total_errors, 0)
