!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage

class BaseModels:
    """class from which all other classes will inherit"""

    def __int__(self, *args, **kwargs):
    """ ïnitiales intances attributes

    Args:
        *aegs: list of arguements
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
            self.id =str(uuid4))
            self.created_at = datetime.now()
            self.update_at = datetime.now()
            storage.new(self)

            def __str__(self):

            return "[{}] ({}) {}".format(type(self).__name, self.id, self.__dict__)

            def save(self):
            self.update_at = datetime.now()
            storage.save()

            def to_dict(self)

            my_dict = self.__dict__.copy()
            my_dict["__class__"] = type(self).__name__
            my_dict["created_at"] = my_dict["created_at"].isoformat()
            

