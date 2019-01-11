import sys
from PyQt5.QtCore import pyqtSlot,QFile, QTextStream
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow,QTreeWidget,QTreeView,QTreeWidgetItem,QTreeWidgetItemIterator
from PyQt5.uic import loadUi
from PyQt5 import QtGui

from Lib.UI.SCRIPT.Teste_ui import Ui_Form

app = QApplication(sys.argv)
app.processEvents()



class MainWindow(QMainWindow,QTreeWidgetItem,Ui_Form):
    def __init__(self, parent = None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())        
        self.show()

        dbTbs = {
            "sakila":['a','b','c'],
            "dbbi01":['aa','bb','cc'],
            "menagerie":['aaa','bbb','ccc']
        }

        for db in dbTbs:
            parent = QTreeWidgetItem(self.widget)
            parent.setText(0,str(db))
            parent.setFlags(parent.flags())

            for table in dbTbs.get(db):
                child = QTreeWidgetItem(parent)
                child.setFlags(child.flags())
                child.setText(0,str(table))

Main_GUI = MainWindow()
sys.exit(app.exec_())