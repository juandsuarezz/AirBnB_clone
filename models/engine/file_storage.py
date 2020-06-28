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
        dic = {}
        for id, objs in self.__objects.items():
            dic[id] = objs.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as f:
            json.dump(dic, f)

    def reload(self):
        try:
            with open(self.__file_path, encoding="UTF-8") as f:
                obj = json.load(f)
            for key, value in obj.items():
                self.__objects[key] = models.allclasses[value["__class__"]](**value)
        except FileNotFoundError:
            pass
