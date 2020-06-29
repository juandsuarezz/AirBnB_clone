#!/usr/bin/python3
"""
Class User inheriting from superclass BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Creating public class attributes.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Instantiation of argument if it exists and is a dictionary.
        """
        if (args and type(args[0]) is dict):
            BaseModel.__init__(self, args[0])
        else:
            BaseModel.__init__(self)
