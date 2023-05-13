#!/usr/bin/python3
"""Module that contains class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for User instances"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
