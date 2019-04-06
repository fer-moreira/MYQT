"""
MYQT.Connector é o modulo que gerencia como o aplicativo deve se conectar com o Servidor
e como ele deve agir depois de conectar

Atualmente o conector conta com as seguintes interfaces:

+---------------------------+----+
|Connection Type            |USE?|
+---------------------------+----+
| MYSQL Server     (TCP/IP) | OK |
| Microsoft Server (TCP/IP) | NO |
| Postgree SQL     (TCP/IP) | NO |
+---------------------------+----+
"""

from PyQt5.QtCore import  Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QMainWindow, QMessageBox)

from assets.UI.Scripts.ConnectorWindow import Ui_Connector

from Core.Manager import ManagerWindow

from Engines import MSSQL_Engine, MYSQL_Engine

from Helper.ConfigHandler import ConfigHandler
from Helper.icons_manager import b_mssql, b_mysql, b_postgreesql, win_icon

class ConnectorWindow(QMainWindow,Ui_Connector):
    def __init__(self, parent = None):
        super(ConnectorWindow,self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(win_icon))

        self.setWindowFlags(Qt.Sheet | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)

        self.dbType.setItemIcon(0,QIcon(b_mysql))
        self.dbType.setItemIcon(1,QIcon(b_mssql))
        self.dbType.setItemIcon(2,QIcon(b_postgreesql))

        self.cf = ConfigHandler(self)
        self.cf.load_config()

        self.connections = {0:'mysql',1:'mssql',2:'postgre'}

        self.show()
        self.connect.clicked.connect(self.pre_connection)

        self.check_connection_type()
        self.dbType.currentIndexChanged[int].connect(self.check_connection_type)

    def pre_connection (self):        
        if self.host_in.text() == "" or self.port_in.text() == "" or self.user_in.text() == "" or self.pass_in.text() == "":
            QMessageBox.warning(self," EMPTY FIELD ALERT!! ","Maybe you left some empty field \nPlease check and try again.",QMessageBox.Ok)
        else:self.Connect()

    def Connect (self):
        self._type      = self.connections.get(self.dbType.currentIndex())
        self._host      = self.host_in.text()
        self._port      = self.port_in.text() 
        self._user      = self.user_in.text()
        self._pass      = self.pass_in.text()
        self.buffered_c = self.buffered.isChecked()

        try:
            if self._type == 'mysql':
                MYSQL_Engine.connect(self._host,self._port,self._user,self._pass,self.buffered_c)
            if self._type == 'mssql':
                MSSQL_Engine.connect(self._host,self._user,self._pass)
            if self._type == 'postgre':
                print("POSTGRE")

            self.manager = ManagerWindow(self._host,self._port,self._user,self._pass,self.buffered_c,self._type)
            self.cf.save_config()
            self.hide()
        except Exception as error:
            QMessageBox.critical(self, "CRITICAL ERROR",str(error),QMessageBox.Ok)
            pass
    
    def check_connection_type(self):
        if self.dbType.currentIndex() == 0: 
            self.port_in.setEnabled(True)
        else: 
            self.port_in.setEnabled(False)

    def closeEvent(self,sender):
        #Your code here
        import sys
        sys.exit(0)