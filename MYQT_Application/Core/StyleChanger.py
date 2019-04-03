""" MYQT.Console simple module to view all console log and export to file """

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox,QFileDialog

from assets.UI.Scripts.DebugStyle import Ui_Stylechanger

class StyleChanger(QMainWindow,Ui_Stylechanger):
    def __init__(self,window, parent = None):
        super(StyleChanger,self).__init__(parent)
        self.setupUi(self)
        self.show()

        self.window = window


        self.apply.clicked.connect(lambda:self.setStyle(self.input.toPlainText()))

    def setStyle (self,style):
        self.window.setStyleSheet(style)


