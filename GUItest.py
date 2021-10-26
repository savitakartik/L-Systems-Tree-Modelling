
# pop up message after button was clicked
""" 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
app = QApplication([])
app.setStyleSheet("QPushButton { margin: 5ex; }")
app.setStyle('Fusion')
palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.blue)
app.setPalette(palette)
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))

button=QPushButton('Click')
def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec()

button.clicked.connect(on_button_clicked)
layout.addWidget(button)
window.setLayout(layout)
window.show()
app.exec() """


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout
from PyQt5.QtCore import Qt
import sys
 
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(400,400,500,300)
    win.setWindowTitle("L-System Configuration")

    # display multiple checkboxes and retrieve state
    def show():
        print(check.text())
        print(check.checkState())
        
    def show2():
        print(check2.text())
        print(check2.checkState())

    layout = QGridLayout()
 
    check = QtWidgets.QCheckBox(win)
    check.setText("EdgeReplacement")
    check.stateChanged.connect(show)
    check.move(50,100)
    layout.addWidget(check, 0, 0)
    
    check2 = QtWidgets.QCheckBox(win)
    check2.setText("NodeReplacement")
    check2.stateChanged.connect(show2)
    check2.move(50,150)
    layout.addWidget(check2, 0, 1)

    # provide a drop-down menu and submit button that outputs user selection
    def show3():
        result = combo.currentText()
        print(result)

    combo = QtWidgets.QComboBox(win)
    combo.addItems(["F","+","-"])
    combo.move(200,100)

    button = QtWidgets.QPushButton(win)
    button.setText("Submit")
    button.clicked.connect(show3)
    button.move(200,125)

    # provide a line for user input and print string in terminal
    def show4():
        print(line.text())

    line = QtWidgets.QLineEdit(win)
    line.setFixedWidth(140)
    line.move(50,50)
    
    button = QtWidgets.QPushButton(win)
    button.setText("Submit")
    button.clicked.connect(show4)
    button.move(200,40)
    
    button = QtWidgets.QPushButton(win)
    button.setText("Clear")
    button.clicked.connect(line.clear)
    button.move(200,65)

    # provide a slider for the choice of different values between certain numbers
    """ def display():
     my_label.setText(str(slider.value()))

    slider = QtWidgets.QSlider(win)
    slider.setGeometry(300,50, 200, 50)
    slider.setMinimum(1)
    slider.setMaximum(5)
    slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
    slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
    slider.setTickInterval(2)
    slider.valueChanged.connect(display)
    
    my_label = QtWidgets.QLabel(win)
    my_label.move(300, 300) """

    win.show()
    sys.exit(app.exec_())
     
window() 
