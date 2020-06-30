#!/usr/bin/python3
"""class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """rep of user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """init user"""
        super().__init__(*args, **kwargs)
