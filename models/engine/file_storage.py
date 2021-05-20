!/usr/bin/python3
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
        # making a key, and the key is a string
        print(obj)
        print("obj passed to new() function")
        new_key = type(obj).__name__ + "." + obj.id
        print(new_key)
        print("checking format of created object")
        FileStorage.__objects[new_key] = obj

    def save(self):
        #  the obj is a dictionary
        # make a new empty dict
        to_be_json = {}
        # open file
        # loop through key/value in filestorage.__objects
        for k, v in FileStorage.__objects.items():
            to_be_json[k] = v.to_dict() 
            print("k: {} and v: {}".format(k, v))
        with open(FileStorage.__file_path, 'w') as FS:
            json.dump(to_be_json, FS)
           
        #  use to_dic to update new dict info from filestorage.__objects
        #  json dump dict to file

'''   def reload(self):
          """read json file, create python objects"""
          if file does not exist
              raise Exception
          open file
          json load to temp_obj variable
          loop through temp obj (key:value pairs)
               temp_obj is a dict containing dicts
          store variables in filestoreag.__objects'''
