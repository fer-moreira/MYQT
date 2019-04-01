"""
MYQT.Manager é o modulo principal que gerencia todo o funcionamento do aplicativo

Como:
- Gerenciamento de tabelas
- Criação, modificação e remoção de banco de dados
- Amostragem de resultado em tabela
- Exportar uma tabela para um arquivo

"""

import sys
import time
from functools import partial

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication, QFile, Qt,QPoint
from PyQt5.QtGui import QIcon,QCursor
from PyQt5.QtWidgets import (QAction, QDialog, QFileDialog,QHeaderView,
QMainWindow, QMenu, QMessageBox,QSizePolicy, QTableWidget,QTableWidgetItem,
QToolBar, QTreeWidgetItem,QWidget, qApp)

from Lib.icons_manager import _export, _import, _newDatabase, _refresh, _run, _runSelected, _viewGraphs, _exportData,_settings
from Lib.icons_manager import ui_db, ui_tb,ui_folder, ui_data,ui_field,ui_query
from Lib.icons_manager import win_icon

from Lib.SQL_formatter import Formatter

from assets.UI.Scripts.MainWindow import Ui_SQLMANAGER
# from Core.Table_Creator import TBCreator
from Core.Database_Creator import DBCreator
from Core.Console import Console

from Engines import MYSQL_Engine
from Engines import MSSQL_Engine

