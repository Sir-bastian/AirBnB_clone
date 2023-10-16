#!/usr/bin/python3

from models.base_model import BaseModel

"""amenity module """


class Amenity(BaseModel):
    """Amenity classs that inherits from BAseModel class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Overriding constrctor"""
        super().__init__(self, *args, **kwargs)
