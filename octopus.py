import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import qDebug
from PyQt5.QtWidgets import QFileDialog

import mainwindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.startBtn.clicked.connect(self.advanceSlider)
        self.ui.fileLine.setEnabled(False)
        self.ui.fileOpen.clicked.connect(self.openFile)
        

    def advanceSlider(self):
        print('hello')
        self.ui.fileSpin.setValue(32)
        
    def openFile(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        self.ui.fileLine.setText(file)
        print(file)
        
        

app = QtWidgets.QApplication(sys.argv)

my_mainWindow = MainWindow()
my_mainWindow.show()

sys.exit(app.exec_())
