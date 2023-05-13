#!/usr/bin/python3
"""Module for FileStorage class"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
import os


class FileStorage:
    """Class for serialization and deserialization to json format"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_d = FileStorage.__objects
        obj_json = {obj: json_d[obj].to_dict() for obj in json_d.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_json, file)

    def reload(self):
        """deserializes the JSON file to __objects
        """
        dict_ = {}
        try:
            with open(self.__file_path, "r") as f:
                dict_ = json.loads(f.read())
                for key, value in dict_.items():
                    class_name = key.split(".")
                    self.__objects[key] = eval(class_name[0])(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj (called in to_destroy)"""
        if obj:
            try:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                del self.__objects[key]
                self.save()
            except:
                pass
