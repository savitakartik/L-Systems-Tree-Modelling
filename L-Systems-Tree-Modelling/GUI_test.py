from PyQt5 import *
import unittest
import sys
from GUI import Window
from PyQt5.QtGui import *
from PyQt5.QtTest import *
from PyQt5.QtCore import *

class GUITest(unittest.TestCase):
    def test_defaults(self):
        self.assertEqual(self.frulebox.text(), '"F[+F]F[-F][F]"' )
        self.assertEqual(self.check1.isChecked(), True)
        self.assertEqual(self.numiterbox.value(), 5)
        self.assertEqual(self.anglespinbox.value(), 20)
        self.assertEqual(self.colourschemedd.text(), "natural")
        self.assertEqual(self.colourdistdd.text(), "sequential")
        self.assertEqual(self.ltslider.value(), 2)
