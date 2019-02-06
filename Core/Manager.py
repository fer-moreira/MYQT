## SIMPLE MODULES ##+
import time
import sys
import xlrd
####################+

######### MYSQL MODULE #########+
import mysql.connector as mysql
################################+

################### PYQT MODULES ###############################################################+
from PyQt5              import QtCore,QtWidgets
from PyQt5.QtGui        import QStandardItemModel,QStandardItem
from PyQt5.QtWidgets    import (QApplication, QDialog,QFileDialog,QMainWindow,QStyleFactory,QWidget,QSizePolicy
,QMenu,qApp,QAction,QToolBar,QTableWidget,QTableWidgetItem,QHeaderView,QTreeWidgetItem)
from PyQt5.QtCore       import pyqtSlot,QFile, QTextStream,QCoreApplication,Qt
from PyQt5.QtGui        import QIcon
################################################################################################+

## INTERFACE MODULES ########################################################################################+
from assets.UI.Scripts.MainWindow   import Ui_SQLMANAGER
from Lib.icons_manager       import (_run,_runSelected,_import,_export,_refresh,_newDatabase,_newTable,ui_db,ui_tb,ico_consult)
from Core.Database_creator import DBCreator
############################################################################################################+

from functools          import partial

class ManagerWindow(QMainWindow,QToolBar,QTreeWidgetItem,QCoreApplication,QWidget,Ui_SQLMANAGER,object):
    def __init__(self,hs,pt,us,ps,bfr, parent = None):
        super(ManagerWindow,self).__init__(parent)
        self.setupUi(self)
        self.add_tool_bar()
        self.setWindowIcon(QIcon(ico_consult))
        self.show()

        self.hs = hs
        self.pt = pt
        self.us = us
        self.ps = ps
        self.bfred = bfr

        try:
            self.mydb = mysql.connect(host=self.hs,port=self.pt,user=self.us,passwd=self.ps,buffered=self.bfred)
            self.Get_Databases()
            self.WriteConsole('<b>Connected to SQL Server</b>',True)
        except:
            self.WriteConsole('<p style="color:rgb(175, 50, 50);">Cannot Connect to SQL Server</span>',True)

        self.tables_out.itemDoubleClicked.connect(self.ItemDoubleClicked)
        self.openConsole.clicked.connect(self.ExpandConsoleWindow)

        self.openedConsole = False

    def ItemDoubleClicked   (self):                 ## SINGLE CLICK HANDLER FOR QTreeWIDGET 
        index = self.tables_out.currentIndex()
        data =  self.tables_out.model().data(index)
        text = str(data)
        if text in self.databases and text != str(self.mydb.database):
            lastDb = self.mydb.database
            self.mydb.database = text
            nowDb = self.mydb.database
            if lastDb != nowDb and lastDb != "None":
                self.tables_out.clear()
                self.Get_Databases()
                self.Get_Tables(nowDb)
        if text not in self.databases:
            self.Get_CreateCode(text)
            self.Get_Desc(text)
            self.Get_All_Data(text)
        self.processEvents()
    def Execute_Querry      (self,text):            ## MASTER HANDLER FOR EXECUTE ANY QUERY AND RETURN ALL RESULTS  
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
            self.WriteConsole("%s"%_query.lower(),False)
            self.processEvents()
        except Exception as error:
            self.WriteConsole(error,True)
            pass
    def GetAllQuery         (self):                 # EXECUTE ALL QUERY TEXT    
        _allQuery = str(self.query_in.toPlainText()).replace("\n"," ")
        self.Execute_Querry(_allQuery)
        self.processEvents()
    def GetSelectedQuery    (self):                 # EXECUTE ONLY SELECTED QUERY TEXT 
        cursor = self.query_in.textCursor()
        _allText = str(self.query_in.toPlainText()).replace("\n"," ")
        _startIndex = cursor.selectionStart()
        _endIndex = cursor.selectionEnd()
        _buildText = ""
        for letter in range(_startIndex,_endIndex):
            _buildText+=_allText[letter]
        self.Execute_Querry(_buildText)
        self.processEvents()
    def Get_Databases       (self):                 # GET ALL DATABASES IN SERVER AND RETURN AS PARENT TO QTREEVIEW 
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
            self.WriteConsole("SHOW DATABASES",False)
        except Exception as error:
            self.WriteConsole(error,True)
            pass
    def Get_Tables          (self,_cDb):            # GET ALL TABLES FROM DATABASE AND RETURN IN TREE VIEW AS CHILD OF DATABASE PARENT ITEM 
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
        self.WriteConsole("SHOW TABLES",False)
    def Get_CreateCode      (self,data):
        table = str(data)
        _query = "show create table %s" %table
        try:
            self.create_in.setPlainText('')
            cursor = self.mydb.cursor()
            cursor.execute(_query)
            allSQLRows = cursor.fetchall()
            code_create = str(allSQLRows[0][1])
            schemeCode = self.SchemeColorText(code_create)
            self.create_in.appendHtml(schemeCode)
            self.WriteConsole("%s"%str(_query),False)
        except Exception as error:
            self.WriteConsole(error,True)
            print(error)
    def Get_Desc            (self,data):            # GET ALL TABLES DESCRITIONS    
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
            self.WriteConsole(error,True)
            pass    
    def Get_All_Data        (self,data):            # GET ALL DATA FROM TABLES      
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
            self.WriteConsole(error,True)
            pass
    def load_query_from_file(self):                 # OPEN DIALOG BOX TO LOAD FILE  
        try:
            fname = QFileDialog.getOpenFileName(self, 'Load SQL From file', 'Query',"Select query file (*.indext *.sql *.dat *.csv *.tsv *.psv)")
            selectFilePath = str(fname[0])
            fileopen = open(r'%s'%selectFilePath,'r')
            _content = str(fileopen.read())
            self.query_in.setPlainText(_content)
            self.processEvents()
        except FileNotFoundError:pass
    def save_query_to_file  (self):                 # OPEN DIALOG BOX TO SAVE QUERY TEXT TO FILE    
        try:
            options = QFileDialog.Options()
            saved_file,_ = QFileDialog.getSaveFileName(self,"Save SQL to file Query","Query","Query Files (*.sql);;Text Files (*.indext);;Data Files (*.dat);;All Files (*)",options=options)            
            toSave_query = self.query_in.toPlainText()
            _file = open(saved_file,'w')
            _file.write(toSave_query)
            _file.close()
            self.processEvents()
        except FileNotFoundError:pass

    def createDatabae (self):
        print("NEW DATABASE")

    def createTable (self):
        self.tableCreator = DBCreator()

    def add_tool_bar        (self):                 # ADD TOOLBAR AND TOOLBAR ICONS HANDLER 
        toolBar = QToolBar()
        toolBar.setMovable(False)
        toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        spacer_a = QWidget() #SPACER LEFT
        spacer_b = QWidget() #SPACER RIGHT
        spacer_a.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Preferred)
        spacer_b.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Preferred)
        tb_config = self.addToolBar(Qt.TopToolBarArea,toolBar)

        refresh_t       = QAction(QIcon(_refresh),    "REFRESH",self,shortcut="F5",           triggered=self.Get_Databases)
        compileAll      = QAction(QIcon(_run),        "COMPILE",self,shortcut="F9",           triggered=self.GetAllQuery)
        import_t        = QAction(QIcon(_import),     " IMPORT",self,shortcut="Ctrl+O",       triggered=self.load_query_from_file)
        export_t        = QAction(QIcon(_export),     " EXPORT",self,shortcut="Ctrl+S",       triggered=self.save_query_to_file)
        compileSelected = QAction(QIcon(_runSelected),"RUN  SL",self,shortcut="Shift+Ctrl+F9",triggered=self.GetSelectedQuery)
        newDatabase     = QAction(QIcon(_newDatabase),"NEW  DB",self,                         triggered=self.createDatabae)
        newTable     = QAction(QIcon(_newTable)      ,"NEW  TB",self,                         triggered=self.createTable)

        refresh_t.setToolTip        ("Refresh Server (F5)")
        import_t.setToolTip         ("Load SQL (Ctrl+O)")
        export_t.setToolTip         ("Save SQL (Ctrl+S)")
        compileAll.setToolTip       ("Run All QUERY (F9)")
        compileSelected.setToolTip  ("Run Selected QUERY (Shift+Ctrl+F9)")
        newDatabase.setToolTip      ("Open DATABASE CREATOR")
        newTable.setToolTip         ("Open TABLE CREATOR")

        toolBar.addWidget(spacer_a),toolBar.addSeparator()
        toolBar.addAction(refresh_t)
        toolBar.addSeparator(),toolBar.addAction(import_t),toolBar.addAction(export_t)
        toolBar.addSeparator(),toolBar.addAction(compileAll),toolBar.addAction(compileSelected)
        toolBar.addSeparator(),toolBar.addAction(newDatabase),toolBar.addAction(newTable)
        toolBar.addSeparator(),toolBar.addWidget(spacer_b)
        
        self.processEvents()

    def WriteConsole        (self,text,isError):    # DEBUG ALL STATE TO CONSOLE    
        if isError == False:
            coloredText = self.SchemeColorText(text)
            self.console_out.appendHtml(coloredText)
            self.processEvents()
        else:
            errorPat = '<p style="color:rgb(175, 50, 50);">{0}</span>'
            self.console_out.appendHtml(errorPat.format(str(text)))
            self.processEvents()
    def ExpandConsoleWindow (self):                 # EXPAND CONSOLE WINDOW 
        self.openedConsole = not self.openedConsole
        if self.openedConsole == True:
            self.console_out.setGeometry(10,9,1000,721)
            self.openConsole.setText("C\nL\nO\nS\nE")
        else:
            self.console_out.setGeometry(10,650,1000,80)
            self.console_out.verticalScrollBar().setValue(self.console_out.verticalScrollBar().maximum())
            self.openConsole.setText("O\nP\nE\nN")
    def SchemeColorText (self,text):                # ADD COLOR TO SQL CODE 
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
    def contextMenuEvent(self, event):              # CUSTOM CONTEXT MENU   
        cmenu = QMenu(self)
        newDB = cmenu.addAction("New Database")
        cmenu.addSeparator()
        saveSQL = cmenu.addAction("Save SQL")
        loadSQL = cmenu.addAction("Load SQL")
        cmenu.addSeparator()
        expTable = cmenu.addAction("Export Table")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
