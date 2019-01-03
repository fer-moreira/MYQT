from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot,QFile, QTextStream,QCoreApplication
from PyQt5.uic import loadUi

from PyQt5.QtWidgets import QApplication, QDialog,QFileDialog,QMainWindow,QStyleFactory
from PyQt5.QtWidgets import QAction,QMenu,QTableWidget,QTableWidgetItem,QTableView

from PyQt5.QtGui import QStandardItemModel,QStandardItem

from PyQt5 import QtGui


from Lib.UI.SCRIPT.MainWindow import Ui_SQLMANAGER
import mysql.connector as mysql

import time
import sys

class ManagerWindow(QMainWindow,QCoreApplication,Ui_SQLMANAGER,object):
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


        self.reftable_btn.clicked.connect(self.Get_Tables)        
        self.Get_Tables()

        self.compile_btn.clicked.connect(self.Execute_Querry)
        self.import_btn.clicked.connect(self.load_query_from_file)

    def Execute_Querry (self):
        _query = str(self.query_in.toPlainText()).replace("\n"," ")

        try:
            cursor = self.mydb.cursor()
            cursor.execute(_query)

            allSQLRows = cursor.fetchall()

            
            lenRow = len(allSQLRows)
            lenCol = len(allSQLRows[0])

            self.result_out.setRowCount(lenRow) ##set number of rows
            self.result_out.setColumnCount(lenCol) ##this is fixed for result_out, ensure that both of your tables, sql and qtablewidged have the same number of columns


            if allSQLRows is not None:
                for lin in range(0,lenRow):
                    for col in range(0,lenCol):
                        data = QTableWidgetItem(str(allSQLRows[lin][col]))
                        self.result_out.setItem(lin,col,data)


            columns = cursor.description
            header_names = []
            for col in range(0,lenCol):
                print(columns[col][0])
                header_names.append(columns[col][0])

            self.processEvents()
            self.tabs.setCurrentIndex(0)


        except Exception as error:
            self.WriteConsole(error)
            pass

    def Get_Tables (self):
        try:
            self.mydb = mysql.connect(
                host=self.hs,
                user=self.us,
                passwd=self.ps,
                buffered=self.bfred,
                database=self.db
            )

            self.mycursor = self.mydb.cursor()
            self.mycursor.execute("show tables")
            self.myresult = self.mycursor.fetchall()

            tables = []

            for x in self.myresult:
                tables.append(x[0])

            self.tables_out.clear()
            self.tables_out.addItems(tables)            
            self.tabs.setCurrentIndex(0)

        except Exception as error:
            self.WriteConsole(error)
            pass
    def WriteConsole (self,text):
        now = "{0} {1:<20}".format(time.strftime("%x"),time.strftime("%X"))
        self.console_out.insertPlainText(str("{0} ERROR:{1}\n".format(now,text)))
        self.tabs.setCurrentIndex(1)

        print(text)
    def load_query_from_file(self):  
        fname = QFileDialog.getOpenFileName(self, 'Open QUERY file', 'c:\\',"Select query file (*.txt *.sql *.dat *.csv *.tsv *.psv)")        
        selectFilePath = str(fname[0])

        fileopen = open(r'%s'%selectFilePath,'r')
        _content = str(fileopen.read())

        self.query_in.setText(_content)
