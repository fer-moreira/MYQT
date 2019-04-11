"""
MYQT.Manager é o modulo principal que gerencia todo o funcionamento do aplicativo

Como:
- Gerenciamento de tabelas
- Criação, modificação e remoção de banco de dados
- Amostragem de resultado em tabela
- Exportar uma tabela para um arquivo

"""

import traceback

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication, QFile, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QFileDialog,QMainWindow, QMessageBox, QTableWidget,QTableWidgetItem, QTreeWidgetItem,QWidget


from assets.UI.Scripts.MainWindow import Ui_SQLMANAGER

from Engines import MYSQL_Engine
from Engines import MSSQL_Engine
from Engines import POSTG_Engine

from Helper.ManagerTools import ManagerTools
from Helper.IconsHandler import ui_db, ui_tb

from Helper.ConfigHandler import ConfigHandler

class ManagerWindow(QMainWindow,QTreeWidgetItem,QCoreApplication,QWidget,Ui_SQLMANAGER,object):
    def __init__(self,hs,pt,us,ps,bfr,_type, parent = None):
        super(ManagerWindow,self).__init__(parent)
        self.setupUi(self)

        self.cf = ConfigHandler(self)
        self.cf.load_theme()

        toolsManager = ManagerTools(self)
        toolsManager.SetIcons()
        toolsManager.AddVerticalToolbar()

        self.showMaximized()

        self.hs = hs;self.pt = pt
        self.us = us;self.ps = ps
        self.bfred = bfr
        self.type = _type

        if self.type == 'mysql':    self.mydb = MYSQL_Engine.connect(self.hs,self.pt,self.us,self.ps,self.bfred)
        if self.type == 'mssql':    self.mydb = MSSQL_Engine.connect(self.hs,self.us,self.ps)
        if self.type == 'postgre':  self.mydb = POSTG_Engine.connect("postgres",self.hs,self.pt,self.us,ps)

        self.refresh_database()
        self.get_server_dbs()


        self.tables_out.itemDoubleClicked.connect(self.ItemDoubleClicked)
    


    def EXECUTE_QUERY_HANDLER(self,text):
        """
        EXECUTE_QUERY_HANDLER ('Sample Query')
        """

        _query = str(text)
        try:
            self.result_out.clear()

            cursor = self.mydb.cursor()
            cursor.execute(_query)
            allSQLRows = cursor.fetchall()
            lenRow = len(allSQLRows)
            lenCol = len(allSQLRows[0])

            self.result_out.setRowCount(lenRow)
            self.result_out.setColumnCount(lenCol) 

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
            traceback.print_exc();self.application_error(error)


    # ──────────────────────────────────────────────────────────────────────────────────────────────────────────────── # 
    
    def ItemDoubleClicked  (self):
        "ItemDoubleClicked()"
        index = self.tables_out.currentIndex()
        data =  self.tables_out.model().data(index)
        _selected = str(data)

        cursor = self.mydb.cursor()

        if _selected in self.databases:
            if self.type == 'mysql'  : MYSQL_Engine.Set_Database(cursor,_selected)
            if self.type == 'mssql'  : MSSQL_Engine.Set_Database(cursor,_selected)
            if self.type == 'postgre': self.mydb = POSTG_Engine.connect(str(_selected),self.hs,self.pt,self.us,self.ps)
            self.refresh_database()

        if _selected in self.tables:
            self.get_table_types(_selected)
            self.get_table_data(_selected)

    # ──────────────────────────────────────────────────────────────────────────────────────────────────────────────── # 

    def refresh_database       (self):
        """refresh_database("Database Name")"""
        cursor = self.mydb.cursor()

        if self.type == 'mysql'  : db = MYSQL_Engine.Database(cursor)
        if self.type == 'mssql'  : db = MSSQL_Engine.Database(cursor)
        if self.type == 'postgre': db = POSTG_Engine.Database(cursor)
        
        if not db == None:
            self.tables_out.clear()
            self.get_server_dbs()
            self.get_tables_from_db(db)
            self.tables_out.expandAll()

    def get_server_dbs     (self):
        """ get_server_dbs () """
        self.tables_out.clear()
        self.databases = []
        _dict = {}

        cursor = self.mydb.cursor()

        if self.type == 'mysql'  : self.dbs = MYSQL_Engine.databases(cursor)
        if self.type == 'mssql'  : self.dbs = MSSQL_Engine.databases(cursor)
        if self.type == 'postgre': self.dbs = POSTG_Engine.databases(cursor)

        for db in self.dbs:
            _db = db[0]
            self.databases.append(_db)
            parent = QTreeWidgetItem(self.tables_out)
            parent.setText(0,"%s"%_db)
            parent.setIcon(0,QIcon(ui_db))
            parent.setFlags(parent.flags())

    def get_tables_from_db (self,_cDb):
        """get_tables_from_db("Current Database")"""
        self.tables = []

        cursor = self.mydb.cursor()
        if self.type == 'mysql'   : self.tbs = MYSQL_Engine.tables(cursor)
        if self.type == 'mssql'   : self.tbs = MSSQL_Engine.tables(cursor)
        if self.type == 'postgre' : self.tbs = POSTG_Engine.tables(cursor)

        top_level_items = self.tables_out.topLevelItemCount()

        for i in range(top_level_items):
            top_item = self.tables_out.topLevelItem(i)
            item_name = top_item.text(0)
            if item_name == str(_cDb):
                
                for tb in self.tbs:
                    _tb = tb[0]
                    self.tables.append(_tb)
                    table_name = "%s"%tb

                    child = QTreeWidgetItem(top_item)
                    child.setFlags(child.flags())
                    child.setText(0,table_name)
                    child.setToolTip(0,table_name)
                    child.setIcon(0,QIcon(ui_tb))
                break

    # ──────────────────────────────────────────────────────────────────────────────────────────────────────────────── # 

    

    def execute_all_query      (self):
        """execute_all_query ()"""
        _allQuery = str(self.query_in.toPlainText()).replace("\n"," ")
        self.EXECUTE_QUERY_HANDLER(_allQuery)
        self.processEvents()

    def execute_selected_query (self):
        """execute_selected_query ()"""
        cursor = self.query_in.textCursor()
        _allText = str(self.query_in.toPlainText()).replace("\n"," ")
        _startIndex = cursor.selectionStart()
        _endIndex = cursor.selectionEnd()
        _buildText = ""
        for letter in range(_startIndex,_endIndex):
            _buildText+=_allText[letter]
        self.EXECUTE_QUERY_HANDLER(_buildText)
        self.processEvents()
  
    # ──────────────────────────────────────────────────────────────────────────────────────────────────────────────── # 
    
    def get_table_types (self,tb):
        """get_table_types ('Table name')"""
        table = str(tb)
        cursor = self.mydb.cursor()
        try:
            if self.type == 'mysql'  : allSQLRows = MYSQL_Engine.Get_Struct(cursor,table)
            if self.type == 'mssql'  : allSQLRows = MSSQL_Engine.Get_Struct(cursor,table)
            if self.type == 'postgre': allSQLRows = POSTG_Engine.Get_Struct(cursor,table)

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
            traceback.print_exc();self.application_error(error)

    def get_table_data  (self,tb):
        """get_table_data ('Tablename')"""
        table = str(tb)
        cursor = self.mydb.cursor()

        try:
            if self.type == 'mysql'  : allSQLRows = MYSQL_Engine.Get_Data(cursor,table)
            if self.type == 'mssql'  : allSQLRows = MSSQL_Engine.Get_Data(cursor,table)
            if self.type == 'postgre': allSQLRows = POSTG_Engine.Get_Data(cursor,table)

            lenRow = len(allSQLRows)
            lenCol = len(allSQLRows[0])

            self.data_result.setRowCount(lenRow)
            self.data_result.setColumnCount(lenCol)

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
            traceback.print_exc();self.application_error(error)    
    
    # ──────────────────────────────────────────────────────────────────────────────────────────────────────────────── # 
    
    def application_error  (self,error):
        " application_error ('error text') "
        QMessageBox.critical(self, "CRITICAL ERROR",str(error),QMessageBox.Ok)

    # ──────────────────────────────────────────────────────────────────────────────────────────────────────────────── # 
    
    def load_query_from_file (self):
        " load_query_from_file () "
        try:
            fname = QFileDialog.getOpenFileName(self, 'Load SQL From file', 'Query',"Select query file (*.indext *.sql *.dat *.csv *.tsv *.psv)")
            selectFilePath = str(fname[0])
            fileopen = open(r'%s'%selectFilePath,'r')
            _content = str(fileopen.read())
            self.query_in.setPlainText(_content)
            self.processEvents()
        except FileNotFoundError:pass

    def save_query_to_file   (self):
        "save_query_to_file ()"
        try:
            options = QFileDialog.Options()
            saved_file,_ = QFileDialog.getSaveFileName(self,"Save SQL to file Query","Query","Query Files (*.sql);;Text Files (*.indext);;Data Files (*.dat);;All Files (*)",options=options)
            toSave_query = self.query_in.toPlainText()
            _file = open(saved_file,'w')
            _file.write(toSave_query)
            _file.close()
            self.processEvents()
        except FileNotFoundError:pass

    def export_table         (self,_w):
        """export_table (QTableWidget or QTableView)"""
        try:
            _data = ""

            maxRow = _w.rowCount()
            maxColumn = _w.columnCount()

            for hc in range(0,maxColumn):
                try: _hci = str(_w.horizontalHeaderItem(hc).text())
                except:_hci="None";pass
                if hc == (maxColumn-1) :_data += _hci
                elif hc < maxColumn:_data += "%s," % _hci

            _data += "\n"

            for r in range(0, maxRow):
                for c in range(0, maxColumn):
                    _d = str(_w.item(r, c).text())
                    if c == (maxColumn-1):_data += _d
                    elif c < maxColumn:_data += "%s," % _d
                _data += "\n"

            options = QFileDialog.Options()

            saved_file, _ = QFileDialog.getSaveFileName(self, "Save Table to file ", "data", "Plain Text (*.txt);;CSV (*.csv);;All Files (*)", options=options)
            _file = open(saved_file, 'w')
            _file.write(_data)
            _file.close()
        except FileNotFoundError:pass

    # ──────────────────────────────────────────────────────────────────────────────────────────────────────────────── # 