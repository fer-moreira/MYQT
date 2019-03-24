# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\assets\UI\Layout\PlotVisualizer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlotView(object):
    def setupUi(self, PlotView):
        PlotView.setObjectName("PlotView")
        PlotView.setWindowModality(QtCore.Qt.ApplicationModal)
        PlotView.resize(349, 208)
        self.centralwidget = QtWidgets.QWidget(PlotView)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(331, 190))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setMinimumSize(QtCore.QSize(310, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setMinimumSize(QtCore.QSize(180, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setMinimumSize(QtCore.QSize(310, 60))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        PlotView.setCentralWidget(self.centralwidget)

        self.retranslateUi(PlotView)
        QtCore.QMetaObject.connectSlotsByName(PlotView)

    def retranslateUi(self, PlotView):
        _translate = QtCore.QCoreApplication.translate
        PlotView.setWindowTitle(_translate("PlotView", "Plot visualizer"))
        self.groupBox.setTitle(_translate("PlotView", "Plot visualizer settings"))
        self.lineEdit.setPlaceholderText(_translate("PlotView", "Enter title:"))
        self.label.setText(_translate("PlotView", "Plot Type:"))
        self.comboBox.setItemText(0, _translate("PlotView", "Vertical Bar"))
        self.comboBox.setItemText(1, _translate("PlotView", "Horizontal Bar"))
        self.comboBox.setItemText(2, _translate("PlotView", "Pizza"))
        self.comboBox.setItemText(3, _translate("PlotView", "Histogram"))
        self.comboBox.setItemText(4, _translate("PlotView", "Paths"))
        self.comboBox.setItemText(5, _translate("PlotView", "Stream Plot"))
        self.pushButton.setText(_translate("PlotView", "GENERATE PLOT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PlotView = QtWidgets.QMainWindow()
    ui = Ui_PlotView()
    ui.setupUi(PlotView)
    PlotView.show()
    sys.exit(app.exec_())

