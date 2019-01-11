from PyQt5 import QtCore
from PyQt5.uic import loadUi

from PyQt5.QtGui import QStandardItemModel,QStandardItem

from PyQt5.QtWidgets import QApplication, QDialog,QFileDialog,QMainWindow,QStyleFactory
from PyQt5.QtWidgets import QAction,QToolBar,QTableWidget,QTableWidgetItem,QHeaderView,QTreeWidgetItem

from PyQt5.QtCore import pyqtSlot,QFile, QTextStream,QCoreApplication,Qt
from PyQt5.QtGui import QIcon

import time
import sys
import mysql.connector as mysql
from functools import partial

from Lib.UI.SCRIPT.MainWindow import Ui_SQLMANAGER
from Lib.icons_manager import _run,_runSelected,_import,_export,_refresh,ui_db,ui_tb

class ManagerWindow(QMainWindow,QToolBar,QTreeWidgetItem,QCoreApplication,Ui_SQLMANAGER,object):

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
            self.WriteConsole("Connected to SQL Server")
        except:
            self.WriteConsole("Cannot Connect to SQL Server")

        
        self.Get_Tables()

        self.tables_out.itemSelectionChanged.connect(self.Get_Desc)
        self.tables_out.itemSelectionChanged.connect(self.Get_All_Data)
        self.tables_out.itemDoubleClicked.connect(self.ItemDoubleClicked)

    def ItemDoubleClicked      (self):
        index = self.tables_out.currentIndex()
        data =  self.tables_out.model().data(index)
        text = str(data)

        if text in self.db_tables:
            self.query_in.insertPlainText(text)
        elif text in self.databases:
            self.mydb.database = text
            self.Get_Tables()
            print(text)

    
    def Execute_Querry      (self,text):
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

            self.result_out.resizeColumnsToContents()

            self.WriteConsole(_query)

        except Exception as error:
            self.WriteConsole(error)
            pass
    
    def GetAllQuery         (self):
        _allQuery = str(self.query_in.toPlainText()).replace("\n"," ")
        self.Execute_Querry(_allQuery) 
    
    def GetSelectedQuery    (self):
        cursor = self.query_in.textCursor()
        
        _allText = str(self.query_in.toPlainText()).replace("\n"," ")
        _startIndex = cursor.selectionStart()
        _endIndex = cursor.selectionEnd()
        
        _buildText = ""

        for letter in range(_startIndex,_endIndex):
            _buildText+=_allText[letter]

        self.Execute_Querry(_buildText)
    
    def Get_Tables          (self):
        try:            
            self.tables_out.clear()
            self.databases = []

            _dict = {}
            
            self.mycursor = self.mydb.cursor()            

            self.mycursor.execute("show databases")
            dbs = self.mycursor.fetchall()

            self.mycursor.execute("show tables")
            tbs = self.mycursor.fetchall()

            self.mycursor.execute("select database()")
            actualDatabase = self.mycursor.fetchall()

            _adb = actualDatabase[0][0]
            for db in dbs:
                _db = db[0]
                self.databases.append(_db)

                parent = QTreeWidgetItem(self.tables_out)
                parent.setText(0,"%s"%_db)
                parent.setIcon(0,QIcon(ui_db))
                parent.setFlags(parent.flags())
                parent.setExpanded(True)

                if _db == _adb:
                    for tb in tbs:
                        child = QTreeWidgetItem(parent)
                        child.setFlags(child.flags())
                        child.setText(0,"%s"%tb)
                        child.setIcon(0,QIcon(ui_tb))

                    parent.setExpanded(True)

            self.db_tables = []
            for ttbs in tbs:
                self.db_tables.append(ttbs[0])

        except Exception as error:
            self.WriteConsole(error)
            pass
    
    def Get_Desc            (self):
        index = self.tables_out.currentIndex()
        data =  self.tables_out.model().data(index)
        table = str(data)

        if table in self.db_tables:
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

                self.desc_result.resizeColumnsToContents()
                self.WriteConsole(str(_query))
                self.processEvents()

            except Exception as error:
                self.WriteConsole(error)
                pass
    
    def Get_All_Data        (self):
        index = self.tables_out.currentIndex()
        data =  self.tables_out.model().data(index)
        table = str(data)

        if table in self.db_tables:
            _query = "select* from %s"%table

            try:
                cursor = self.mydb.cursor()
                cursor.execute(_query)

                allSQLRows = cursor.fetchall()

                lenRow = len(allSQLRows)
                lenCol = len(allSQLRows[0])

                self.data_result.setRowCount(lenRow) ##set number of rows
                self.data_result.setColumnCount(lenCol) ##set number of columns 

                if allSQLRows is not None:
                    for lin in range(0,lenRow):
                        for col in range(0,lenCol):
                            data = QTableWidgetItem(str(allSQLRows[lin][col]))
                            self.data_result.setItem(lin,col,data)

                columns = cursor.description
                for col in range(0,lenCol):
                    headerName = QTableWidgetItem(columns[col][0])
                    self.data_result.setHorizontalHeaderItem(col, headerName)
                
                self.data_result.resizeColumnsToContents()
                self.WriteConsole(str(_query))
                self.processEvents()
            except Exception as error:
                self.WriteConsole(error)
                pass

    def add_tool_bar        (self):
        toolBar = QToolBar()
        toolBar.setMovable(False)
        tb_config = self.addToolBar(Qt.LeftToolBarArea,toolBar)
        # tb = self.addToolBar("File")

        ############### CREATING BUTTONS ICONS AND SETTING FUNCTION #####################################################################################################
        compileAll =        QAction(QIcon(_run),        "Execute SQL        (F9)",              self,shortcut="F9",             triggered=self.GetAllQuery)              #
        compileSelected =   QAction(QIcon(_runSelected),"Execute Selected   (Shift+Ctrl+F9)",   self,shortcut="Shift+Ctrl+F9",  triggered=self.GetSelectedQuery)         #
        import_t =          QAction(QIcon(_import),     "Load SQL from file (Ctrl+O)",          self,shortcut="Ctrl+O",         triggered=self.load_query_from_file)     #
        export_t =          QAction(QIcon(_export),     "Save SQL in file   (Ctrl+S)",          self,shortcut="Ctrl+S",         triggered=self.save_query_to_file)       #
        refresh_t =         QAction(QIcon(_refresh),    "Refresh            (F5)",              self,shortcut="F5",             triggered=self.Get_Tables)               #
        #################################################################################################################################################################

        ## ADDING BUTTON TO MENU ################
        toolBar.addAction(refresh_t)             #
        toolBar.addSeparator()                   #
        toolBar.addAction(compileAll)            #
        toolBar.addAction(compileSelected)       #
        toolBar.addSeparator()                   #
        toolBar.addAction(import_t)              #
        toolBar.addAction(export_t)              #
        #########################################
    
    def load_query_from_file(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Load SQL From file', 'Query',"Select query file (*.indext *.sql *.dat *.csv *.tsv *.psv)")
            selectFilePath = str(fname[0])
            fileopen = open(r'%s'%selectFilePath,'r')
            _content = str(fileopen.read())
            self.query_in.setPlainText(_content)
        except FileNotFoundError:pass
    
    def save_query_to_file  (self):
        try:
            options = QFileDialog.Options()
            saved_file,_ = QFileDialog.getSaveFileName(self,"Save SQL to file Query","Query","Query Files (*.sql);;Text Files (*.indext);;Data Files (*.dat);;All Files (*)",options=options)            
            toSave_query = self.query_in.toPlainText()
            _file = open(saved_file,'w')
            _file.write(toSave_query)
            _file.close()
        except FileNotFoundError:pass

    def WriteConsole        (self,text):
        self.console_out.appendPlainText(str(text))
        self.processEvents()
    