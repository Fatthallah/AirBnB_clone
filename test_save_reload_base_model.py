#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
"""This is the comment I Have to write

    This is the comment I Have to write

    This is the comment I Have to write
    This is the comment I Have to write
    """

"""This is the comment I Have to write

    This is the comment I Have to write

    This is the comment I Have to write
    This is the comment I Have to write
    """
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

"""This is the comment I Have to write

    This is the comment I Have to write

    This is the comment I Have to write
    This is the comment I Have to write
    """
print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
my_model.save()
print(my_model)

