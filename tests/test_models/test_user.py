#!/usr/bin/python3
"""
Module of the User unittest
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test of the User class
    """

    # Specific set up of the unittest
    def setUp(self):
        """Instance of the class"""
        self.inst = User()

    def tearDown(self):
        """Deleting of the instance with the proper file"""
        del self.inst

        try:
            os.remove("file.json")
        except BaseException:
            pass

    # Functionality
    def test_AtributtesClass(self):
        self.assertEqual(str, type(self.inst.email))
        self.assertEqual(str, type(self.inst.password))
        self.assertEqual(str, type(self.inst.first_name))
        self.assertEqual(str, type(self.inst.last_name))

    # Documentation
    def test_ModuleDocstring(self):
        """Testing the documentation of the module"""
        self.assertIsNotNone(User.__doc__)

    def test_MethodsDocstring(self):
        """Testing the documentation of the different methods"""
        for doc in dir(User):
            self.assertIsNotNone(doc.__doc__)

    # Existence and types
    def test_IsInstance(self):
        """Testing the existence of the instance"""
        self.assertIsInstance(self.inst, User)

    def test_TypeId(self):
        """Test the type of the method id"""
        self.assertEqual(str, type(self.inst.id))

    def test_File(self):
        """The existence of the json file"""
        self.inst.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_Attrs(self):
        """Testing the existence of the different methods"""
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))

    def test_ClassDict(self):
        """Testing the dictionary of the class"""
        ClassDict = self.inst.to_dict()
        self.assertEqual(dict, type(ClassDict))
        self.assertIsInstance(ClassDict["created_at"], str)
        self.assertIsInstance(ClassDict["updated_at"], str)

if __name__ == "__main__":
    unittest.main()
