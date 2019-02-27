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
        PlotView.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(PlotView)
        self.centralwidget.setObjectName("centralwidget")
        self.graphics = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphics.setGeometry(QtCore.QRect(10, 10, 781, 581))
        self.graphics.setObjectName("graphics")
        PlotView.setCentralWidget(self.centralwidget)

        self.retranslateUi(PlotView)
        QtCore.QMetaObject.connectSlotsByName(PlotView)

    def retranslateUi(self, PlotView):
        _translate = QtCore.QCoreApplication.translate
        PlotView.setWindowTitle(_translate("PlotView", "Plot visualizer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PlotView = QtWidgets.QMainWindow()
    ui = Ui_PlotView()
    ui.setupUi(PlotView)
    PlotView.show()
    sys.exit(app.exec_())

