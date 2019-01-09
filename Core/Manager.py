from PyQt5 import QtCore
from PyQt5.uic import loadUi

from PyQt5 import QtGui
from PyQt5.QtGui import QStandardItemModel,QStandardItem

from PyQt5.QtWidgets import QApplication, QDialog,QFileDialog,QMainWindow,QStyleFactory
from PyQt5.QtWidgets import QAction,QToolBar,QTableWidget,QTableWidgetItem

from PyQt5.QtCore import pyqtSlot,QFile, QTextStream,QCoreApplication

from PyQt5.QtGui import QIcon

import time
import sys
import mysql.connector as mysql
from functools import partial

from Lib.UI.SCRIPT.MainWindow import Ui_SQLMANAGER


class ManagerWindow(QMainWindow,QCoreApplication,Ui_SQLMANAGER,object):
    def __init__(self,hs,us,ps,bfr,db, parent = None):
        super(ManagerWindow,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.add_tool_bar()
        self.show()

        self.hs = hs
        self.us = us
        self.ps = ps
        self.bfred = bfr
        self.db = db

        try:
            self.mydb = mysql.connect(host=self.hs,user=self.us,passwd=self.ps,
                                  buffered=self.bfred,database=self.db)
        except:
            self.WriteConsole("Cannot Connect to SQL Server",True)

        
        self.Get_Tables() 
        self.tables_out.itemSelectionChanged.connect(self.Get_Desc)
        self.tables_out.itemSelectionChanged.connect(self.Get_All_Data)


    def Execute_Querry (self,text):
        _query = text

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
            self.console_out.setPlainText("")

            self.WriteConsole("Query OK!",False)

        except Exception as error:
            self.WriteConsole(error,True)
            pass

    def GetAllQuery (self):
        _allQuery = str(self.query_in.toPlainText()).replace("\n"," ")
        self.Execute_Querry(_allQuery)
    
    def GetSelectedQuery (self):
        cursor = self.query_in.textCursor()
        
        _allText = str(self.query_in.toPlainText()).replace("\n"," ")
        _startIndex = cursor.selectionStart()
        _endIndex = cursor.selectionEnd()
        
        _buildText = ""

        for letter in range(_startIndex,_endIndex):
            _buildText+=_allText[letter]

        self.Execute_Querry(_buildText)

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
            self.WriteConsole(error,True)
            pass
    
    def Get_Desc (self):
        table = self.tables_out.currentItem().text()
        _query = "desc %s"%table

        try:
            cursor = self.mydb.cursor()
            cursor.execute(_query)

            allSQLRows = cursor.fetchall()

            lenRow = len(allSQLRows)
            lenCol = len(allSQLRows[0])

            self.desc_result.setRowCount(lenRow) ##set number of rows
            self.desc_result.setColumnCount(lenCol) ##this is fixed for result_out, ensure that both of your tables, sql and qtablewidged have the same number of columns

            if allSQLRows is not None:
                for lin in range(0,lenRow):
                    for col in range(0,lenCol):
                        data = QTableWidgetItem(str(allSQLRows[lin][col]))
                        self.desc_result.setItem(lin,col,data)

            columns = cursor.description
            for col in range(0,lenCol):
                headerName = QTableWidgetItem(columns[col][0])
                self.desc_result.setHorizontalHeaderItem(col, headerName)

            self.processEvents()

        except Exception as error:
            self.WriteConsole(error,True)
            pass

    def Get_All_Data (self):
        table = self.tables_out.currentItem().text()
        _query = "select* from %s"%table

        try:
            cursor = self.mydb.cursor()
            cursor.execute(_query)

            allSQLRows = cursor.fetchall()

            lenRow = len(allSQLRows)
            lenCol = len(allSQLRows[0])

            self.data_result.setRowCount(lenRow) ##set number of rows
            self.data_result.setColumnCount(lenCol) ##this is fixed for result_out, ensure that both of your tables, sql and qtablewidged have the same number of columns

            if allSQLRows is not None:
                for lin in range(0,lenRow):
                    for col in range(0,lenCol):
                        data = QTableWidgetItem(str(allSQLRows[lin][col]))
                        self.data_result.setItem(lin,col,data)

            columns = cursor.description
            for col in range(0,lenCol):
                headerName = QTableWidgetItem(columns[col][0])
                self.data_result.setHorizontalHeaderItem(col, headerName)
            
            self.processEvents()

        except Exception as error:
            self.WriteConsole(error,True)
            pass

    def WriteConsole (self,text,isError):
        if isError:
            error = "{0} {1:<10} :::   {2}\n".format(time.strftime("%x"),time.strftime("%X"),text)

            self.console_out.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(79, 0, 1);padding:10;")
            self.console_out.setPlainText(error)
        else:
            self.console_out.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(35, 68, 0);padding:10;")
            self.console_out.setPlainText(text)

    def add_tool_bar(self):
        print("TOOL BAR")

        tb = self.addToolBar("File")

        compileAll = QAction(QIcon(r'src\Toolbar_Icons\compile.PNG'),"Compile All",self)
        compileAll.triggered.connect(self.GetAllQuery)

        compileSelected = QAction(QIcon(r'src\Toolbar_Icons\compileSel.PNG'),"Compile Selected",self)
        compileSelected.triggered.connect(self.GetSelectedQuery)

        import_t = QAction(QIcon(r'src\Toolbar_Icons\import.PNG'),"Import Query",self)
        import_t.triggered.connect(self.load_query_from_file)

        export_t = QAction(QIcon(r'src\Toolbar_Icons\export.PNG'),"Export Query",self)
        export_t.triggered.connect(self.save_query_to_file)

        refresh_t = QAction(QIcon(r'src\Toolbar_Icons\refresh.PNG'),"Refresh Tables",self)
        refresh_t.triggered.connect(self.Get_Tables)


        tb.addAction(refresh_t)
        tb.addAction(compileAll)
        tb.addAction(compileSelected)
        tb.addAction(import_t)
        tb.addAction(export_t)

    def load_query_from_file(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open QUERY file', 'Query',"Select query file (*.txt *.sql *.dat *.csv *.tsv *.psv)")
            selectFilePath = str(fname[0])

            fileopen = open(r'%s'%selectFilePath,'r')
            _content = str(fileopen.read())

            self.query_in.setPlainText(_content)
        except FileNotFoundError:pass

    def save_query_to_file(self):
        try:
            options = QFileDialog.Options()
            saved_file,_ = QFileDialog.getSaveFileName(self,"Export Query","Query","Query Files (*.sql);;Text Files (*.txt);;Data Files (*.dat);;All Files (*)",options=options)
            
            toSave_query = self.query_in.toPlainText()

            _file = open(saved_file,'w')
            _file.write(toSave_query)
            _file.close()
        except FileNotFoundError:pass

