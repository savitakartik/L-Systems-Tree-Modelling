import sys
import unittest
from PyQt5 import *
import GUI
from GUI import Window
from PyQt5.QtGui import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)
class GUITest(unittest.TestCase):
    '''Test the margarita mixer GUI'''
    def setUp(self):
        '''Create the GUI'''
        self.form = GUI.Window()
        
    def test_defaults(self):
        self.assertEqual(self.form.frulebox.text(), "F[+F]F[-F][F]")
        self.assertEqual(self.form.check1.isChecked(), True)
        self.assertEqual(self.form.numiterbox.value(), 5)
        self.assertEqual(self.form.anglespinbox.value(), 20)
        self.assertEqual(self.form.colourschemedd.currentText(), "natural")
        self.assertEqual(self.form.colourdistdd.currentText(), "sequential")
        self.assertEqual(self.form.ltslider.value(), 2)

if __name__ == "__main__":
    unittest.main()