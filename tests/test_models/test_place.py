#!/usr/bin/python3
"""
Module of the City unittest
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test of the Place class
    """

    # Specific set up of the unittest
    def setUp(self):
        """Instance of the class"""
        self.inst = Place()

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
        self.assertEqual("Nicolas", self.inst.name)
        self.assertEqual(str, type(self.inst.city_id))
        self.assertEqual(str, type(self.inst.user_id))
        self.assertEqual(str, type(self.inst.name))
        self.assertEqual(str, type(self.inst.description))
        self.assertEqual(int, type(self.inst.number_rooms))
        self.assertEqual(int, type(self.inst.number_bathrooms))
        self.assertEqual(int, type(self.inst.max_guest))
        self.assertEqual(int, type(self.inst.price_by_night))
        self.assertEqual(float, type(self.inst.latitude))
        self.assertEqual(float, type(self.inst.longitude))
        self.assertEqual(list, type(self.inst.amenity_ids))

    # Documentation
    def test_ModuleDocstring(self):
        """Testing the documentation of the module"""
        self.assertIsNotNone(Place.__doc__)

    def test_MethodsDocstring(self):
        """Testing the documentation of the different methods"""
        for doc in dir(Place):
            self.assertIsNotNone(doc.__doc__)

    # Existence and types
    def test_IsInstance(self):
        """Testing the existence of the instance"""
        self.assertIsInstance(self.inst, Place)

    def test_TypeId(self):
        """Test the type of the method id"""
        self.assertEqual(str, type(self.inst.id))

    def test_File(self):
        """The existence of the json file"""
        self.inst.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_Methods(self):
        """Testing the existence of the different methods"""
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "amenity_ids"))

    def test_ClassDict(self):
        """Testing the dictionary of the class"""
        ClassDict = self.inst.to_dict()
        self.assertEqual(dict, type(ClassDict))
        self.assertIsInstance(ClassDict["created_at"], str)
        self.assertIsInstance(ClassDict["updated_at"], str)

if __name__ == "__main__":
    unittest.main()
