#!/usr/bin/python3

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
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%y-%m-%dt%H:%M:%S.%f"
                elif key != '__class__':
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.update_at = self.created_at
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

    def from_dict(cls, dict_rep):
        """Creates an instance from a dirctionary representation.

        Args:
            cls: The class of the instance to create.
            dict_rep: A dictionary representation of the instance.

        Returns:
            A new instance of the class with attributes from the dictionary.
        """
        if '__class__' in dict_rep:
            class_name = dict_rep[ '__class__']
            if cls.__name__ == class_name:
                return cls(**dict_rep)
        return None
