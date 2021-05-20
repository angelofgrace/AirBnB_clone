#!/usr/bin/python3
"""Storage componenet for consone"""


from models.base_model import BaseModel
import json
from os import path
from datetime import datetime


class FileStorage:

    __file_path = "CVanndys_excellent_OOP.json"
    __objects = {}

    def all(self):
         
        return FileStorage.__objects

        # new dictionary entry, passed object as parameter
    def new(self, obj):
        """ new() formats and passes objects to an appendable dict """
        """ making a key: a string, <class>.id """
        new_key = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[new_key] = obj

    def save(self):
        """ Storing __objects in a JSON file """
        to_be_json = {}
        """ loop through key/value pairs in __objects """
        for k, v in FileStorage.__objects.items():
            """ store a copy of each instance, v """
            to_be_json[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w') as FS:
            """ Dump list of dictionaries (to_be_json) to file as JSON string """
            json.dump(to_be_json, FS)

    def reload(self):
        """ convert JSON file back to python dict of dict: __objects """
        if not path.exists(FileStorage.__file_path):
            return None
        with open(FileStorage.__file_path, "r") as FS:
            FileStorage.__objects = json.loads(FS.read())
