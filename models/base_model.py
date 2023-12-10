#!/usr/bin/python3
'''the comment to be checked 6'''


import uuid
from datetime import datetime
import models


class BaseModel():
    '''the comment to be checked 78'''
    def __init__(self, *args, **kwargs):
        '''the comment to be checked 48888'''
        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''the comment to be checked 4fdf'''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        '''the comment to be checked 4 rttrtrt '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''the comment to be checked 4 trtrtrt'''
        new_dict = dict(self.__dict__)
        new_dict['created_at'] = self.__dict__['created_at'].isoformat()
        new_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return (new_dict)

