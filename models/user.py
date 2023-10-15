#!/usr/bin/python3
""" Class User that inherits from BaseModel
that takes in user information """

from models.base_model import BaseModel


class User(BaseModel):
    """ Class use inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
