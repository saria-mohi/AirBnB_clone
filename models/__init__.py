#!/usr/bin/python3
"""Module for create an instance FileStorage"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review
}

storage = FileStorage()
storage.reload()
