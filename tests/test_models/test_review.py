#!/usr/bin/python3
'''This is the comment I Have to write'''
import unittest
import json
import pep8
import datetime


from models.review import Review
from models.base_model import BaseModel



class TestReview(unittest.TestCase):
    '''This is the comment I Have to write'''
    def test_doc_module(self):
        '''This is the comment I Have to write'''
        doc = Review.__doc__
        self.assertGreater(len(doc), 1)


    def test_pep8_conformance_review(self):
        '''This is the comment I Have to write'''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


    def test_pep8_conformance_test_review(self):
        '''This is the comment I Have to write'''
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")


    def test_doc_constructor(self):
        '''This is the comment I Have to write'''
        doc = Review.__init__.__doc__
        self.assertGreater(len(doc), 1)


    def test_class(self):
        '''This is the comment I Have to write'''
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Review, BaseModel))


        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Review.place_id, str)
            self.assertIsInstance(Review.user_id, str)
            self.assertIsInstance(Review.text, str)


if __name__ == '__main__':
    unittest.main()
