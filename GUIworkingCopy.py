from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QMainWindow, QGridLayout, QMessageBox, QPushButton, QCheckBox, QInputDialog
from PyQt5.QtCore import Qt
import sys

class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.btn()
        self.btn2()
        self.label()
        self.checks()
        self.grid_layout()
        

    def check_state(self):
        if self.check1.isChecked():
            print(self.check1.text())
        if self.check2.isChecked():
            print(self.check2.text())
        if self.check3.isChecked():
            print(self.check3.text())
        if self.check4.isChecked():
            print(self.check4.text())

    def popUp(self):
        text, ok = QInputDialog.getText(self, 'String generation', 'Enter update rule')

    def btn(self):
        btn = QPushButton('Dictionary', self)
        btn.move(370,80)
        btn.clicked.connect(self.dictionary)

    def btn2(self):
        btn = QPushButton('Submit', self)
        btn.move(10,180)
        btn.clicked.connect(self.check_state)
        btn.clicked.connect(self.popUp)

    def label(self):
        label = QLabel(self)
        label.setText("Used symbols:")
        label.move(10,80)

    def dictionary(self):
        mbox = QMessageBox(self)
        mbox.setText("Available symbols: F,  +,  -,  [ ]")
        mbox.setDetailedText("Description of symbols meanings")
        mbox.setStandardButtons(QMessageBox.Ok)
                
        mbox.exec_()

    def checks(self):
        self.check1=QCheckBox('F')
        self.check2=QCheckBox('+')
        self.check3=QCheckBox('-')
        self.check4=QCheckBox('[ ]')

    def grid_layout(self):
        grid = QGridLayout(self)
        grid.addWidget(self.check1, 10, 50)
        grid.addWidget(self.check2, 10, 70)
        grid.addWidget(self.check3, 10, 90)
        grid.addWidget(self.check4, 10, 110)
        self.setLayout(grid)


def main ():

    app = QApplication(sys.argv)
    widget=MainWidget()
    widget.resize(500,300)
    widget.setWindowTitle('L-systems')
    widget.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

