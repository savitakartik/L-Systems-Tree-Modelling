import unittest
from lsystem import LSystem

class LSystemTest(unittest.TestCase):
    """
    Tests the :class:`LSystem` class.
    """
    def test_addToDict(self):
        axiom='F'
        updateStr="FF-[-F+F+F]+[+F-F-F]"
        testLS = LSystem()
        assert testLS.addToDict(axiom, updateStr) == "FF-[-F+F+F]+[+F-F-F]"

