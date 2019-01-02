import sys
from PyQt5.QtCore import pyqtSlot,QFile, QTextStream
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow,QStyleFactory,QAction,QMenu
from PyQt5.uic import loadUi
from PyQt5 import QtGui

from Lib.UI.SCRIPT.ConnectorWindow import Ui_Connector

from Core.SQLManager import ManagerWindow

import mysql.connector as mysql

app = QApplication(sys.argv)
app.processEvents()

class MainWindow(QMainWindow,Ui_Connector):
    
    def __init__(self, parent = None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())        
        self.show()

        self.getdb_btn.clicked.connect(self.Get_Databases_to_combobox)

    def Get_Databases_to_combobox (self):
        print("GET_DATABASES")

        self._host = self.host_in.displayText()
        self._user = self.user_in.displayText()
        self._pass = self.pass_in.displayText()


        mydb = mysql.connect(
        host=self._host,
        user=self._user,passwd=self._pass
        )

        mycursor = mydb.cursor()
        mycursor.execute("show databases")

        myresult = mycursor.fetchall()

        items = []

        for x in myresult:
            items.append(str(x[0]))

        self.dbs.setEnabled(True)
        self.buffered.setEnabled(True)
        self.Connect_btn.setEnabled(True)

        self.dbs.addItems(items)

        self.Connect_btn.clicked.connect(self.Get_Database_to_manager)

    @pyqtSlot()
    def Get_Database_to_manager (self):
        self.buffered_c = self.buffered.isChecked()
        self.db = self.dbs.currentText()

        # print(self._host,self._user,self._pass,self.buffered_c,self.db)

        self.manager = ManagerWindow(self._host,self._user,self._pass,self.buffered_c,self.db)
    

Main_GUI = MainWindow()
sys.exit(app.exec_())