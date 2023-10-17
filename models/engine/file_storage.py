#!/usr/bin/python3
"""
Class FileStorage that serializes to a JSON file
and deserializes Json file to instances
"""
import json
import os


class FileStorage:
    """ Class FileStorage that serializes and deserializes JSON objects """

    __file_path = "file.json"
    __objects = {}


    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Set in __objects the obj with key <obj class name>.id """
        key = "{0}.{1}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj 

    def save(self):
        """ Serializes __objects to JSON file __file_path """
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    @staticmethod

    def classes():

      from models.base_model import BaseModel
      from models.amenity import Amenity
      from models.city import City
      from models.place import Place
      from models.review import Review
      from models.state import State
      from models.user import User

    classes = {
            "BaseModel": BaseModel,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
        }

        return classes


    def load_previous_data(self):
        """ Reloading from previous data """
        if not os.path.isfile(FilStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["_class_"]](**v) for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    @staticmethod
    def attributes():
        """Returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel": {
                "id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime
            },
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str
            },
            "State": {
                "name": str
            },
            "City": {
                "state_id": str,
                "name": str
            },
            "Amenity": {
                "name": str
            },
            "Place": {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list
            },
            "Review": {
                "place_id": str,
                "user_id": str,
                "text": str
            }
        }
        return attributes

    def reload(self):
        """ Deserializes the JSON file to __object if __file_path exists
        otherwise does nothing, with no exception being reaised """
        

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    for k, v in value.items():
                        if k == 'created_at' or k == 'updated_at':
                            value[k] = datetime.fromisoformat(v)
                    cls_name = value['__class__']
                    cls = models.classes.get(cls_name)
                    if cls:
                        self.new(cls(**value))
