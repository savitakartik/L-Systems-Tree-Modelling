import unittest
from argsChecker import argsChecker

class argsCheckerTest(unittest.TestCase):
    """
    Tests the :class:`argsChecker` class.
    """
    def test_check_iter(self):

        with self.assertRaises(TypeError):
            argsChecker.checkIter(0)

    def test_checkAngle(self):

        with self.assertRaises(TypeError):
            argsChecker.checkAngle(-45)

    def test_checkAxiom(self):

        with self.assertRaises(TypeError):
            argsChecker.checkAxiom('1')
    
    def test_checkUpdateStrLetters(self):

        with self.assertRaises(TypeError):
            argsChecker.checkUpdateStrLetters("?")
    
    def test_checkUpdateStrRecursion(self):

        with self.assertRaises(TypeError):
            argsChecker.checkUpdateStrRecursion(123)



