#!/usr/bin/python3
""" Class Review that inherits from BaseModel
take review information """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Review inherits from BaseModel """
    place_id = ""
    user_id = ""
    text = ""