class ManagerWindow(QMainWindow,QToolBar,QTreeWidgetItem,QCoreApplication,QWidget,Ui_SQLMANAGER,object):
    def __init__(self,hs,pt,us,ps,bfr,type, parent = None):
        super(ManagerWindow,self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(win_icon))
        self.tabs.setTabIcon(0,QIcon(ui_data))
        self.tabs.setTabIcon(1,QIcon(ui_field))
        self.tabs.setTabIcon(2,QIcon(ui_query))
        self.add_tool_bar()
        self.showMaximized()

        self.hs = hs;self.pt = pt
        self.us = us;self.ps = ps
        self.bfred = bfr;self.type = type

        if self.type == 'mysql':
            self.mydb = MYSQL_Engine.connect(self.hs,self.pt,self.us,self.ps,self.bfred)
        if self.type == 'mssql':
            self.mydb = MSSQL_Engine.connect(self.hs,self.us,self.ps)

        self.console_output('<b>Connected to SQL Server</b>',True)
        self.get_server_dbs()

        self.tables_out.itemDoubleClicked.connect(self.ItemDoubleClicked)
        self.openConsole.clicked.connect(self.expand_console)

        self.openedConsole = False

    def EXECUTE_QUERY_HANDLER(self,text):            ## 
        """Master function to execute all type of query and return in result table"""

        _query = text
        try:
            self.result_out.clear()
            self.result_out.verticalScrollBar().setValue(self.result_out.verticalScrollBar().maximum())

            cursor = self.mydb.cursor()
            cursor.execute(_query)
            try:
                allSQLRows = cursor.fetchall() #fetch results to dictionary
                # allSQLRows_dict = allSQLRows
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
                self.result_out.resizeColumnsToContents()
                self.console_output("%s"%_query.lower(),False)
                syntax_pars.PythonHighlighter(self.query_in.document())

            except:pass
            # self.console_output(_query,False)
        except Exception as error:
            self.console_output(error,True)
            pass

    def ItemDoubleClicked    (self):                 ## SINGLE CLICK HANDLER FOR QTreeWIDGET
        index = self.tables_out.currentIndex()
        data =  self.tables_out.model().data(index)
        _selected = str(data)

        cursor = self.mydb.cursor()

        if _selected in self.databases:
            if self.type == 'mysql':
                MYSQL_Engine.Set_Database(cursor,_selected)
                self.refresh_database(_selected)
            if self.type == 'mssql': 
                MSSQL_Engine.Set_Database(cursor,_selected)
                self.refresh_database(_selected)
        if _selected in self.tables:
            self.get_table_types(_selected)
            self.get_table_data(_selected)

    def get_server_dbs       (self):
        """GET ALL DATABASES IN SERVER AND RETURN AS PARENT TO QTREEVIEW"""
        self.tables_out.clear()
        self.databases = []
        _dict = {}

        cursor = self.mydb.cursor()

        if self.type == 'mysql':
            self.dbs = MYSQL_Engine.databases(cursor)
        if self.type == 'mssql':
            self.dbs = MSSQL_Engine.databases(cursor)

        for db in self.dbs:
            _db = db[0]
            self.databases.append(_db)
            parent = QTreeWidgetItem(self.tables_out)
            parent.setText(0,"%s"%_db)
            parent.setIcon(0,QIcon(ui_db))
            parent.setFlags(parent.flags())

    def get_tables_from_db   (self,_cDb):
        """GET ALL TABLES FROM DATABASE AND RETURN IN TREE VIEW AS CHILD OF DATABASE PARENT ITEM"""
        self.tables = []


        cursor = self.mydb.cursor()
        if self.type == 'mysql' : self.tbs = MYSQL_Engine.tables(cursor)
        if self.type == 'mssql' : self.tbs = MSSQL_Engine.tables(cursor)

        top_level_items = self.tables_out.topLevelItemCount()

        for i in range(top_level_items):
            top_item = self.tables_out.topLevelItem(i)
            item_name = top_item.text(0)
            if item_name == str(_cDb):
                folder = QTreeWidgetItem(top_item)
                folder.setText(0,"Tables")
                folder.setIcon(0,QIcon(ui_folder))
                
                for tb in self.tbs:
                    _tb = tb[0]
                    self.tables.append(_tb)

                    child = QTreeWidgetItem(folder)
                    child.setFlags(child.flags())
                    child.setText(0,"%s"%tb)
                    child.setIcon(0,QIcon(ui_tb))
                break

    def execute_all_query    (self):
        """EXECUTE ALL QUERY TEXT"""
        _allQuery = str(self.query_in.toPlainText()).replace("\n"," ")
        self.EXECUTE_QUERY_HANDLER(_allQuery)
        self.processEvents()

    def execute_selected_query    (self):
        """EXECUTE ONLY SELECTED QUERY TEXT"""
        cursor = self.query_in.textCursor()
        _allText = str(self.query_in.toPlainText()).replace("\n"," ")
        _startIndex = cursor.selectionStart()
        _endIndex = cursor.selectionEnd()
        _buildText = ""
        for letter in range(_startIndex,_endIndex):
            _buildText+=_allText[letter]
        self.EXECUTE_QUERY_HANDLER(_buildText)
        self.processEvents()
  
    def get_table_script     (self,table):
        """GET CREATE TABLE SCRIPT"""

    def get_table_types      (self,tb):
        """GET ALL TABLES DESCRITIONS"""
        table = str(tb)
        cursor = self.mydb.cursor()
        try:
            if self.type == 'mysql':
                allSQLRows = MYSQL_Engine.Get_Struct(cursor,table)
            if self.type == 'mssql':
                allSQLRows = MSSQL_Engine.Get_Struct(cursor,table)

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

    def get_table_data       (self,tb):
        """GET ALL DATA FROM TABLES"""
        table = str(tb)
        cursor = self.mydb.cursor()

        try:
            if self.type == 'mysql': allSQLRows = MYSQL_Engine.Get_Data(cursor,table)
            if self.type == 'mssql': allSQLRows = MSSQL_Engine.Get_Data(cursor,table)

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
        except Exception as error:
            self.console_output(error,True)
            pass

    def load_query_from_file (self):
        """OPEN DIALOG BOX TO LOAD FILE"""
        try:
            fname = QFileDialog.getOpenFileName(self, 'Load SQL From file', 'Query',"Select query file (*.indext *.sql *.dat *.csv *.tsv *.psv)")
            selectFilePath = str(fname[0])
            fileopen = open(r'%s'%selectFilePath,'r')
            _content = str(fileopen.read())
            self.query_in.setPlainText(_content)
            self.processEvents()
        except FileNotFoundError:pass

    def save_query_to_file   (self):
        """OPEN DIALOG BOX TO SAVE QUERY TEXT TO FILE"""
        try:
            options = QFileDialog.Options()
            saved_file,_ = QFileDialog.getSaveFileName(self,"Save SQL to file Query","Query","Query Files (*.sql);;Text Files (*.indext);;Data Files (*.dat);;All Files (*)",options=options)
            toSave_query = self.query_in.toPlainText()
            _file = open(saved_file,'w')
            _file.write(toSave_query)
            _file.close()
            self.processEvents()
        except FileNotFoundError:pass

    def create_database      (self):
        """OPEN DATABASE CREATOR WIZARD"""
        try:
            self.databaseCreator = DBCreator(self.hs,self.pt,self.us,self.ps,self.bfred,self)
            self.databaseCreator.show()

        except Exception as error:
            self.application_error(error)
            pass

    def refresh_database     (self,db):
        """REFRESH HANDLER FOR REFRESHIND DATABASE AND ITS TABLE"""
        self.tables_out.clear()
        cursor = self.mydb.cursor()

        # if self.type == 'mysql': db = MYSQL_Engine.Get_Data(cursor)
        if self.type == 'mssql': db = MSSQL_Engine.Database(cursor)
        
        self.get_server_dbs()
        self.get_tables_from_db(db)
        self.tables_out.expandAll()

    def add_tool_bar         (self):
        """ADD TOOLBAR AND TOOLBAR ICONS HANDLER"""
        toolBar = QToolBar()
        toolBar.setMovable(False)
        toolBar.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.addToolBar(Qt.LeftToolBarArea,toolBar)

        refresh_t       = QAction(QIcon(_refresh),    "REFRESH",self,shortcut="F5",           triggered=self.refresh_database)
        compileAll      = QAction(QIcon(_run),        "COMPILE",self,shortcut="F9",           triggered=self.execute_all_query)
        import_t        = QAction(QIcon(_import),     "IMPORT" ,self,shortcut="Ctrl+O",       triggered=self.load_query_from_file)
        export_t        = QAction(QIcon(_export),     "EXPORT" ,self,shortcut="Ctrl+S",       triggered=self.save_query_to_file)
        compileSelected = QAction(QIcon(_runSelected),"RUN SL" ,self,shortcut="Shift+Ctrl+F9",triggered=self.execute_selected_query)
        newDatabase     = QAction(QIcon(_newDatabase),"NEW DB" ,self,                         triggered=self.create_database)
        exportData      = QAction(QIcon(_exportData) ,"EXPORT" ,self,                         triggered=lambda:self.export_table(self.result_out))
        settings        = QAction(QIcon(_settings), "SETTINGS"  ,self,                        triggered=lambda: print("WORKS"))


        refresh_t.setToolTip        ("Refresh all server databases and table (F5)")
        import_t.setToolTip         ("Load SQL (Ctrl+O)")
        export_t.setToolTip         ("Save SQL (Ctrl+S)")
        compileAll.setToolTip       ("Run all query (F9)")
        compileSelected.setToolTip  ("Run selected query (Shift+Ctrl+F9)")
        newDatabase.setToolTip      ("Open database creator")
        exportData.setToolTip       ("Export all data from result table")
        settings.setToolTip         ("View settings")

        # toolBar.addSeparator()
        toolBar.addAction(refresh_t)
        toolBar.addAction(import_t),toolBar.addAction(export_t)
        toolBar.addSeparator()
        toolBar.addAction(compileAll),toolBar.addAction(compileSelected)
        toolBar.addSeparator()
        toolBar.addAction(newDatabase)
        toolBar.addSeparator()
        toolBar.addAction(exportData)

        _sp = QWidget()
        _sp.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Expanding)
        toolBar.addWidget(_sp)
        toolBar.addAction(settings)
        
        self.processEvents()

    def expand_console       (self):
        """EXPAND CONSOLE WINDOW"""
        _msg = str(self.console_out.toPlainText())
        self.consoleWindow = Console()
        self.consoleWindow.console.setPlainText(_msg)
        self.consoleWindow.show()

    def colorize_sql_query   (self,text):
        """ADD COLOR TO SQL CODE"""
        return text

    def console_output       (self,text,isError):
        """DEBUG ALL STATE TO CONSOLE"""
        if isError == False:
            coloredText = self.colorize_sql_query(text)
            self.console_out.appendHtml(coloredText)
            self.processEvents()
        else:
            errorPat = '<p style="color:rgb(175, 50, 50);">{0}</span>'
            self.console_out.appendHtml(errorPat.format(str(text)))
            self.processEvents()

    def application_error    (self,error): QMessageBox.critical(self, "CRITICAL ERROR",str(error),QMessageBox.Ok) ; print(error)

    def format_sql_text      (self):
        sql_text = str(self.query_in.toPlainText())

        formated_text = sql_text.replace("from","\nfrom").replace("FROM","\nFROM")
        self.query_in.setPlainText(formated_text)

    def export_table         (self,_w):  
        try:
            maxRow = _w.rowCount()
            maxColumn = _w.columnCount()

            _data = ""

            for r in range(0, maxRow):
                for c in range(0, maxColumn):
                    _d = str(_w.item(r, c).text())
                    _data += "%s," % _d
                _data += "\n"

            options = QFileDialog.Options()

            saved_file, _ = QFileDialog.getSaveFileName(self, "Save Table to file ", "data", "Table to text data(*.txt);;Table to csv (*.csv);;All Files (*)", options=options)
            _file = open(saved_file, 'w')
            _file.write(_data)
            _file.close()
        except FileNotFoundError:pass