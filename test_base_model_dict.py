#!/usr/bin/python3
from models.base_model import BaseModel
"""This is the comment I Have to write

    This is the comment I Have to write

    This is the comment I Have to write
    This is the comment I Have to write
    """

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
"""This is the comment I Have to write

    This is the comment I Have to write

    This is the comment I Have to write
    This is the comment I Have to write
    """
for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]),
                                       my_model_json[key]))

        print("--")
        my_new_model = BaseModel(**my_model_json)
        print(my_new_model.id)
        print(my_new_model)
        print(type(my_new_model.created_at))

        print("--")
        print(my_model is my_new_model)

