# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\assets\UI\Layout\Console.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Canvas(object):
    def setupUi(self, Canvas):
        Canvas.setObjectName("Canvas")
        Canvas.setWindowModality(QtCore.Qt.ApplicationModal)
        Canvas.resize(462, 537)
        self.GRID = QtWidgets.QWidget(Canvas)
        self.GRID.setObjectName("GRID")
        self.gridLayout = QtWidgets.QGridLayout(self.GRID)
        self.gridLayout.setObjectName("gridLayout")
        self.console = QtWidgets.QPlainTextEdit(self.GRID)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.console.setFont(font)
        self.console.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.console.setFrameShadow(QtWidgets.QFrame.Plain)
        self.console.setUndoRedoEnabled(False)
        self.console.setReadOnly(False)
        self.console.setPlainText("")
        self.console.setObjectName("console")
        self.gridLayout.addWidget(self.console, 0, 0, 1, 1)
        self.export_2 = QtWidgets.QPushButton(self.GRID)
        self.export_2.setMinimumSize(QtCore.QSize(0, 40))
        self.export_2.setObjectName("export_2")
        self.gridLayout.addWidget(self.export_2, 1, 0, 1, 1)
        Canvas.setCentralWidget(self.GRID)

        self.retranslateUi(Canvas)
        QtCore.QMetaObject.connectSlotsByName(Canvas)
        Canvas.setTabOrder(self.console, self.export_2)

    def retranslateUi(self, Canvas):
        _translate = QtCore.QCoreApplication.translate
        Canvas.setWindowTitle(_translate("Canvas", "CONSOLE"))
        self.export_2.setText(_translate("Canvas", "EXPORT LOG"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Canvas = QtWidgets.QMainWindow()
    ui = Ui_Canvas()
    ui.setupUi(Canvas)
    Canvas.show()
    sys.exit(app.exec_())
