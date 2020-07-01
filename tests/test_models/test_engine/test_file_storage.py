#!/usr/bin/python3
"""
Module of the Amenity unittest
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test of the FileStorage class
    """

    # Specific set up of the unittest
    def setUp(self):
        """Instance of the class"""
        self.inst = FileStorage()

    def tearDown(self):
        """Deleting of the instance with the proper file"""
        del self.inst

        try:
            os.remove("file.json")
        except BaseException:
            pass

    # Functionality
    def test_AtributtesClass(self):
        self.inst.name = "Nicolas"
        self.assertEqual(str, type(self.inst.name))
        self.assertEqual("Nicolas", self.inst.name)

    # Documentation
    def test_ModuleDocstring(self):
        """Testing the documentation of the module"""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_MethodsDocstring(self):
        """Testing the documentation of the different methods"""
        for doc in dir(FileStorage):
            self.assertIsNotNone(doc.__doc__)

    # Existence and types
    def test_IsInstance(self):
        """Testing the existence of the instance"""
        self.assertIsInstance(self.inst, FileStorage)

    def test_File(self):
        """The existence of the json file"""
        self.inst.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_Methods(self):
        """Testing the existence of the different methods"""
        self.assertTrue(hasattr(FileStorage, "__init__"))
        self.assertTrue(hasattr(FileStorage, "__str__"))
        self.assertTrue(hasattr(FileStorage, "save"))

if __name__ == "__main__":
    unittest.main()
