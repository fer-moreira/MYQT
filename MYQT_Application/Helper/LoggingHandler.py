import traceback

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication, QFile, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QFileDialog,QMainWindow, QMessageBox, QTableWidget,QTableWidgetItem, QTreeWidgetItem,QWidget

class Logging (object):
    def __init__(self, parent = None):
        print("a")

    def LOG_Crtitical   (self,Content): QMessageBox.critical(self,"Critical"   ,str(Content),QMessageBox.Ok)
    def LOG_Warning     (self,Content): QMessageBox.Warning (self,"Warning"    ,str(Content),QMessageBox.Ok)
    def LOG_Information (self,Content): QMessageBox.Information (self,"Information",str(Content),QMessageBox.Ok)