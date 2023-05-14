#!/usr/bin/python3
"""Test cases for Review class"""

import unittest
import time
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models import review
import inspect
Review = review.Review


class TestReview(unittest.TestCase):
    """tests for the Class Review"""

    def setUp(self):
        """Set up test methods"""
        pass

    def tearDown(self):
        """Tear Down test methods"""
        pass

    def test_Review_pep8(self):
        """pep8 test"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/review.py'])
        self.assertEqual(result.total_errors, 0)

    def test_Review_pep8(self):
        """pep8 test"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0)

    def test_review_module_docstring(self):
        """Test for the review.py module docstring"""
        self.assertIsNot(Review.__doc__, None,
                         "review.py without docstring")
        self.assertTrue(len(Review.__doc__) >= 1,
                        "review.py without docstring")

    def test_review_class_docstring(self):
        """Test for the Review class docstring"""
        self.assertIsNot(Review.__doc__, None,
                         "Review class without docstring")
        self.assertTrue(len(Review.__doc__) >= 1,
                        "Review class without docstring")

    def test_class_Review(self):
        """test for the class"""
        obj_review = Review()
        self.assertIsInstance(obj_review, Review)

    def test_subclass_BaseModel(self):
        """Test the review class is subclass of BaseModel"""
        obj_review = Review()
        self.assertIsInstance(obj_review, BaseModel)
        self.assertTrue(hasattr(obj_review, "id"))
        self.assertTrue(hasattr(obj_review, "created_at"))
        self.assertTrue(hasattr(obj_review, "updated_at"))

    def test_attributes_review(self):
        """Test review attributes"""
        attributes_review = {"place_id": str,
                             "user_id": str,
                             "text": str}
        obj_review = Review()
        for key, value in attributes_review.items():
            self.assertTrue(hasattr(obj_review, key))
            self.assertEqual(type(getattr(obj_review, key, None)), value)

    def test_str(self):
        """Test str method"""
        obj_review = Review()
        string = "[Review] ({}) {}".format(
                 obj_review.id, obj_review.__dict__)
        self.assertEqual(string, str(obj_review))

    def test_to_dict_review_attributes(self):
        """Test to_dict method creates a dictionary with expected attributes"""
        obj_review = Review()
        new_dict = obj_review.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attributes in obj_review.__dict__:
            self.assertTrue(attributes in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_to_dict_review_values(self):
        """Test dictionary values"""
        obj_review = Review()
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        new_dict = obj_review.to_dict()
        self.assertEqual(new_dict["__class__"], "Review")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         obj_review.created_at.strftime(t_format))
        self.assertEqual(new_dict["updated_at"],
                         obj_review.updated_at.strftime(t_format))

    def test_save(self):
        """Test save method"""
        obj_review = Review()
        before = obj_review.updated_at
        time.sleep(2)
        obj_review.save()
        self.assertLess(before, obj_review.updated_at)
        with open("file.json", "r") as file:
            self.assertIn("Review." + obj_review.id, file.read())

if __name__ == "__main__":
    unittest.main()
