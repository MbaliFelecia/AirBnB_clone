#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage

class BaseModels:
    """class from which all other classes will inherit"""

    def __init__(self, *args, **kwargs):
    """ initializes intances attributes

    Args:
        *args: list of arguements
        **kwargs: dict of key-value arguments
    """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(kwargs["created_at"], "%y-%m-%dt%H:%M:%S.%f"
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(kwargs["update_at"], "%Y-%m-%dT%H:%M:%S.%f"
                elif key == "id":
                    self.__dict__[key] = kwargs[key]

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.update_at = datetime.now()
            storage.new(self)

    def __str__(self):
        class_name = "[" + self.__class__.__name__ + "]"
        dct = {k: v for (k, v) in self.__dict__.items() if v is not None}
        return class_name + " (" + self.id + ") " + str(dct)

            return "[{}] ({}) {}".format(type(self).__name, self.id, self.__dict__)

    def save(self):
        self.update_at = datetime.now()
        storage.save()

    def to_dict(self):
        new_dict = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                new_dict[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if value is not None:
                    new_dict[key] = value
        new_dict['__class__'] = self.__class__.__name
        return new_dict
