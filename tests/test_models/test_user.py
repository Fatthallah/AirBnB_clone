#!/usr/bin/python3
'''This is the comment I Have to write'''
import unittest
import json
import pep8
import datetime


from models.user import User
from models.base_model import BaseModel



class TestUser(unittest.TestCase):
    '''This is the comment I Have to write'''
    def test_doc_module(self):
        '''This is the comment I Have to write'''
        doc = User.__doc__
        self.assertGreater(len(doc), 1)


    def test_pep8_conformance_base_model(self):
        '''This is the comment I Have to write'''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


    def test_pep8_conformance_test_base_model(self):
        '''This is the comment I Have to write'''
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")


    def test_doc_constructor(self):
        '''This is the comment I Have to write'''
        doc = User.__init__.__doc__
        self.assertGreater(len(doc), 1)


    def test_class(self):
        '''This is the comment I Have to write'''
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(User, BaseModel))


        with self.subTest(msg='Attributes'):
            self.assertIsInstance(User.email, str)
            self.assertIsInstance(User.password, str)
            self.assertIsInstance(User.first_name, str)
            self.assertIsInstance(User.last_name, str)


if __name__ == '__main__':
    unittest.main()
