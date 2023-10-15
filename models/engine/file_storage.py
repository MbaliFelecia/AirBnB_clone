#!/usr/bin/python3
"""
Class FileStorage that serializes to a JSON file
and deserializes Json file to instances
"""
import json
import os

class FileStorage:
    """ Class FileStorage that serializes and deserializes JSON objects """

    __file_path = 'file.json'
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
            '''json.dump(obj_dict, f)'''

    def reload(self):
        """ Deserializes the JSON file to __object if __file_path exists
        otherwise does nothing, with no exception being reaised """

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                    obj_dict = json.load(file)
                    for key,obj_data in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        obj_cls = globals().get(class_name)
                        if obj_cls:
                            obj = obj_cls(**obj_data)
                            self.new(obj) 
