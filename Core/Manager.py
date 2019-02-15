import sys
import time
from functools import partial
import mysql.connector as mysql
import xlrd
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication, QFile, Qt, QTextStream, pyqtSlot
from PyQt5.QtGui import QIcon, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import (QAction, QApplication, QDialog, QFileDialog,QHeaderView,
QMainWindow, QMenu, QMessageBox,QSizePolicy, QStyleFactory, QTableWidget,QTableWidgetItem,
 QToolBar, QTreeWidgetItem,QWidget, qApp)

from Lib.icons_manager import (_export, _import, _newDatabase, _newTable,
                               _refresh, _run, _runSelected, ico_consult,
                               ui_db, ui_tb)


from assets.UI.Scripts.MainWindow import Ui_SQLMANAGER
from Core.Table_Creator import TBCreator
from Core.Database_Creator import DBCreator
from Core.Console import Console

class ManagerWindow(QMainWindow,QToolBar,QTreeWidgetItem,QCoreApplication,QWidget,Ui_SQLMANAGER,object):
    def __init__(self,hs,pt,us,ps,bfr, parent = None):
        super(ManagerWindow,self).__init__(parent)
        self.setupUi(self)
        self.add_tool_bar()
        self.setWindowIcon(QIcon(ico_consult))
        self.showMaximized()

        self.hs = hs
        self.pt = pt
        self.us = us
        self.ps = ps
        self.bfred = bfr

        try:
            self.mydb = mysql.connect(host=self.hs,port=self.pt,user=self.us,passwd=self.ps,buffered=self.bfred)
            self.console_output('<b>Connected to SQL Server</b>',True)
            self.get_server_dbs()
        except:
            self.console_output('<p style="color:rgb(175, 50, 50);">Cannot Connect to SQL Server</span>',True)

        self.tables_out.itemDoubleClicked.connect(self.ItemDoubleClicked)
        self.openConsole.clicked.connect(self.expand_console)

        self.openedConsole = False

    def EXECUTE_QUERY_HANDLER(self,text):            ## MASTER HANDLER FOR EXECUTE ANY QUERY AND RETURN ALL RESULTS  
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
            self.console_output("%s"%_query.lower(),False)
            self.processEvents()
        except Exception as error:
            self.console_output(error,True)
            pass
    
    def ItemDoubleClicked    (self):                 ## SINGLE CLICK HANDLER FOR QTreeWIDGET 
        index = self.tables_out.currentIndex()
        data =  self.tables_out.model().data(index)
        text = str(data)
        if text in self.databases and text != str(self.mydb.database):
            lastDb = self.mydb.database
            self.mydb.database = text
            nowDb = self.mydb.database
            if lastDb != nowDb and lastDb != "None":
                self.tables_out.clear()
                self.get_server_dbs()
                self.get_tables_from_db(nowDb)
        if text not in self.databases:
            self.get_table_script(text)
            self.get_table_types(text)
            self.get_table_data(text)
        self.processEvents() 
    
    def get_all_text         (self):                 # EXECUTE ALL QUERY TEXT           
        _allQuery = str(self.query_in.toPlainText()).replace("\n"," ")
        self.EXECUTE_QUERY_HANDLER(_allQuery)
        self.processEvents()
    
    def get_selected_text    (self):                 # EXECUTE ONLY SELECTED QUERY TEXT 
        cursor = self.query_in.textCursor()
        _allText = str(self.query_in.toPlainText()).replace("\n"," ")
        _startIndex = cursor.selectionStart()
        _endIndex = cursor.selectionEnd()
        _buildText = ""
        for letter in range(_startIndex,_endIndex):
            _buildText+=_allText[letter]
        self.EXECUTE_QUERY_HANDLER(_buildText)
        self.processEvents()
    
    def get_server_dbs       (self):                 # GET ALL DATABASES IN SERVER AND RETURN AS PARENT TO QTREEVIEW    
        try:
            self.tables_out.clear()
            self.databases = []
            _dict = {}
            self.mycursor = self.mydb.cursor()
            self.mycursor.execute("show databases")
            self.dbs = self.mycursor.fetchall()
            for db in self.dbs:
                _db = db[0]
                self.databases.append(_db)
                parent = QTreeWidgetItem(self.tables_out)
                parent.setText(0,"%s"%_db)
                parent.setIcon(0,QIcon(ui_db))
                parent.setFlags(parent.flags())
            self.console_output("SHOW DATABASES",False)
        except Exception as error:
            self.application_error(error)
            pass
    
    def get_tables_from_db   (self,_cDb):            # GET ALL TABLES FROM DATABASE AND RETURN IN TREE VIEW AS CHILD OF DATABASE PARENT ITEM 
        top_level_items = self.tables_out.topLevelItemCount()
        for i in range(top_level_items):
            top_item = self.tables_out.topLevelItem(i)
            item_name = top_item.text(0)
            if item_name == str(_cDb):
                self.mycursor.execute("show tables")
                self.tbs = self.mycursor.fetchall()
                for tb in self.tbs:
                    child = QTreeWidgetItem(top_item)
                    child.setFlags(child.flags())
                    child.setText(0,"%s"%tb)
                    child.setIcon(0,QIcon(ui_tb))
                break
        self.tables_out.expandAll()
        self.console_output("SHOW TABLES",False)
    
    def get_table_script     (self,data):            # GET CREATE TABLE SCRIPT       
        table = str(data)
        _query = "show create table %s" %table
        try:
            self.create_in.setPlainText('')
            cursor = self.mydb.cursor()
            cursor.execute(_query)
            allSQLRows = cursor.fetchall()
            code_create = str(allSQLRows[0][1])
            schemeCode = self.colorize_sql_query(code_create)
            self.create_in.appendHtml(schemeCode)
            self.console_output("%s"%str(_query),False)
        except Exception as error:
            self.console_output(error,True)
            print(error)
    
    def get_table_types      (self,data):            # GET ALL TABLES DESCRITIONS    
        table = str(data)
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
            self.processEvents()
        except Exception as error:
            self.console_output(error,True)
            pass    
    
    def get_table_data       (self,data):            # GET ALL DATA FROM TABLES      
        table = str(data)
        _query = "select * from %s"%table
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
            self.processEvents()
        except Exception as error:
            self.console_output(error,True)
            pass
    
    def load_query_from_file (self):                 # OPEN DIALOG BOX TO LOAD FILE  
        try:
            fname = QFileDialog.getOpenFileName(self, 'Load SQL From file', 'Query',"Select query file (*.indext *.sql *.dat *.csv *.tsv *.psv)")
            selectFilePath = str(fname[0])
            fileopen = open(r'%s'%selectFilePath,'r')
            _content = str(fileopen.read())
            self.query_in.setPlainText(_content)
            self.processEvents()
        except FileNotFoundError:pass
    
    def save_query_to_file   (self):                 # OPEN DIALOG BOX TO SAVE QUERY TEXT TO FILE    
        try:
            options = QFileDialog.Options()
            saved_file,_ = QFileDialog.getSaveFileName(self,"Save SQL to file Query","Query","Query Files (*.sql);;Text Files (*.indext);;Data Files (*.dat);;All Files (*)",options=options)            
            toSave_query = self.query_in.toPlainText()
            _file = open(saved_file,'w')
            _file.write(toSave_query)
            _file.close()
            self.processEvents()
        except FileNotFoundError:pass
    
    def create_database      (self):                 # OPEN DATABASE CREATOR WIZARD     
        try:
            self.databaseCreator = DBCreator(self.hs,self.pt,self.us,self.ps,self.bfred,self)
            self.databaseCreator.show()

        except Exception as error:
            self.application_error(error)
            pass
     
    def create_table         (self):                 # OPEN TABLE CREATOR WIZARD        
        try:
            if not (self.mydb.database is None):
                self.tableCreator = TBCreator(str(self.mydb.database),self.hs,self.pt,self.us,self.ps,self.bfred,self)
                self.tableCreator.show()
            else:
                self.application_error("myqt_1:\nNo database selected")
        except Exception as error:
            self.application_error(error)
            pass

    def refresh_database     (self):                 # REFRESH HANDLER FOR REFRESHIND DATABASE AND ITS TABLE    
        self.get_server_dbs()
        _db = str(self.mydb.database)
        self.get_tables_from_db(_db)

    def add_tool_bar         (self):                 # ADD TOOLBAR AND TOOLBAR ICONS HANDLER                    
        toolBar = QToolBar()
        toolBar.setMovable(False)
        toolBar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        
        tb_config = self.addToolBar(Qt.LeftToolBarArea,toolBar)

        refresh_t       = QAction(QIcon(_refresh),    "REFRESH",self,shortcut="F5",           triggered=self.refresh_database)
        compileAll      = QAction(QIcon(_run),        "COMPILE",self,shortcut="F9",           triggered=self.get_all_text)
        import_t        = QAction(QIcon(_import),     "IMPORT" ,self,shortcut="Ctrl+O",       triggered=self.load_query_from_file)
        export_t        = QAction(QIcon(_export),     "EXPORT" ,self,shortcut="Ctrl+S",       triggered=self.save_query_to_file)
        compileSelected = QAction(QIcon(_runSelected),"RUN SL" ,self,shortcut="Shift+Ctrl+F9",triggered=self.get_selected_text)
        newDatabase     = QAction(QIcon(_newDatabase),"NEW DB" ,self,                         triggered=self.create_database)
        newTable        = QAction(QIcon(_newTable)   ,"NEW TB" ,self,                         triggered=self.create_table)

        refresh_t.setToolTip        ("Refresh Server (F5)")
        import_t.setToolTip         ("Load SQL (Ctrl+O)")
        export_t.setToolTip         ("Save SQL (Ctrl+S)")
        compileAll.setToolTip       ("Run All QUERY (F9)")
        compileSelected.setToolTip  ("Run Selected QUERY (Shift+Ctrl+F9)")
        newDatabase.setToolTip      ("Open DATABASE CREATOR")
        newTable.setToolTip         ("Open TABLE CREATOR")

        toolBar.addAction(refresh_t)
        toolBar.addAction(import_t),toolBar.addAction(export_t)
        toolBar.addAction(compileAll),toolBar.addAction(compileSelected)
        toolBar.addAction(newDatabase),toolBar.addAction(newTable)
        
        self.processEvents()

    def expand_console       (self):                 # EXPAND CONSOLE WINDOW        
        _msg = str(self.console_out.toPlainText())
        self.consoleWindow = Console()
        self.consoleWindow.console.setPlainText(_msg)
        self.consoleWindow.show()
    
    def colorize_sql_query   (self,text):            # ADD COLOR TO SQL CODE        
        query = str(text.lower()).replace(","," , ").replace("("," ( ").replace(")"," ) ").replace("="," = ")
        from Lib.color_schema import schema,greenPat,bluePat
        words = query.split(" ")
        finalQuery = ""
        for w in words:
            if w in schema.keys():
                scWord = schema.get(w)
                finalQuery += "%s " %scWord.format(str(w).upper())
            else:
                try:
                    if eval(w) >= 0:
                        finalQuery += "%s " %bluePat.format(w)                    
                except:
                    finalQuery += "%s " %greenPat.format(w)
                    pass
        return finalQuery.replace('\n','<br></br>').replace(' , ',',').replace(' ) ',')').replace(' ( ','(') 
    
    def contextMenuEvent     (self,event):          # CUSTOM CONTEXT MENU           
        cmenu = QMenu(self)
        newDB   = cmenu.addAction("New Database",self.create_database)
        newTbl  = cmenu.addAction("New Table",self.create_table)
        saveSQL = cmenu.addAction("Save SQL",self.save_query_to_file)
        loadSQL = cmenu.addAction("Load SQL",self.load_query_from_file)

        action = cmenu.exec_(self.mapToGlobal(event.pos()))

    def console_output       (self,text,isError):   # DEBUG ALL STATE TO CONSOLE    
        if isError == False:
            coloredText = self.colorize_sql_query(text)
            self.console_out.appendHtml(coloredText)
            self.processEvents()
        else:
            errorPat = '<p style="color:rgb(175, 50, 50);">{0}</span>'
            self.console_out.appendHtml(errorPat.format(str(text)))
            self.processEvents()
    
    def application_error    (self,error): reply = QMessageBox.critical(self, "CRITICAL ERROR",str(error),QMessageBox.Ok)
