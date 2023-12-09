#!/usr/bin/python3
'''This is the comment I Have to write'''
import unittest
import json
import pep8
import datetime


from models.amenity import Amenity
from models.base_model import BaseModel



class TestAmenity(unittest.TestCase):
    '''This is the comment I Have to write'''
    def test_doc_module(self):
        '''This is the comment I Have to write'''
        doc = Amenity.__doc__
        self.assertGreater(len(doc), 1)


    def test_pep8_conformance_amenity(self):
        '''This is the comment I Have to write'''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


    def test_pep8_conformance_test_amenity(self):
        '''This is the comment I Have to write'''
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")


    def test_doc_constructor(self):
        '''This is the comment I Have to write'''
        doc = Amenity.__init__.__doc__
        self.assertGreater(len(doc), 1)


    def test_class(self):
        '''This is the comment I Have to write'''
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Amenity, BaseModel))


        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Amenity.name, str)


if __name__ == '__main__':
    unittest.main()
