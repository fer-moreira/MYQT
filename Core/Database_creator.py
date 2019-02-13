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

        self.hs = hs        #HOST
        self.pt = pt        #PORTA
        self.us = us        #USUARIO
        self.ps = ps        #PASSWORD
        self.bfred = bfr    #BUFFERED

        self.mydb = mysql.connect(host=self.hs,port=self.pt,user=self.us,passwd=self.ps,buffered=self.bfred)

        self.get_all_database()

        # self.deleteBtn.clicked.connect(self.delete_selected_database())


    def get_all_database (self):
        self.databases.clear()

        cursor = self.mydb.cursor()
        cursor.execute("SHOW databases")
        _result = cursor.fetchall()

        for db in _result:
            _item = db[0]
            self.databases.addItem(_item)

    # def delete_selected_database (self):
    #     _selectedItem = self.databases.currentItem()
    #     print(_selectedItem)