from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication, QFile, Qt,QPoint
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QAction,QSizePolicy,QToolBar,QWidget

from Helper.IconsHandler import _export, _import, _refresh, _run, _runSelected, _exportData,_themeSwitch,_alerts,_settings
from Helper.IconsHandler import ui_data,ui_field,ui_query,win_icon
from Helper.ConfigHandler import ConfigHandler

class ManagerTools (object):
    def __init__(self,w):
        """ ManagerTools (Window) """ 
        self.window = w
        self.cf = ConfigHandler(self)
        self.themeIsDark = self.cf.themeIsDark()

    def SetIcons (self):
        """ SetIcons () Set window tabs icon """
        self.window.setWindowIcon(QIcon(win_icon))
        self.window.tabs.setTabIcon(0,QIcon(ui_data))
        self.window.tabs.setTabIcon(1,QIcon(ui_field))
        self.window.tabs.setTabIcon(2,QIcon(ui_query))

    def AddVerticalToolbar (self):
        """ AddVerticalToolbar() """
        toolBar = QToolBar()

        toolBar.setMovable(False)
        toolBar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        # toolBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.window.addToolBar(Qt.LeftToolBarArea,toolBar)

        _spacer = QWidget()
        _spacer.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Expanding)        

        toolBar.addAction(QAction(QIcon(_refresh)    ,"Refresh"          ,self.window,shortcut="F5"           ,triggered=self.window.refresh_database))
        toolBar.addAction(QAction(QIcon(_run)        ,"Compile all"      ,self.window,shortcut="F9"           ,triggered=self.window.execute_all_query))
        toolBar.addAction(QAction(QIcon(_runSelected),"Compile Selected" ,self.window,shortcut="F10"          ,triggered=self.window.execute_selected_query))
        toolBar.addAction(QAction(QIcon(_import)     ,"Load query"       ,self.window,shortcut="Ctrl+I"       ,triggered=self.window.load_query_from_file))
        toolBar.addAction(QAction(QIcon(_export)     ,"Save query"       ,self.window,shortcut="Ctrl+E"       ,triggered=self.window.save_query_to_file))
        toolBar.addAction(QAction(QIcon(_exportData) ,"Export Data"      ,self.window                         ,triggered=lambda:self.window.export_table(self.window.result_out)))

        toolBar.addWidget(_spacer)

        toolBar.addAction(QAction(QIcon(_themeSwitch),"Change theme"     ,self.window,triggered=self.flipTheme))
        toolBar.addAction(QAction(QIcon(_alerts)     ,"Open Alerts"      ,self.window))
        toolBar.addAction(QAction(QIcon(_settings)   ,"Open Settings"    ,self.window))
        
        self.window.processEvents()

    def flipTheme (self):
        """ flipTheme () """
        self.themeIsDark = not self.themeIsDark

        white = str(open(r'assets\css\Style_White.css','r').read())
        dark  = str(open(r'assets\css\Style_Dark.css','r').read())

        if self.themeIsDark == True: self.window.setStyleSheet(dark)
        else:                        self.window.setStyleSheet(white)

        self.cf.save_theme(self.themeIsDark)