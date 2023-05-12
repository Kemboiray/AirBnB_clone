#!/usr/bin/python3
"""Defines class ``BaseModel`` """

import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Base class """

    def __init__(self, *args, **kwargs):
        """Constructor method """

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """Print a description of the class instance """
        temp = self.__dict__
        #temp['created_at'] = datetime.fromisoformat(temp['created_at'])
        #temp['updated_at'] = datetime.fromisoformat(temp['updated_at'])
        return f'[{self.cls_name()}] ({self.id}) {temp}'

    def save(self):
        """Update ``updated_at`` with the current datetime """
        models.storage.save()

    def to_dict(self):
        """Return a dictionary description of the instance """
        my_dict = self.__dict__
        my_dict['__class__'] = self.cls_name()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict

    @classmethod
    def cls_name(cls):
        """Return an instance's class name """
        return cls.__name__
