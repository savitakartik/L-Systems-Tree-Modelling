import unittest
from lsystem import LSystem

class LSystemTest(unittest.TestCase):
    """
    Tests the :class:`argsChecker` class.
    """
    def test_addToDict(self):
        axiom='F'
        updateStr="FF-[-F+F+F]+[+F-F-F]"
        testLS = LSystem()
        testLS.addToDict(axiom, updateStr)
        assert testLS[axiom] == "FF-[-F+F+F]+[+F-F-F]"


    # def test_checkAngle(self):

    #     with self.assertRaises(TypeError):
    #         argsChecker.checkAngle(-45)

    # def test_checkAxiom(self):

    #     with self.assertRaises(TypeError):
    #         argsChecker.checkAxiom('1')
    
    # def test_checkUpdateStrLetters(self):

    #     with self.assertRaises(TypeError):
    #         argsChecker.checkUpdateStrLetters("?")
    
    # def test_checkUpdateStrRecursion(self):

    #     with self.assertRaises(TypeError):
    #         argsChecker.checkUpdateStrRecursion(123)


