# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Lib\UI\LAYOUT\Console.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Console(object):
    def setupUi(self, Console):
        Console.setObjectName("Console")
        Console.resize(665, 503)
        self.canvas = QtWidgets.QWidget(Console)
        self.canvas.setObjectName("canvas")
        self.console = QtWidgets.QTextBrowser(self.canvas)
        self.console.setGeometry(QtCore.QRect(2, 2, 660, 500))
        self.console.setObjectName("console")
        Console.setCentralWidget(self.canvas)

        self.retranslateUi(Console)
        QtCore.QMetaObject.connectSlotsByName(Console)

    def retranslateUi(self, Console):
        _translate = QtCore.QCoreApplication.translate
        Console.setWindowTitle(_translate("Console", "Console"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Console = QtWidgets.QMainWindow()
    ui = Ui_Console()
    ui.setupUi(Console)
    Console.show()
    sys.exit(app.exec_())

