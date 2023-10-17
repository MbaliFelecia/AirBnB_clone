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

    '''def save(self):
        """ Serializes __objects to JSON file __file_path """
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)'''

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """ Deserializes the JSON file to __objects if __file_path exists
        otherwise do nothing, with no exception being reaised """
        # if file doesnt exists it returns
        file_name = FileStorage.__file_path
        if (not os.path.exists(file_name)) or os.stat(file_name).st_size == 0:
            return
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        classes = {"BaseModel": BaseModel,
                   "Amenity": Amenity,
                   "City": City,
                   "Place": Place,
                   "Review": Review,
                   "State": State,
                   "User": User}
        with open(FileStorage.__file_path, "r") as f:
            thing = json.load(f)
        for key, value in thing.items():
            if value['__class__'] in classes.keys():
                value = classes[key.split(".")[0]](**value)
                FileStorage.__objects.update({key: value})
            else:
                print("** class doesn't exist **")
                FileStorage.__objects.update({key: None})

    '''def reload(self):
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
                        self.new(cls(**value))'''
