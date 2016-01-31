__author__ = 'Jessy'


##  Import unittest class to test a method in a TestGame class
##  Import blue class from game file to test a method in a blue class

import unittest

from game import blue



class TestGame(unittest.TestCase):

##   testing if the user number and computer number are equal
#    and display the message, if the number were equal
    def test_compareNum(self):

        the_game=blue()
        the_game.numberUser = 15   ##  give a user and computer a same number to test the equality
        the_game.number =15
        self.assertEqual(the_game.compareNum(),0,"The number is same")


##   testing if the user and computer number are not equal, and if the user number is too high from the
##   computer number and display the message
    def test_compareNotEqual(self):

        the_game=blue()
        the_game.numberUser = 15   ##  give user a higher number than a computer number to test
        the_game.number =14
        self.assertEqual(the_game.compareNum(),-1,"The number is too high")



##   testing if the user and computer number are not equal, and if the user number is too low from the
##   computer number and display the message
    def test_compareNotEqualA(self):

        the_game=blue()
        the_game.numberUser = 10        ##  give the user number lower than a computer number to test
        the_game.number =14
        self.assertEqual(the_game.compareNum(),1,"The number is too low")


