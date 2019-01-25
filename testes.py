from PyQt5.QtCore import pyqtSlot,QFile, QTextStream
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow,QStyleFactory,QAction,QMenu
from PyQt5.uic import loadUi
from PyQt5 import QtGui

from Lib.UI.SCRIPT.Testes import Ui_Testes

import sys

app = QApplication(sys.argv)
app.processEvents()

class MainWindow(QMainWindow,Ui_Testes):
    def __init__(self, parent = None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.show()

Main_GUI = MainWindow()
sys.exit(app.exec_())