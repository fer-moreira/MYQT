from PyQt5.QtCore import pyqtSlot,QFile, QTextStream
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow,QStyleFactory,QAction,QMenu
from PyQt5.uic import loadUi
from PyQt5 import QtGui

from Lib.UI.SCRIPT.Console import Ui_Console

class ConsoleWindow(QMainWindow,Ui_Console):
    def __init__(self,text,parent = None):
        super(ConsoleWindow,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.show()

        self.console.setHtml(text)
