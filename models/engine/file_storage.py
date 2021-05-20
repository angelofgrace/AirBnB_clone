#!/usr/bin/python3
"""Storage componenet for consone"""


from models.base_model import BaseModel
import json


class FileStorage:

    __file_path = "CVanndys_excellent_OOP.json"
    __objects = {}

    def all(self):
         
        return FileStorage.__objects

        # new dictionary entry, passed object as parameter
    def new(self, obj):
        """new() formats and passes objects to an appendable dict """
        # making a key, and the key is a string
        print(obj)
        print("^^^ the obj passed to new() function ^^^")
        # why must type(obj).__name but can obj.id???
        new_key = type(obj).__name__ + "." + obj.id
        print(new_key)
        print("checking formatting for new object")
        FileStorage.__objects[new_key] = obj

    def save(self):
        # the obj is a dictionary
        to_be_json = {}
        # loop through key/value in filestorage.__objects
        for k, v in FileStorage.__objects.items():
            to_be_json[k] = v.to_dict() 
            print("k: {} and v: {}".format(k, v))
            print("^^^ printing list of objects in __objects^^^")
        with open(FileStorage.__file_path, 'w') as FS:
            json.dump(to_be_json, FS)
           
        #  use to_dic to update new dict info from filestorage.__objects
        #  json dump dict to file

    '''def reload(self):
          """read json file, create python objects"""
          if file does not exist
              raise Exception
          open file
          json load to temp_obj variable
          loop through temp obj (key:value pairs)
               temp_obj is a dict containing dicts
          store variables in filestoreag.__objects'''
