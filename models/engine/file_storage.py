#!/usr/bin/python3
"""This is the File Storage module."""
import json
from datetime import datetime
from os.path import isfile
from models import *


class FileStorage():
    """A serlization and deserlization json files class."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            FileStorage.__objects.update({type(obj).__name__
                                          + "." + str(obj.id): obj})

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        store = {}
        for k in FileStorage.__objects.keys():
            store[k] = FileStorage.__objects[k].to_dict()
        with open(FileStorage.__file_path, 'w', encoding="UTF-8") as my_file:
            json.dump(store, my_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        clsses = {
            "BaseModel": BaseModel
        }
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                for value in json.load(file).values():
                    self.new(clsses[value['__class__']](**value))
