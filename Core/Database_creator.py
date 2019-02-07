######### MYSQL MODULE #########+
import mysql.connector as mysql
################################+

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow,QMenu
from PyQt5 import QtGui

from assets.UI.Scripts.DB_Creator import Ui_Creator

class DBCreator(QMainWindow,Ui_Creator):
    def __init__(self,db,hs,pt,us,ps,bfr, parent = None):
        super(DBCreator,self).__init__(parent)
        self.setupUi(self)
        self.show()


        self.db = db,self.hs = hs,self.pt = pt,self.us = us,self.ps = ps,self.bfred = bfr
        self.mydb = mysql.connect(database=self.db,host=self.hs,port=self.pt,user=self.us,passwd=self.ps,buffered=self.bfred)


        self._content   = ""
        self._fieldDict = {}

        self.create.clicked.connect(self.get_content)

    def get_content (self):
        code_pattern = ''',{field_name} {data_type}({data_scale}) {unsigned} {zerofill} {useNull} {pattern_increment} COMMENT '{comment}' COLLATE '{collection}'''

        _tableName  = str(self.table_name.text())
        _fieldName  = str(self.field_name.text())
        _dataType   = str(self.databox.currentText())
        _dataValue  = str(self.datavalue.text())

        if self.unsigned_2.isChecked():_unsigned = "UNSIGNED"
        else:_unsigned = ""
        
        if self.allownull.isChecked():_allownull  = "NULL"
        else:_allownull  = "NOT NULL"
        
        if self.zerofill.isChecked(): _zerofill = "ZEROFILL" 
        else: _zerofill = ""
        
        _pattern    = str(self.pattern_combo.currentText())
        _comment    = str(self.f_comment.text())
        _collection = str(self.f_collection.text())

        final_code = code_pattern.format(
        field_name=_fieldName,
        data_type=_dataType,
        data_scale=_dataValue,
        unsigned=_unsigned,
        zerofill=_zerofill,
        useNull=_allownull,
        pattern_increment=_pattern,
        comment=_comment,
        collection=_collection)
        
        self._content += "%s\n" %final_code

        _queryPattern = '''CREATE TABLE {tb_name} (\n{content}\n)\nCOLLATE='utf8_general_ci\n;'''
        final_query = _queryPattern.format(tb_name=_tableName,content=self._content).replace("(\n,","(\n")

        self.code_preview.setPlainText(final_query)

        self._fieldDict

    def execute_create_code (self):
        sql_query = str(self.code_preview.ToPlainText())

        self.cursor = self.mydb.cursor()
        self.cursor.execute(sql_query)
