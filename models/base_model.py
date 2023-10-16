#!/usr/bin/python3
""" Class BaseModel defines common attributes/methods for classes"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """class from which all other classes will inherit"""

    def __init__(self, *args, **kwargs):
        """ initializes intances attributes
        Args:
            *args: list of arguements
            **kwargs: dict of key-value arguments
        """

        if kwargs:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], f)
                elif key != '__class__':
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """ Prints strings representing class """

        class_name = "[" + self.__class__.__name__ + "]"
        dct = {k: v for (k, v) in self.__dict__.items() if v is not None}
        return class_name + " (" + self.id + ") " + str(dct)

        return "[{}] ({}) {}".format(type(self).__name, self.id, self.__dict__)

    def save(self):
        """ Update public instances attribute update_at with
        current datetime"""

        self.update_at = datetime.now()
        '''storage.save()'''

    def to_dict(self):
        """ Returns dictionary containing all keys/values """

        __dict__ = dict(self.__dict__)
        __dict__['__class__'] = type(self).__name__
        __dict__['created_at'] = self.created_at.isoformat()
        __dict__['updated_at'] = self.updated_at.isoformat()
        return __dict__
