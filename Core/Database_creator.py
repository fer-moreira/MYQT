import mysql.connector as mysql
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox

from assets.UI.Scripts.DB_Creator import Ui_Creator

class DBCreator(QMainWindow,Ui_Creator):
    def __init__(self,hs,pt,us,ps,bfr,manager_window, parent = None):
        super(DBCreator,self).__init__(parent)
        self.setupUi(self)
        self.show()

        self.hs = hs        #HOST
        self.pt = pt        #PORTA
        self.us = us        #USUARIO
        self.ps = ps        #PASSWORD
        self.bfred = bfr    #BUFFERED
        self.manager = manager_window

        self.mydb = mysql.connect(host=self.hs,port=self.pt,user=self.us,passwd=self.ps,buffered=self.bfred)

        self.refresh_databases()

        self.deleteBtn.clicked.connect(self.delete_selected_database)
        self.createBtn.clicked.connect(self.create_new_database)

    def refresh_databases (self):
        self.databases.clear()

        cursor = self.mydb.cursor()
        cursor.execute("SHOW databases")
        _result = cursor.fetchall()

        for db in _result:
            _item = db[0]
            self.databases.addItem(_item)

        self.manager.refresh_database()

    def create_new_database (self):
        _db_name = str(self.db_name.displayText())
        add_query = "CREATE DATABASE {}".format(_db_name)
        cursor = self.mydb.cursor()
        cursor.execute(add_query)
        self.refresh_databases()
        

    def delete_selected_database (self):
        try:
            selected_item  = str([item.text() for item in self.databases.selectedItems()][0])
            del_query = "drop database {}".format(selected_item)
            cursor = self.mydb.cursor()
            cursor.execute(del_query)
            self.refresh_databases()
        except Exception as error:
            print(error)
