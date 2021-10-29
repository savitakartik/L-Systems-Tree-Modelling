import unittest
from PyQt5 import *
import sys
from GUI import Window
from PyQt5.QtGui import QApplication
from PyQt5.QtTest import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class GUITest(unittest.TestCase):
    def test_defaults(self):
        app = QApplication(sys.argv)
        window = Window()
        window.show()
        self.assertEqual(window.frulebox.text(), '"F[+F]F[-F][F]"' )
        self.assertEqual(window.check1.isChecked(), True)
        self.assertEqual(window.numiterbox.value(), 5)
        self.assertEqual(window.anglespinbox.value(), 20)
        self.assertEqual(window.colourschemedd.text(), "natural")
        self.assertEqual(window.colourdistdd.text(), "sequential")
        self.assertEqual(window.ltslider.value(), 2)
        sys.exit(app.exec_())
