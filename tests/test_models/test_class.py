#!/usr/bin/python3
'''This is the comment I Have to write'''
import inspect
import pep8



class TestClassDocumentation():
    '''This is the comment I Have to write'''


    def __init__(self, tests, _class):
        '''This is the comment I Have to write'''
        self.tests = tests
        self.name = _class


        # Get all the methods of class @name
        self.functions = inspect.getmembers(self.name, inspect.isfunction)


    def documentation(self):
        '''This is the comment I Have to write'''
        with self.tests.subTest(msg='Testing methods'):
            for f in self.functions:
                with self.tests.subTest(msg='Documentation method {}'
                                        .format(f[0])):


                    doc = f[1].__doc__
                    self.tests.assertGreaterEqual(len(doc), 1)


        with self.tests.subTest(msg='Testing class'):
            doc = self.name.__doc__
            self.tests.assertGreaterEqual(len(doc), 1)


    def pep8(self, files):
        '''This is the comment I Have to write'''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(files)
        self.tests.assertEqual(result.total_errors, 0,
                               'Found code style errors (and warnings)."')


if __name__ == '__main__':
    unittest.main()
