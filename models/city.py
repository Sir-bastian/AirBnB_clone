#!/usr/bin/python3
# - city module
from models.base_model import BaseModel
""" City module """


class City(BaseModel):
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
