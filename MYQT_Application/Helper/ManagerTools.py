from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication, QFile, Qt,QPoint
from PyQt5.QtGui import QIcon,QCursor
from PyQt5.QtWidgets import (QAction,QSizePolicy, QTableWidget,QTableWidgetItem,QToolBar,QWidget)

from Helper.icons_manager import _export, _import, _newDatabase, _refresh, _run, _runSelected, _exportData,_settings

class ManagerTools (object):
    def __init__(self,w):
        self.window = w

    def AddVerticalToolbar (self):
        """ADD TOOLBAR AND TOOLBAR ICONS HANDLER"""
        toolBar = QToolBar()
        toolBar.setMovable(False)
        toolBar.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.window.addToolBar(Qt.LeftToolBarArea,toolBar)

        refresh_t       = QAction(QIcon(_refresh),    "REFRESH" ,self.window,shortcut="F5",           triggered=self.window.refresh_database)
        compileAll      = QAction(QIcon(_run),        "COMPILE" ,self.window,shortcut="F9",           triggered=self.window.execute_all_query)
        import_t        = QAction(QIcon(_import),     "IMPORT"  ,self.window,shortcut="Ctrl+O",       triggered=self.window.load_query_from_file)
        export_t        = QAction(QIcon(_export),     "EXPORT"  ,self.window,shortcut="Ctrl+S",       triggered=self.window.save_query_to_file)
        compileSelected = QAction(QIcon(_runSelected),"RUN SL"  ,self.window,shortcut="Shift+Ctrl+F9",triggered=self.window.execute_selected_query)
        newDatabase     = QAction(QIcon(_newDatabase),"NEW DB"  ,self.window,                         triggered=self.window.create_database_wizard)
        exportData      = QAction(QIcon(_exportData) ,"EXPORT"  ,self.window,                         triggered=lambda:self.window.export_table(self.window.result_out))
        settings        = QAction(QIcon(_settings),   "SETTINGS",self.window,                         triggered=self.window.openChanger)


        refresh_t.setToolTip        ("Refresh all server databases and table (F5)")
        import_t.setToolTip         ("Load SQL (Ctrl+O)")
        export_t.setToolTip         ("Save SQL (Ctrl+S)")
        compileAll.setToolTip       ("Run all query (F9)")
        compileSelected.setToolTip  ("Run selected query (Shift+Ctrl+F9)")
        newDatabase.setToolTip      ("Open database creator")
        exportData.setToolTip       ("Export all data from result table")
        settings.setToolTip         ("View settings")

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
        
        self.window.processEvents()