#!/usr/bin/python3
# - state module

from models.base_models import BaseModel
""" State module """


class State(baseModel):
    """ class with the name of the states """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Overriding constructor """
        super().__init__(*args, *kwargs)
