# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Lib\UI\LAYOUT\ConnectorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Connector(object):
    def setupUi(self, Connector):
        Connector.setObjectName("Connector")
        Connector.resize(286, 243)
        self.centralwidget = QtWidgets.QWidget(Connector)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(14, 0, 260, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.Connect_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Connect_btn.setEnabled(True)
        self.Connect_btn.setGeometry(QtCore.QRect(14, 140, 260, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Connect_btn.setFont(font)
        self.Connect_btn.setObjectName("Connect_btn")
        self.host_in = QtWidgets.QLineEdit(self.centralwidget)
        self.host_in.setGeometry(QtCore.QRect(14, 50, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.host_in.setFont(font)
        self.host_in.setFrame(True)
        self.host_in.setAlignment(QtCore.Qt.AlignCenter)
        self.host_in.setClearButtonEnabled(True)
        self.host_in.setObjectName("host_in")
        self.user_in = QtWidgets.QLineEdit(self.centralwidget)
        self.user_in.setGeometry(QtCore.QRect(14, 100, 90, 30))
        self.user_in.setClearButtonEnabled(True)
        self.user_in.setObjectName("user_in")
        self.pass_in = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_in.setGeometry(QtCore.QRect(114, 100, 90, 30))
        self.pass_in.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.pass_in.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.pass_in.setClearButtonEnabled(True)
        self.pass_in.setObjectName("pass_in")
        self.buffered = QtWidgets.QCheckBox(self.centralwidget)
        self.buffered.setEnabled(True)
        self.buffered.setGeometry(QtCore.QRect(214, 100, 80, 30))
        self.buffered.setStyleSheet("")
        self.buffered.setCheckable(True)
        self.buffered.setChecked(True)
        self.buffered.setAutoRepeat(False)
        self.buffered.setAutoExclusive(False)
        self.buffered.setTristate(False)
        self.buffered.setObjectName("buffered")
        self.port_in = QtWidgets.QLineEdit(self.centralwidget)
        self.port_in.setGeometry(QtCore.QRect(170, 50, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.port_in.setFont(font)
        self.port_in.setFrame(True)
        self.port_in.setAlignment(QtCore.Qt.AlignCenter)
        self.port_in.setClearButtonEnabled(True)
        self.port_in.setObjectName("port_in")
        self.console_out = QtWidgets.QTextBrowser(self.centralwidget)
        self.console_out.setGeometry(QtCore.QRect(-1, 205, 286, 40))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.console_out.setFont(font)
        self.console_out.setObjectName("console_out")
        Connector.setCentralWidget(self.centralwidget)

        self.retranslateUi(Connector)
        QtCore.QMetaObject.connectSlotsByName(Connector)

    def retranslateUi(self, Connector):
        _translate = QtCore.QCoreApplication.translate
        Connector.setWindowTitle(_translate("Connector", "SQL CONNECTOR"))
        self.title.setText(_translate("Connector", "SQL MANAGER"))
        self.Connect_btn.setText(_translate("Connector", "CONNECT"))
        self.host_in.setText(_translate("Connector", "127.0.0.1"))
        self.host_in.setPlaceholderText(_translate("Connector", "Host:"))
        self.user_in.setText(_translate("Connector", "root"))
        self.user_in.setPlaceholderText(_translate("Connector", "User:"))
        self.pass_in.setText(_translate("Connector", "123456"))
        self.pass_in.setPlaceholderText(_translate("Connector", "Password:"))
        self.buffered.setText(_translate("Connector", "Buffered"))
        self.port_in.setText(_translate("Connector", "3306"))
        self.port_in.setPlaceholderText(_translate("Connector", "Port:"))
        self.console_out.setHtml(_translate("Connector", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Connector = QtWidgets.QMainWindow()
    ui = Ui_Connector()
    ui.setupUi(Connector)
    Connector.show()
    sys.exit(app.exec_())

