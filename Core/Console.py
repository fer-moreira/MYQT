import mysql.connector as mysql
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox,QFileDialog

from assets.UI.Scripts.Console import Ui_Canvas

class Console(QMainWindow,Ui_Canvas):
    def __init__(self, parent = None):
        super(Console,self).__init__(parent)
        self.setupUi(self)
        self.show()

        self.export_2.clicked.connect(self.export_log)

    def export_log (self):    
        try:
            options = QFileDialog.Options()
            saved_file,_ = QFileDialog.getSaveFileName(self,"Save LOG File","log","Text file (*.txt);;Others files (*.indext);;Data Files (*.dat);;All Files (*)",options=options)            
            toSave_query = self.console.toPlainText()
            _file = open(saved_file,'w')
            _file.write(toSave_query)
            _file.close()
        except FileNotFoundError:pass