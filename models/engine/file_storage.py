#!/usr/bin/python3

import json
import models

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):

        return (self.__objects)

    def new(self, obj):

        if obj:
            self.__objects["{}.{}".format(str(type(obj).__name__),
                                          obj.id)] = obj

    def save(self):

        for key, value in self.__objects.items():
            if not isinstance(value, dict):
                self.__objects[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as f:
            json.dump(self.__objects, f)

    def reload(self):

        try:
            with open(self.__file_path, encoding="UTF-8") as f:
                obj = json.load(f)
            for key, value in obj.items():
                self.__objects[key] = models.allclasses[value["__class__"]](**value)
        except FileNotFoundError:
            pass
