from PyQt5 import *
import unittest
import sys
from GUI import Window
from PyQt5.QtGui import *
from PyQt5.QtTest import *
from PyQt5.QtCore import *

class argsCheckerTest(unittest.TestCase):
    def test_defaults(self):
        self.assertEqual(self.form.ui.tequilaScrollBar.value(), 8 )
        self.assertEqual(self.form.ui.tripleSecSpinBox.value(), 4)
        self.assertEqual(self.form.ui.limeJuiceLineEdit.text(), "12.0")
        self.assertEqual(self.form.ui.iceHorizontalSlider.value(), 12)
        self.assertEqual(self.form.ui.speedButtonGroup.checkedButton().text(), "&Karate Chop")

        # Class is in the default state even without pressing OK
        self.assertEqual(self.form.getJiggers(), 36.0)
        self.assertEqual(self.form.getSpeedName(), "&Karate Chop")

        # Push OK with the left mouse button
        okWidget = self.form.ui.buttonBox.button(self.form.ui.buttonBox.Ok)
        QTest.mouseClick(okWidget, Qt.LeftButton)
        self.assertEqual(self.form.getJiggers(), 36.0)
        self.assertEqual(self.form.getSpeedName(), "&Karate Chop")