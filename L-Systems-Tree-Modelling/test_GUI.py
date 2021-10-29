import unittest
from PyQt5 import *
import sys
import GUI
from GUI import Window
from PyQt5.QtTest import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

class GUITest(unittest.TestCase):
    def setUp(self):
        self.form = GUI.Window()

    def test_defaults(self):
        self.assertEqual(self.form.frulebox.text(), 'F[+F]F[-F][F]' )
        self.assertEqual(self.form.check1.isChecked(), True)
        self.assertEqual(self.form.numiterbox.value(), 5)
        self.assertEqual(self.form.anglespinbox.value(), 20)
        self.assertEqual(self.form.colourschemedd.currentText(), "natural")
        self.assertEqual(self.form.colourdistdd.currentText(), "sequential")
        self.assertEqual(self.form.ltslider.value(), 2)
        self.assertEqual(self.form.lrslider.value(), 3)
        self.assertEqual(self.form.ssslider.value(), 5)
        self.assertEqual(self.form.scrsizeslider.value(), 350)

if __name__=="__main__":
    unittest.main()
