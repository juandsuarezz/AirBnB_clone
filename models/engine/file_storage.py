#!/usr/bin/python3
"""
This module contains code related to file storage
for the airbnb clone project
"""
import json
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    serializes instances to a JSON file
    """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __object with key id
        """
        if obj:
            self.__objects["{}.{}".format(str(type(obj).__name__),
                                          obj.id)] = obj

    def save(self):
        """
        Serializes __objects to JSON file
        """
        for key, value in self.__objects.items():
            if not isinstance(value, dict):
                self.__objects[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects if file exists
        """
        try:
            with open(self.__file_path, encoding="UTF-8") as f:
                obj = json.load(f)
            for key, value in obj.items():
                self.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            pass
