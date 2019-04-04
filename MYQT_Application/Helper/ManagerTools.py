from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication, QFile, Qt,QPoint
from PyQt5.QtGui import QIcon,QCursor
from PyQt5.QtWidgets import (QAction,QActionGroup,QSizePolicy, QTableWidget,QTableWidgetItem,QToolBar,QWidget)

from Helper.icons_manager import _export, _import, _newDatabase, _refresh, _run, _runSelected, _exportData,_alerts,_settings
from Helper.icons_manager import ui_data,ui_field,ui_query,win_icon

class ManagerTools (object):
    def __init__(self,w):
        self.window = w

    def SetIcons (self):
        self.window.setWindowIcon(QIcon(win_icon))
        self.window.tabs.setTabIcon(0,QIcon(ui_data))
        self.window.tabs.setTabIcon(1,QIcon(ui_field))
        self.window.tabs.setTabIcon(2,QIcon(ui_query))

    def AddVerticalToolbar (self):
        """ADD TOOLBAR AND TOOLBAR ICONS HANDLER"""
        toolBar = QToolBar()
        toolBar.setMovable(False)
        toolBar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.window.addToolBar(Qt.LeftToolBarArea,toolBar)

        _spacer = QWidget()
        _spacer.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Expanding)        

        toolBar.addAction(QAction(QIcon(_refresh)    ,"Refresh"          ,self.window,shortcut="F5"           ,triggered=self.window.refresh_database))
        toolBar.addAction(QAction(QIcon(_run)        ,"Compile all"      ,self.window,shortcut="F9"           ,triggered=self.window.execute_all_query))
        toolBar.addAction(QAction(QIcon(_runSelected),"Compile Selected" ,self.window,shortcut="F10"          ,triggered=self.window.execute_selected_query))
        toolBar.addAction(QAction(QIcon(_import)     ,"Load query"       ,self.window,shortcut="Ctrl+I"       ,triggered=self.window.load_query_from_file))
        toolBar.addAction(QAction(QIcon(_export)     ,"Save query"       ,self.window,shortcut="Ctrl+E"       ,triggered=self.window.save_query_to_file))
        toolBar.addAction(QAction(QIcon(_newDatabase),"Create Database"  ,self.window,shortcut="Shift+Ctrl+F7",triggered=self.window.create_database_wizard))
        toolBar.addAction(QAction(QIcon(_exportData) ,"Export Data"      ,self.window,shortcut="Shift+Ctrl+F6",triggered=lambda:self.window.export_table(self.window.result_out)))

        toolBar.addWidget(_spacer)

        toolBar.addAction(QAction(QIcon(_alerts)     ,"Open Alerts"      ,self.window,shortcut="Shift+Ctrl+F4",triggered=self.window.openChanger))
        toolBar.addAction(QAction(QIcon(_settings)   ,"Open Settings"    ,self.window,shortcut="Shift+Ctrl+F5",triggered=self.window.openChanger))
        
        self.window.processEvents()