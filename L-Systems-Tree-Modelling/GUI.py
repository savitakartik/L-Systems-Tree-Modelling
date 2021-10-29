from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import lsystem as LS
import argsChecker as val
from Turtle2D_interpretation import *
import cv2
import numpy as np
from re import search


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.makeGUI()

    def makeGUI(self):
        self.setWindowTitle('L-Systems Tree Modeller')
        # set layouts for widgets and groups
        layoutLS1 = QVBoxLayout()
        layoutLS = QVBoxLayout()
        layoutTree = QVBoxLayout()
        layoutGo = QVBoxLayout()
        parentLayout = QHBoxLayout()
        parentLayout.addLayout(layoutLS)
        horizontalSpacer1 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        horizontalSpacer2 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        verticalSpacer1 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        parentLayout.addItem(horizontalSpacer1)
        parentLayout.addLayout(layoutTree)
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(parentLayout)
        mainLayout.addLayout(layoutGo)
        # add widgets...
        # ...for L-system parameters

        # layoutLS.addItem(verticalSpacer1)
        imgLabel = QLabel(self)
        pixmap = QPixmap('L-Systems-Tree-Modelling/tree.jpg')
        imgLabel.setPixmap(pixmap)
        imgLabel.setMaximumSize(150, 50)
        layoutLS.addWidget(imgLabel)

        self.labelLSTitle = QLabel("L-System parameters")
        myFont = QFont()
        myFont.setBold(True)
        self.labelLSTitle.setFont(myFont)
        layoutLS.addWidget(self.labelLSTitle)
        # F check box - disabled as there is only one option which is mandatory at the moment
        self.label1 = QLabel('Axiom and constants:')
        #self.label1.setStyleSheet("border: 1px solid black;")
        layoutLS.addWidget(self.label1)
        self.check1 = QCheckBox('F')
        self.check1.setChecked(True)
        self.check1.setDisabled(True)
        layoutLS.addWidget(self.check1)

        # update-string text box for axiom
        layoutLS.addWidget(QLabel('Update string:'))
        self.frulebox = QLineEdit(self, placeholderText="example: F[+F]F[-F]F")
        self.frulebox.setText("F[+F]F[-F]F")
        # Add validator to check if characters are in dictionary and that axiom is present at least once.
        regexPattern = QRegExp("^[F\[\]\+\-]*[F]+[F\[\]\+\-]*$")
        validator = QRegExpValidator(regexPattern)
        self.frulebox.setValidator(validator)
        layoutLS.addWidget(self.frulebox)

        # X check box
        self.check4 = QCheckBox('X (Future implementation)')
        self.check4.setChecked(False)
        self.check4.setDisabled(True)
        layoutLS.addWidget(self.check4)
        layoutLS.addWidget(QLabel('Update string:'))
        self.xrulebox = QLineEdit(
            self, placeholderText="Future implementation")
        self.xrulebox.setDisabled(True)
        validator = QRegExpValidator(regexPattern)
        self.xrulebox.setValidator(validator)
        layoutLS.addWidget(self.xrulebox)

        # + check box and text box for + update string
        #self.check2=QCheckBox('+')
        #layoutLS.addWidget(self.check2)
        #layoutLS.addWidget(QLabel('Update string:'))
        #self.plusrulebox = QLineEdit(self, placeholderText="+")
        #self.plusrulebox.setText("+")
        #self.plusrulebox.setDisabled(True)
        #validator=QRegExpValidator(regexPattern)
        #self.plusrulebox.setValidator(validator)
        #layoutLS.addWidget(self.plusrulebox)
        #self.check2.toggled.connect(self.plusrulebox.setEnabled)

        # - checkbox and text box for - update rule
        #self.check3=QCheckBox('-')
        #layoutLS.addWidget(self.check3)
        #layoutLS.addWidget(QLabel('Enter update string for:'))
        #self.minusrulebox = QLineEdit(self, placeholderText="example: -")
        #self.minusrulebox.setText("-")
        #self.minusrulebox.setDisabled(True)
        #validator=QRegExpValidator(regexPattern)
        #self.minusrulebox.setValidator(validator)
        #layoutLS.addWidget(self.minusrulebox)
        #self.check3.toggled.connect(self.minusrulebox.setEnabled)

        # Dictionary dialog
        btn = QPushButton('Dictionary', self)
        btn.move(370, 80)
        btn.clicked.connect(self.dictionary)
        layoutLS.addWidget(btn)

        # text box for number of iterations
        layoutLS.addWidget(QLabel('Number of iterations:'))
        self.numiterbox = QSpinBox()
        self.numiterbox.setRange(1, 10)
        self.numiterbox.setValue(4)
        layoutLS.addWidget(self.numiterbox)

        layoutLS.addItem(verticalSpacer1)

        # ...for tree parameters
        # text box for angle
        self.labelTreeTitle = QLabel("Tree parameters")
        myFont = QFont()
        myFont.setBold(True)
        self.labelTreeTitle.setFont(myFont)
        layoutTree.addWidget(self.labelTreeTitle)
        layoutTree.addWidget(QLabel('Angle of rotation (delta, in deg):'))
        # TODO: accept floating values
        self.anglespinbox = QSpinBox()
        self.anglespinbox.setRange(0, 179)
        self.anglespinbox.setValue(22)
        layoutTree.addWidget(self.anglespinbox)

        # drop-down for colour scheme
        layoutTree.addWidget(QLabel('Colour scheme:'))
        self.colourschemedd = QComboBox(self)
        self.colourschemedd.addItem("natural")
        self.colourschemedd.addItem("rainbow")
        layoutTree.addWidget(self.colourschemedd)

        # drop-down for colour distribution
        layoutTree.addWidget(QLabel('Colour distribution:'))
        self.colourdistdd = QComboBox(self)
        self.colourdistdd.addItem("sequential")
        self.colourdistdd.addItem("random")
        layoutTree.addWidget(self.colourdistdd)

        # slider for line thickness
        layoutTree.addWidget(QLabel('Line thickness:'))
        self.ltslider = QSlider(Qt.Horizontal)
        self.ltslider.setRange(1, 10)
        self.ltslider.setValue(5)
        self.ltslider.setTickPosition(QSlider.TicksBelow)
        self.ltslider.setTickInterval(5)
        self.ltslider.valueChanged.connect(self.updateltSliderLabel)
        self.ltsliderabel = QLabel('5', self)
        layoutTree.addWidget(self.ltsliderabel)
        self.ltsliderabel.setMinimumWidth(80)
        layoutTree.addWidget(self.ltslider)

        # slider for step size
        layoutTree.addWidget(QLabel('Turtle step size:'))
        self.ssslider = QSlider(Qt.Horizontal)
        self.ssslider.setRange(1, 10)
        self.ssslider.setValue(5)
        self.ssslider.setTickPosition(QSlider.TicksBelow)
        self.ssslider.setTickInterval(5)
        self.ssslider.valueChanged.connect(self.updatessSliderLabel)
        self.sssliderabel = QLabel('5', self)
        layoutTree.addWidget(self.sssliderabel)
        self.sssliderabel.setMinimumWidth(80)
        layoutTree.addWidget(self.ssslider)

        # slider for screensize
        layoutTree.addWidget(QLabel('Plot dimensions (square):'))
        self.scrsizeslider = QSlider(Qt.Horizontal)
        self.scrsizeslider.setRange(100, 1000)
        self.scrsizeslider.setValue(500)
        self.scrsizeslider.setTickPosition(QSlider.TicksBelow)
        self.scrsizeslider.setTickInterval(100)
        self.scrsizeslider.valueChanged.connect(self.updatescrsizeSliderLabel)
        self.scrsizesliderlabel = QLabel('500', self)
        #self.label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        layoutTree.addWidget(self.scrsizesliderlabel)
        self.scrsizesliderlabel.setMinimumWidth(80)
        layoutTree.addWidget(self.scrsizeslider)

        # option to use default values
        #self.check5=QCheckBox('Use default values')
        # layoutGo.addWidget(self.check5)

        # go button
        self.gobtn = QPushButton('Go!')
        self.gobtn.setToolTip('Click to generate the tree.')
        layoutGo.addWidget(self.gobtn)
        self.gobtn.clicked.connect(self.ongobtnClick)

        # layoutGo.addItem(verticalSpacer1)

        # set layout on application window
        self.setLayout(mainLayout)

    def dictionary(self):
        mbox = QMessageBox(self)
        mbox.setWindowTitle("Dictionary")
        mbox.setText("Available symbols: F,  +,  -,  [ ]")
        mbox.setDetailedText(
            "Dictionary symbols\n F:   a constant letter\n +:  move left by delta degrees\n+:  move right by delta degrees\n []:  no action; denote branch start and end")
        mbox.setStandardButtons(QMessageBox.Ok)
        mbox.exec_()

    def updateltSliderLabel(self, value):
        self.ltsliderabel.setText(str(value))

    def updatessSliderLabel(self, value):
        self.sssliderabel.setText(str(value))

    def updatescrsizeSliderLabel(self, value):
        self.scrsizesliderlabel.setText(str(value))

    @pyqtSlot()
    def ongobtnClick(self):
        axiom = 'F'
        frule = self.frulebox.text()
        niter = self.numiterbox.value()
        rotation = self.anglespinbox.value()
        colourscheme = self.colourschemedd.currentText()
        colourdist = self.colourdistdd.currentText()
        thickness = self.ltslider.value()
        stepsize = self.ssslider.value()
        scrsize = self.scrsizeslider.value()

        # call wrapper.py
        print(axiom, frule, niter, rotation, colourscheme,
              colourdist, thickness, stepsize, scrsize)

        # TODO: implement dialog error if update string contains a letter ind ictionary that is not selected in the checkbox first.
        #f((not self.check2.isChecked) and (search('+',self.frulebox.text) or search('+',self.xrulebox.text) or search('+',self.minusrulebox.text) )):
        #if (self.check2.isChecked() == False and (search('+',self.frulebox.text) or search('+',self.xrulebox.text) or search('+',self.minusrulebox.text) )):
        #    msg = QMessageBox()
        #    msg.setIcon(QMessageBox.Critical)
        #    msg.setText("Error")
        #    msg.setInformativeText('Pleae check your update string: cannot contain '+' unless selected as a constant.')
        #    msg.setWindowTitle("Error")
        #    msg.exec_()

        #else:
        # connect to LSystem code
        myChecker = val.argsChecker()
        # TODO change argChecker to check for float
        myChecker.checkAngle(int(rotation))
        myChecker.checkIter(int(niter))
        myChecker.checkUpdateStrLetters(frule)
        myChecker.checkUpdateStrRecursion(frule)
        myLS = LS.LSystem()
        # add update string to dictionary
        for char in frule:
            myLS.addToDict(char, char)
        myLS.addToDict(axiom, frule)
        # build treeSeq
        treeSeq = myLS.makeLSystem(int(niter), axiom)
        # print(treeSeq)

        # call turtle interpretation: input-string, output-write to jpg
        # turtle=Turtle2D(p0=np.array([500,0]),o0=np.array([0,1]),std_d=10,std_delta=22.5)
        turtle = Turtle2D(p0=np.array([scrsize/2, 0]), o0=np.array(
            [0, 1]), std_d=stepsize, std_delta=rotation, color_scheme=colourscheme, color_type=colourdist)
        next_position = turtle.next_position()
        drawer = Tree_drawing_2D(turtle, (scrsize, scrsize))
        drawer.draw_tree(treeSeq)
        drawer.show_tree()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    # housekeeping statement for clean exit from program once GUI app is closed.
    sys.exit(app.exec_())
