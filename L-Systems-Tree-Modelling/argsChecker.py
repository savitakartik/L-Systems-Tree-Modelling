from typing import ItemsView
import os


class argsChecker:
    """
    Class containing methods to validate user input. 
    A layer of validation is provided at GUI side, but this class contains methods to further check 
    arguments passed from GUI.
    ...
    Attributes
    ----------
    Methods
    ----------
        :__init__: constuctor.
        :checkIter(self, argIter): checks that iterations argument is a valid number.
        :checkAngle(self, argAngle): checks that the angle of rotation for the turtle step is a valid entry.
        :checkAxiom(self, argAxiom): checks that the axiom input is present in the dictionary of L-Systems alphabet.
        :checkUpdateStrLetters(self, argUpdateStr): checks that the update string contains only valid letters.
        :checkUpdateStrRecursion: checks that the update string is capable of recursion, ie, that it is extendable in further iterations.
    """
    def __init__(self) -> None:
        pass
    
    def checkIter(self, argIter):
        """
        checks that iterations argument is a valid number.
        :param self: class instance, defaults to self
        :param argIter: int, required, number of iterations
        :raises: exception, e
        """
        try:
            assert (type(argIter) == int and argIter > 0 and argIter <= 100), "Check iterations argument"
        except Exception as e:
            print (e)

    def checkAngle(self, argAngle):
        """
        checks that rotation angle is a valid number.
        :param self: class instance, defaults to self
        :param argAngle: int, required, rotation angle
        :raises: exception, e
        """
        try:
            assert (type(argAngle) == int and argAngle >= 0 and argAngle < 180), "Check angle argument"
        except Exception as e:
            print (e)

    def checkAxiom(self, argAxiom):
        """
        checks that the axiom is present in the dictionary.
        :param self: class instance, defaults to self
        :param argAxiom: string, required, axiom letter
        :raises: exception, e
        """
        try:
            letterSet=['F']
            assert (type(argAxiom) == str and len(argAxiom) == 1 and argAxiom in letterSet), "Check axiom argument"
        except Exception as e:
            print (e)
    
    def checkUpdateStrLetters(self, argUpdateStr):
        """
        checks that the update string symbols are each present in the dictionary.
        :param self: class instance, defaults to self
        :param argupdateStr: string, update string
        :raises: exception, e
        """
        charSet=['F','+','-','[',']']
        try:
            for char in argUpdateStr:
                assert (char in charSet), "Please check your update string!"
                break

        except Exception as e:
            print (e)

    def checkUpdateStrRecursion(self, argUpdateStr):
        """
        checks that the update string is capable of extension.
        :param self: class instance, defaults to self
        :param argupdateStr: string, update string
        :raises: exception, e
        """
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