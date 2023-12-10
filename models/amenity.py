#!/usr/bin/python3
'''the comment to be checked 1'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''the comment to be checked 2'''

    name = ""

    def __init__(self, *args, **kwargs):
        """the comment to be checked 3"""
        super().__init__(*args, **kwargs)

