#!/usr/bin/python3
import uuid
import datetime
from models import storage
""" BaseModel class module """


class BaseModel():
    """Base class for all other clsses """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel
        """
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        
    def __str__(self):
        """ Returns the string representaion of the model """
        return f"{self.__class__.__name__}, {self.id}, {self.__dict__}"
    
    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary representation of the model """
        model_dict = self.__dict__.copy()
        model_dict["__class__"] = type(self).__name__
        model_dict["created_at"] = model_dict["created_at"].isoformat()
        model_dict["updated_at"] = model_dict["updated_at"].isoformat()
        return model_dict
