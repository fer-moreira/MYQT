from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QMenu, QApplication

from Lib.UI.SCRIPT.Testes import Ui_Testes

import sys

app = QApplication(sys.argv)
app.processEvents()

class MainWindow(QMainWindow,Ui_Testes):
    def __init__(self, parent = None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Prototype Window")
        self.setFixedSize(self.size())
        self.show()



Main_GUI = MainWindow()
sys.exit(app.exec_())