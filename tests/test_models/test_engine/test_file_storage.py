#!/usr/bin/python3
"""Test cases for FileStorage class"""
import unittest
import pep8
import json
import os
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """ Set a variable """
        self.my_model = BaseModel()
        self.file_sto = FileStorage()

    def tearDown(self):
        """Tears down test methods"""
        pass

    def test_FileStorage_pep8(self):
        """pep8 test"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)

    def test_instantiation(self):
        """Test instantiation of storage class"""
        self.assertEqual(type(models.storage).__name__, "FileStorage")

    def test_init_no_args(self):
        """Test __init__ without arguments"""
        with self.assertRaises(TypeError) as error:
            FileStorage.__init__()
        fail = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(error.exception), fail)

    def test_init_many_args(self):
        """Test __init__ with many arguments"""
        with self.assertRaises(TypeError) as error:
            base = FileStorage(67, 7, 12, 9, 4, 5)
        fail = "object() takes no parameters"
        self.assertEqual(str(error.exception), fail)

    def test_attributes(self):
        """Test class attributes"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertIsInstance(models.storage._FileStorage__objects, dict)
        self.assertIsInstance(models.storage._FileStorage__file_path, str)

        storage2 = FileStorage()
        self.assertIsInstance(storage2, FileStorage)
        self.assertIsNot(models.storage, storage2)

    def test_all(self):
        """Test the all method"""
        storage = FileStorage()
        objs = storage.all()
        self.assertIsInstance(objs, dict)
        self.assertFalse(objs == {})

    def test_file_storage_doc(self):
        """ Check the documentation """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.__init__.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)
        self.assertIsNotNone(FileStorage.delete.__doc__)

    def test_field_storage_exist(self):
        """ Check if methods exists """
        self.assertTrue(hasattr(self.file_sto, "__init__"))
        self.assertTrue(hasattr(self.file_sto, "all"))
        self.assertTrue(hasattr(self.file_sto, "new"))
        self.assertTrue(hasattr(self.file_sto, "save"))
        self.assertTrue(hasattr(self.file_sto, "reload"))
        self.assertTrue(hasattr(self.file_sto, "delete"))

    def test_models_save(self):
        """ Check if the save function works """
        self.my_model.name = "Halo"
        self.my_model.save()
        models.storage.reload()
        models.storage.all()
        self.assertTrue(models.storage.all(), "Holberton")
        self.assertIsInstance(models.storage.all(), dict)
        self.assertTrue(hasattr(self.my_model, 'save'))
        self.assertNotEqual(self.my_model.created_at, self.my_model.updated_at)

    def test_delete(self):
        """Tests the method delete (obj, called from destroy method)"""
        storage = FileStorage()
        state = State()
        state.id = 123455
        state.name = "Medellin"
        key = state.__class__.__name__ + "." + str(state.id)
        storage.new(state)
        storage.delete(state)
        obj = storage.all()
        self.assertTrue(key not in obj.keys())

    def test_reload(self):
        """Test the reload method"""
        test_1 = BaseModel()
        test_1.save()
        test_1.name = "Holberton"
        test_1.number = 1
        test_1.save()
        self.assertTrue(os.path.exists("file.json"))
        dic = {}
        with open('file.json', 'r') as fjson:
            dic = json.loads(fjson.read())
        test_1_key = test_1.__class__.__name__ + '.' + test_1.id
        self.assertDictEqual(test_1.to_dict(), dic[test_1_key])

    def test_new(self):
        """ Test the new method"""
        test_1 = BaseModel()
        test_1.name = "Holberton"
        test_2 = BaseModel()
        test_2.name = "Holberton"
        id_tests_1 = test_1.id
        id_tests_2 = test_2.id
        self.assertFalse(id_tests_1 == id_tests_2)

if __name__ == '__main__':
    unittest.main()
