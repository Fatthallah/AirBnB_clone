#!/usr/bin/python3
'''This is the comment I Have to write'''


import unittest
import console
from console import HBNBCommand



class test_console(unittest.TestCase):
    '''This is the comment I Have to write'''


    def create(self):
        '''This is the comment I Have to write'''
        return HBNBCommand()


    def test_quit(self):
        '''This is the comment I Have to write'''
        con = self.create()
        self.assertTrue(con.onecmd("quit"))


    def test_EOF(self):
        '''This is the comment I Have to write'''
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))
