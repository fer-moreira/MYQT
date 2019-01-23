from PyQt5.QtCore import pyqtSlot,QFile, QTextStream
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow,QStyleFactory,QAction,QMenu
from PyQt5.uic import loadUi
from PyQt5 import QtGui

from Lib.UI.SCRIPT.ErrorPopup import Ui_Error

class PopupWindow(QMainWindow,Ui_Error):
    def __init__(self, _log,parent = None):
        super(PopupWindow,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())        

        self._log = _log

        self.console_out.setText(self._log)

        self.ok.clicked.connect(self.close)

        self.show()
