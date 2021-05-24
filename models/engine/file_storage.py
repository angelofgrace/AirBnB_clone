#!/usr/bin/python3
"""Storage componenet for consone"""


from models.base_model import BaseModel
import json
from os import path
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:

    # __file_path is defined as storage in __init__ ???
    __file_path = "file.json"
    __objects = {}
    class_inits = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review}

    def all(self):
        # at __init__ update() refreshes __objects dict
        """all returns all object instances in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """ new() formats and passes objects to an appendable dict """
        """ new_key is set as a string in format ' <class>.id' """
        new_key = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[new_key] = obj

    # are we able to replace any of this code with "storage"??
    def save(self):
        """save() serializes __objects contents to a JSON file """
        to_be_json = {}
        """ loop through key/value pairs in __objects """
        for k, v in FileStorage.__objects.items():
            """ store a copy of each instance, v """
            to_be_json[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w') as FS:
            """ Dump list of dicts (to_be_json) to file as JSON string """
            json.dump(to_be_json, FS)

    def reload(self):
        """reload deserializes JSON file into  __objects"""
        # reload() is called in __init__, deserializes json string to a dict of
        # dicts in __objects
        if not path.exists(FileStorage.__file_path):
            return None
        with open(FileStorage.__file_path, "r") as FS:
            tempDictofDicts = json.loads(FS.read())
        for key in tempDictofDicts.keys():
            # loop through dictionary of classes/class instantiating methods
            # *****CHRIS NEEDS TO GO OVER THIS BLOCK OF CODE*****
            for cls_name in FileStorage.class_inits.keys():
                if cls_name in key:
                    # if match, call instantiation with TDD value as parameter
                    FileStorage.__objects[key] = FileStorage.class_inits[
                        cls_name](**(tempDictofDicts[key]))
