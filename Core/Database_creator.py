from PyQt5.QtCore import pyqtSlot,QFile, QTextStream
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow,QStyleFactory,QAction,QMenu
from PyQt5.uic import loadUi
from PyQt5 import QtGui

from assets.UI.Scripts.DB_Creator import Ui_Creator

class DBCreatpr(QMainWindow,Ui_Creator):
    def __init__(self, _log,parent = None):
        super(DBCreatpr,self).__init__(parent)
        self.setupUi(self)
        self.show()

'''

CREATE TABLE {tb_name} (
{content}
)
COLLATE='utf8_general_ci
;

{field_name} {data_tipe}({data_scale}) {unsigned} {zerofill} {useNull} {pattern_increment} COMMENT '{comment}' COLLATE '{collection}'

'''