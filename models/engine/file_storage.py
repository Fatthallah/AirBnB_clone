#!/usr/bin/python3
"""the comment to be checked a"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """
    the comment to be checked b:
    ------------------
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        the comment to be checked c
        the comment to be checked g
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        the comment to be checked xx
        the comment to be checked oki
        sdd:
        ----------
        the comment to be checkeddffdfdf
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """
        the comment to be checked dfdfd
        the comment to be checked rgfgfg
        fggfgs:
        ----------
        nthe comment to be checked
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict().copy()
        with open(FileStorage.__file_path, mode='w') as my_file:
            json.dump(new_dict, my_file)

    def reload(self):
        """
        the comment to be checked fddfdf
        the comment to be checkedrtrtrtr
        """
        try:
            with open(FileStorage.__file_path, mode='r') as my_file:
                new_dict = json.load(my_file)

            for key, value in new_dict.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass

