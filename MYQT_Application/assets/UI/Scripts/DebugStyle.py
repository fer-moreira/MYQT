# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\assets\UI\Layout\debug_style.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Stylechanger(object):
    def setupUi(self, Stylechanger):
        Stylechanger.setObjectName("Stylechanger")
        Stylechanger.setWindowModality(QtCore.Qt.ApplicationModal)
        Stylechanger.resize(575, 485)
        self.canvas = QtWidgets.QWidget(Stylechanger)
        self.canvas.setObjectName("canvas")
        self.gridLayout = QtWidgets.QGridLayout(self.canvas)
        self.gridLayout.setObjectName("gridLayout")
        self.input = QtWidgets.QPlainTextEdit(self.canvas)
        self.input.setObjectName("input")
        self.gridLayout.addWidget(self.input, 0, 0, 1, 1)
        self.apply = QtWidgets.QPushButton(self.canvas)
        self.apply.setMinimumSize(QtCore.QSize(0, 60))
        self.apply.setMaximumSize(QtCore.QSize(16777215, 60))
        self.apply.setObjectName("apply")
        self.gridLayout.addWidget(self.apply, 1, 0, 1, 1)
        Stylechanger.setCentralWidget(self.canvas)

        self.retranslateUi(Stylechanger)
        QtCore.QMetaObject.connectSlotsByName(Stylechanger)

    def retranslateUi(self, Stylechanger):
        _translate = QtCore.QCoreApplication.translate
        Stylechanger.setWindowTitle(_translate("Stylechanger", "Style Changer"))
        self.apply.setText(_translate("Stylechanger", "APPLY"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Stylechanger = QtWidgets.QMainWindow()
    ui = Ui_Stylechanger()
    ui.setupUi(Stylechanger)
    Stylechanger.show()
    sys.exit(app.exec_())
