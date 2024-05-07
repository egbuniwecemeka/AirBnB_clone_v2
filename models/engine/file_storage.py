#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import shlex


class FileStorage:
    """This class serializes instances to JSON format/file
       and deserializes JSON format/file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary

        Args:
            cls: Filter for class type(optional)

        Return:
            returns dict of .__object
        """

        if cls:
            filtered_objects = {}
            for key, obj in self.__objects.items():
                obj_id = key.split('.')
                if obj_id[0] == cls.__name__:
                    filtered_objects[key] = obj
            return (filtered_objects)
        else:
            return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    class_name, obj_id = key.split('.')
                    obj_cls = classes[class_name]
                    self.__objects[key] = obj_cls(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Deletes an obj from __object if present """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """ reload to deserialize the JSON file to object """
        self.reload()
