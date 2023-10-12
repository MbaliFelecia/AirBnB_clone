#!/usr/bin/python3
"""
Class FileStorage that serializes to a JSON file
and deserializes Json file to instances
"""
import json
import os

class FileStorage:
    """ Class that serializes and deserializes JSON objects """
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """  class that serializes and deserializes JSON objects """
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj 

    def save(self):
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file, ensure_ascii=False)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8' as file:
                    obj_dict = json.load(file)
                    for key,obj_data in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        obj_cls = globals().get(class_name)
                        if obj_cls:
                            obj = obj_cls(**obj_data)
                            self.new(obj) 
