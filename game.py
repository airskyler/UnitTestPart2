__author__ = 'Jessy'


##   LAB 3, Part 2

##   I got some help from my classmate Boyd for this problem

import random


class blue:

##  set the value on the variable to start with

    number = 0

    numberUser = -1


    def __init__(self):
        self.count =0      # count variable


    def makeRandomNum(self):
        self.number = random.randint(1, 11)   # set random number variable from computer


##   get user input and set the user input in a variable
    def userInput(self):
        numberUser = int(input("Please pick one number from range between 1 to 11\n"))

        self.numberUser = numberUser


##   method to count, how many games were played, for the user to guess the correct number
##   that computer have generated
    def countNum(self):
        self.count = self.count +1


##   display the message, if the user guessed the correct number
    def disPlayCorrectNum(self):
        print("You guess the correct number! - it took - ")
        print(str(self.count)+ " time to guess the correct number\n")


##    display the message, if the user guessed, too low of the number
    def disPlayLowNum(self):
        print("Hint... you guess the number too low\n")



##    display the message, if the user guessed, too high of the number
    def disPlayHigh(self):
         print("Hint... you guess the number too high\n")



##    method to compare the user number and computer number and return the value
    def compareNum(self):

        if self.number == self.numberUser:
            return 0

        elif self.number > self.numberUser:
            return 1

        elif self.number < self.numberUser:
            return -1



    def main(self):

        self.makeRandomNum()

##   keep playing the guessing number game till the user guess the correct number

        while True:
            self.userInput()

            if self.compareNum()== 0:
                self.disPlayCorrectNum()
                print(" guess time count is "+str(self.count ))
                break

            elif self.compareNum() == 1:
                self.countNum()
                self.disPlayLowNum()

            elif self.compareNum() == -1:
                self.countNum()
                self.disPlayHigh()



if __name__== '__main__':

    GameNumber = blue()
    GameNumber.main()






