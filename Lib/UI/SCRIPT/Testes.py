# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Lib\UI\LAYOUT\Testes.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Testes(object):
    def setupUi(self, Testes):
        Testes.setObjectName("Testes")
        Testes.resize(547, 466)
        self.centralwidget = QtWidgets.QWidget(Testes)
        self.centralwidget.setObjectName("centralwidget")
        Testes.setCentralWidget(self.centralwidget)

        self.retranslateUi(Testes)
        QtCore.QMetaObject.connectSlotsByName(Testes)

    def retranslateUi(self, Testes):
        _translate = QtCore.QCoreApplication.translate
        Testes.setWindowTitle(_translate("Testes", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Testes = QtWidgets.QMainWindow()
    ui = Ui_Testes()
    ui.setupUi(Testes)
    Testes.show()
    sys.exit(app.exec_())

