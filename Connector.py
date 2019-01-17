import sys
import mysql.connector as mysql

from PyQt5.QtCore import pyqtSlot,QFile, QTextStream
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow,QStyleFactory,QAction,QMenu
from PyQt5.uic import loadUi
from PyQt5 import QtGui

from Core.Manager import ManagerWindow
from Lib.UI.SCRIPT.ConnectorWindow import Ui_Connector

from Lib.icons_manager import ico_connector

app = QApplication(sys.argv)
app.processEvents()

_style = str(open(r'Lib\Style.css','r').read())
app.setStyleSheet(_style)

class MainWindow(QMainWindow,Ui_Connector):
    def __init__(self, parent = None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())        
        self.setWindowIcon(QtGui.QIcon(ico_connector))

        self.show()

        self.Connect_btn.clicked.connect(self.Connect)

    def Connect (self):
        self._host = self.host_in.displayText()
        self._port = self.port_in.displayText() 
        self._user = self.user_in.displayText()
        self._pass = self.pass_in.displayText()
        self.buffered_c = self.buffered.isChecked()

        
        try:
            mydb = mysql.connect(
            host=self._host,
            port=self._port,
            user=self._user,passwd=self._pass,
            buffered=self.buffered_c
            )

            self.manager = ManagerWindow(self._host,self._port,self._user,self._pass,self.buffered_c)
            self.close()
        
        except Exception as error:
            # self.console_out.appendHtml("%s"%error)
            
            print(error)
            pass
    

Main_GUI = MainWindow()
sys.exit(app.exec_())