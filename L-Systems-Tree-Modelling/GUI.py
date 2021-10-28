from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import lsystem as LS
import argsChecker as val
#import turtle_test as tt
#import Turtle2D_interpretation as ti

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.makeGUI()

    def makeGUI(self):
        self.setWindowTitle('Tree Window')
        # set a vertical layout
        layout = QVBoxLayout()
        # add widgets...
        # ...for L-system parameters
        #layout.addWidget(QLabel('Axiom=F'))

        # TODO: set scaling for widgets
        # TODO: change drop-down to textbox with validation for characters in dictionary, and F mandatory.
        layout.addWidget(QLabel('Choose update strings:'))
        #self.updatedd = QComboBox(self)
        # updatedd.move(20,20)
        #self.updatedd.addItem("F[+F]F[-F]F")
        #self.updatedd.addItem("F[+F]F[-F][F]")
        #self.updatedd.addItem("FF-[-F+F+F]+[+F-F-F]")
        #layout.addWidget(self.updatedd)

        #VIKI added this:
        self.check1=QCheckBox('F')
        self.check2=QCheckBox('+')
        self.check3=QCheckBox('-')

        layout.addWidget(self.check1)
        layout.addWidget(QLabel('Enter update string for F :'))
        self.frulebox = QLineEdit(self)
        #self.frulebox.setValidator(QIntValidator())
        layout.addWidget(self.frulebox)

        layout.addWidget(self.check2)
        layout.addWidget(QLabel('Enter update string for + :'))
        self.plusrulebox = QLineEdit(self)
        #self.plusrulebox.setValidator(QIntValidator())
        layout.addWidget(self.plusrulebox)

        layout.addWidget(self.check3)
        layout.addWidget(QLabel('Enter update string for - :'))
        self.minusrulebox = QLineEdit(self)
        #self.minusrulebox.setValidator(QIntValidator())
        layout.addWidget(self.minusrulebox)

        btn = QPushButton('Dictionary', self)
        btn.move(370,80)
        btn.clicked.connect(self.dictionary)
        layout.addWidget(btn)

        #VIKIs changes end here

        layout.addWidget(QLabel('Enter number of iterations:'))
        self.numiterbox = QLineEdit(self)
        self.numiterbox.setValidator(QIntValidator())
        # TODO: add check for num below 100?
        layout.addWidget(self.numiterbox)

        # ...for tree parameters
        layout.addWidget(QLabel('Enter angle of rotation:'))
        self.anglebox = QLineEdit(self)
        # TODO: add check for angle between 0 and 360
        self.anglebox.setValidator(QIntValidator())
        layout.addWidget(self.anglebox)

        layout.addWidget(QLabel('Choose colour scheme:'))
        self.colourdd = QComboBox(self)
        self.colourdd.addItem("random")
        self.colourdd.addItem("brown-green")
        layout.addWidget(self.colourdd)

        self.gobtn = QPushButton('Go!')
        self.gobtn.setToolTip('Click to generate the tree.')
        layout.addWidget(self.gobtn)

        self.gobtn.clicked.connect(self.onClick)

        # set layout on application window
        self.setLayout(layout)
        
    #VIKI added this
    def dictionary(self):
            mbox = QMessageBox(self)
            mbox.setText("Available symbols: F,  +,  -,  [ ]")
            mbox.setDetailedText("Description of symbols meanings")
            mbox.setStandardButtons(QMessageBox.Ok)
                    
            mbox.exec_()
    #VIKIs changes end here

    @pyqtSlot()
    def onClick(self):
        numiterboxVal = self.numiterbox.text()
        angleboxVal = self.anglebox.text()
        colourddVal = self.colourdd.currentText()
        updateddVal = self.updatedd.currentText()

        # collect values from input boxes
        # call wrapper.py
        print(numiterboxVal, angleboxVal, colourddVal, updateddVal)

        #connect to LSystem code
        myChecker=val.argsChecker()
        #TODO change argChecker to check for float
        #TODO change textbox validation to include float
        myChecker.checkAngle(int(angleboxVal))
        myChecker.checkIter(int(numiterboxVal))
        myChecker.checkUpdateStrLetters(updateddVal)
        myChecker.checkUpdateStrRecursion(updateddVal)

        #creat L-systems obj
        myLS = LS.LSystem()

        #for updateStr, if valid, add each char-> updateStr to Dict
        for char in updateddVal:
            myLS.addToDict(char, char)
        myLS.addToDict('F', updateddVal)
        #build treeSeq
        treeSeq=myLS.makeLSystem(int(numiterboxVal), 'F')

        print(treeSeq)
        #call turtle interpretation: input-string, output-write to jpg
        #label = QLabel(self)
        #pixmap = QPixmap('tree.jpg')
        #label.setPixmap(pixmap)
        #self.setCentralWidget(label)
        #self.resize(pixmap.width(), pixmap.height())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    # set the window position and dimensions: 200 pi right, then 200 pi below from the top-left corner, 1000 pi wide and 500 pi tall
    # win.setGeometry(200,200,1000,500)
    # show window
    win.show()
    # housekeeping statement for clean exit from program once GUI app is closed.
    sys.exit(app.exec_())
