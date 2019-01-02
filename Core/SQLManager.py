import sys
from PyQt5.QtCore import pyqtSlot,QFile, QTextStream
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow,QStyleFactory,QAction,QMenu
from PyQt5.uic import loadUi
from PyQt5 import QtGui

from Lib.UI.SCRIPT.MainWindow import Ui_SQLMANAGER


class ManagerWindow(QMainWindow,Ui_SQLMANAGER,object):
    def __init__(self,hs,us,ps,bfr,db, parent = None):
        super(ManagerWindow,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())        
        self.show()

        self.hs = hs
        self.us = us
        self.ps = ps
        self.bfred = bfr
        self.db = db


        print(self.hs,self.us,self.ps,self.bfred,self.db)
