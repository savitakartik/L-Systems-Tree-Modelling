from typing import ItemsView
import os


class argsChecker:
    """
    Class containing methods to validate user input.
    """
    def __init__(self) -> None:
        pass
    
    def checkIter(self, argIter):
        #check if positive number below 100?
        try:
            assert (type(argIter) == int and argIter > 0 and argIter <= 100), "Check iterations argument"
        except Exception as e:
            print (e)

    def checkAngle(self, argAngle):
        #check if number b/w 0 and 360
        try:
            assert (type(argAngle) == int and argAngle >= 0 and argAngle < 360), "Check angle argument"
        except Exception as e:
            print (e)

    def checkAxiom(self, argAxiom):
        #check if "F" for now. if program can handle multiple letters in future, update letterSet
        try:
            letterSet=['F']
            assert (type(argAxiom) == str and len(argAxiom) == 1 and argAxiom in letterSet), "Check axiom argument"
        except Exception as e:
            print (e)
    
    def checkUpdateStrLetters(self, argUpdateStr):
        #check if each char in set of dictionary letters
        charSet=['F','+','-','[',']']
        try:
            for char in argUpdateStr:
                assert (char in charSet), "Please check your update string!"
                break

        except Exception as e:
            print (e)

    def checkUpdateStrRecursion(self, argUpdateStr):
        #check that updateStr provides the possibility to expand - should contain 'F'
        #rewrite input as array to include multiple constants
        #if program can handle multiple letters, it is sufficient if any one of the updateStrs contain a constant
        constants=['F']
        ifExists=False
        try:
            for char in argUpdateStr:
                if char in constants:
                #print(char)
                    ifExists=True
            assert (ifExists == True), "Please check that update string has a constant!"
        #return ifExists
        except Exception as e:
            print (e)

    #quick tests
    #print(checkIter(100)) #valid
    #print(checkIter(0)) #invalid
    #print(checkIter(10)) #valid
    #print(checkIter(101)) #invalid
    #print(checkIter(1)) #valid
    #print(checkIter('A')) #invalid
    
    #print(checkAngle(360))
    #print(checkAngle(0))
    #print(checkAngle(45))
    #print(checkAngle(-45))
    #print(checkAngle('A'))

    #print(checkAxiom('F'))
    #print(checkAxiom('A'))
    #print(checkAxiom('FF'))
    #print(checkAxiom('ABC'))
    #print(checkAxiom(1))
    #print(checkAxiom('+'))

    #print(checkUpdateStrLetters('ABC'))
    #print(checkUpdateStrLetters('+'))
    #print(checkUpdateStrLetters('[F+]'))
    #print(checkUpdateStrLetters('[F+-]'))
    #print(checkUpdateStrLetters('F+@'))
    #print(checkUpdateStrLetters('123'))

    #print('####')
    #print(checkUpdateStrRecursion('F'))
    #print(checkUpdateStrRecursion('AF'))
    #print(checkUpdateStrRecursion('F+-[]'))
    #print(checkUpdateStrRecursion('[+=]'))
    #print(checkUpdateStrRecursion('1'))
    #print(checkUpdateStrRecursion(123))

#input:
#display dict: alphabet:1-26, symbols
#how many alphabet? n 
#show A,B,C...n
#axiom? 
#check it is subset of user input for alphabet
#for each letter, ask for an update string
#check that each symbol is a subset of symbol/alphabet set
#check there is at least one letter from alphabet in update string overall
#ask number of iterations
#check negative number, non-number etc
#ask angle of rotation
#don't do anything


#dictionary:
#ALPHABET: 
#UPDATE DICT - construct a string for each alphabet letter you have chosen, based on the Turtle pattern you wish to use (no need to replace with anything for these)
#+
#-
# [
# ] 

#for now assuming one letter F as alphabet
