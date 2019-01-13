from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot,QFile, QTextStream,QCoreApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog,QFileDialog,QMainWindow,QStyleFactory,QAction,QMenuBar,QAction,QMenu,QTableWidget,QTableWidgetItem

import time
import sys
import mysql.connector as mysql

from Lib.UI.SCRIPT.MainWindow import Ui_SQLMANAGER

class ManagerWindow(QMainWindow,QCoreApplication,Ui_SQLMANAGER,object):
    def __init__(self,hs,us,ps,bfr,db, parent = None):
        super(ManagerWindow,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.add_menu_bar()
        self.show()

        self.hs = hs
        self.us = us
        self.ps = ps
        self.bfred = bfr
        self.db = db

        self.mydb = mysql.connect(host=self.hs,user=self.us,passwd=self.ps,buffered=self.bfred,database=self.db)

        self.Get_Tables()

    def Get_Tables (self):
        try:
            self.mycursor = self.mydb.cursor()
            self.mycursor.execute("show tables")
            self.myresult = self.mycursor.fetchall()

            tables = []

            for x in self.myresult:
                tables.append(x[0])

            self.tables_out.clear()
            self.tables_out.addItems(tables)

        except Exception as error:
            self.WriteConsole(error)
            pass

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
            for col in range(0,lenCol):
                headerName = QTableWidgetItem(columns[col][0])
                self.result_out.setHorizontalHeaderItem(col, headerName)

            self.processEvents()

        except Exception as error:
            self.WriteConsole(error)
            pass


    def WriteConsole (self,text):
        error = "{0} {1:<10} :::   {2}\n".format(time.strftime("%x"),time.strftime("%X"),text)
        self.console_out.insertPlainText(error)
        print(error)


    def load_query_from_file(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open QUERY file', 'c:\\',"Select query file (*.txt *.sql *.dat *.csv *.tsv *.psv)")
            selectFilePath = str(fname[0])

            fileopen = open(r'%s'%selectFilePath,'r')
            _content = str(fileopen.read())

            self.query_in.setText(_content)
        except FileNotFoundError:pass

    def add_menu_bar (self):
        mainMenu = self.menuBar()

        importQuery = QAction("&Import Query", self)
        importQuery.setShortcut("Ctrl+W")
        importQuery.triggered.connect(self.load_query_from_file)

        exportQuery = QAction("&Export Query",self)
        exportQuery.setShortcut("Ctrl+S")
        
        compileQuery = QAction("&Compile Query",self)
        compileQuery.setShortcut("F5")
        compileQuery.triggered.connect(self.Execute_Querry)

        selectedQuery = QAction("&Compile Selected Query",self)
        selectedQuery.setShortcut("F6")
        compileQuery.triggered.connect(self.Execute_Querry)

        refreshTables = QAction("&Refresh Tables",self)
        refreshTables.setShortcut("Ctrl+R")
        refreshTables.triggered.connect(self.Get_Tables)

        _file = mainMenu.addMenu('&File')
        _file.addAction(importQuery)
        _file.addAction(exportQuery)
        _file.addAction(compileQuery)
        _file.addAction(selectedQuery)
        _file.addAction(refreshTables)
