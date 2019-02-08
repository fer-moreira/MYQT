import mysql.connector as mysql
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox

from assets.UI.Scripts.DB_Creator import Ui_Creator

class DBCreator(QMainWindow,Ui_Creator):
    def __init__(self,hs,pt,us,ps,bfr, parent = None):
        super(DBCreator,self).__init__(parent)
        self.setupUi(self)
        self.show()