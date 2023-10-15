#!/usr/bin/python3
# - user module
from models.base_model import BaseModel

""" a class User that inherits from BaseModel """


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Overriding constructor"""
        super().__init__(*args, **kwargs)
