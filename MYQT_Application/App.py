import sys
from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from Core.Connector import ConnectorWindow

app = QApplication(sys.argv)
Main_GUI = ConnectorWindow()

def closeEvent(self): sys.exit(0)

sys.exit(app.exec_())