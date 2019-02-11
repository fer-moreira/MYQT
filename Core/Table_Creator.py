import mysql.connector as mysql
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox

from assets.UI.Scripts.TB_Creator import Ui_Creator

class TBCreator(QMainWindow,Ui_Creator):
    def __init__(self,db,hs,pt,us,ps,bfr, parent = None):
        super(TBCreator,self).__init__(parent)
        self.setupUi(self)
        self.show()

        self.db = db
        self.hs = hs
        self.pt = pt
        self.us = us
        self.ps = ps
        self.bfred = bfr
        self.mydb = mysql.connect(database=self.db,host=self.hs,port=self.pt,user=self.us,passwd=self.ps,buffered=self.bfred)
    
        self._content = ""
        self._fieldDicts = {}

        try:
            self.create.clicked.connect(self.get_content)
        except Exception as error:
            self.application_error(error)


    def get_content (self):
        code_pattern = '''`{field_name}` {data_type}{data_scale} {unsigned} {zerofill} {useNull} {pattern_increment} {comment}  {collection} COMMA_POINTER'''

        _tableName  = str(self.table_name.text())
        _fieldName  = str(self.field_name.text())
        _dataType   = str(self.databox.currentText()).replace(" ","")
        if not(self.datavalue.text() == ''):_dataValue = str("(%s)"%self.datavalue.text()).replace(" ","")
        else:_dataValue = ''

        if self.unsigned_2.isChecked():_unsigned = "UNSIGNED"
        else:_unsigned = ''
        
        if self.allownull.isChecked():_allownull  = "NULL"
        else:_allownull  = "NOT NULL"
        
        if self.zerofill.isChecked(): _zerofill = "ZEROFILL" 
        else: _zerofill = ''
        
        if not (str(self.pattern_combo.currentText()) == 'NO DEFAULT VALUE'):_pattern = str(self.pattern_combo.currentText())
        else: _pattern = ''

        if not(self.f_collection.text() == ''):_collection = str("COLLATE '%s'"%self.f_collection.text())
        else:_collection=''

        if not(self.f_comment.text() == ''):_comment = str("COMMENT '%s'"%self.f_comment.text())
        else:_comment = ''

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

        self._fieldDicts[_fieldName] = final_code

        for patKey in self._fieldDicts:
            _piece = self._fieldDicts.get(patKey)
            pass

        lastKeyID = int(len(self._fieldDicts)-1)
        lastKey = list(self._fieldDicts)[lastKeyID]

        _content_pattern = '''CREATE TABLE `{tb_name}` (\n{content}\n)\nCHARSET=UTF8\nENGINE=InnoDB\n;'''
        _content = ""

        for key in self._fieldDicts:
            if key == lastKey:_query = self._fieldDicts.get(key).replace("COMMA_POINTER","")
            else:_query = self._fieldDicts.get(key).replace("COMMA_POINTER",",")
            _content += "%s\n"%_query
        
        final_createTable = _content_pattern.format(tb_name=_tableName,content=_content)

        self.code_preview.setPlainText(final_createTable)

    def execute_create_code (self):
        sql_query = str(self.code_preview.ToPlainText())

        self.cursor = self.mydb.cursor()
        self.cursor.execute(sql_query)

    def application_error    (self,error):
        print(error)
        reply = QMessageBox.critical(self, "ERROR",str(error),QMessageBox.Ok)
