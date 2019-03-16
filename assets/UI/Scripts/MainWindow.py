# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\assets\UI\Layout\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SQLMANAGER(object):
    def setupUi(self, SQLMANAGER):
        SQLMANAGER.setObjectName("SQLMANAGER")
        SQLMANAGER.setWindowModality(QtCore.Qt.ApplicationModal)
        SQLMANAGER.resize(942, 725)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SQLMANAGER.sizePolicy().hasHeightForWidth())
        SQLMANAGER.setSizePolicy(sizePolicy)
        SQLMANAGER.setWindowOpacity(1.0)
        SQLMANAGER.setAutoFillBackground(False)
        SQLMANAGER.setWindowFilePath("")
        SQLMANAGER.setInputMethodHints(QtCore.Qt.ImhNone)
        SQLMANAGER.setIconSize(QtCore.QSize(24, 24))
        SQLMANAGER.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        SQLMANAGER.setAnimated(True)
        SQLMANAGER.setDocumentMode(False)
        SQLMANAGER.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(SQLMANAGER)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tables_out = QtWidgets.QTreeWidget(self.centralwidget)
        self.tables_out.setMinimumSize(QtCore.QSize(258, 0))
        self.tables_out.setMaximumSize(QtCore.QSize(258, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial,Helvetica,sans-serif")
        font.setPointSize(10)
        self.tables_out.setFont(font)
        self.tables_out.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tables_out.setAutoFillBackground(False)
        self.tables_out.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tables_out.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tables_out.setLineWidth(0)
        self.tables_out.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tables_out.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tables_out.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tables_out.setHeaderHidden(False)
        self.tables_out.setColumnCount(1)
        self.tables_out.setObjectName("tables_out")
        self.tables_out.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tables_out.headerItem().setFont(0, font)
        self.tables_out.header().setVisible(True)
        self.tables_out.header().setCascadingSectionResizes(True)
        self.tables_out.header().setDefaultSectionSize(100)
        self.tables_out.header().setHighlightSections(True)
        self.gridLayout.addWidget(self.tables_out, 0, 0, 3, 1)
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.tabs.setMinimumSize(QtCore.QSize(571, 541))
        self.tabs.setSizeIncrement(QtCore.QSize(9, 18))
        font = QtGui.QFont()
        font.setFamily("Arial,Helvetica,sans-serif")
        font.setPointSize(12)
        self.tabs.setFont(font)
        self.tabs.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabs.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tabs.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabs.setAutoFillBackground(False)
        self.tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabs.setIconSize(QtCore.QSize(15, 15))
        self.tabs.setElideMode(QtCore.Qt.ElideLeft)
        self.tabs.setUsesScrollButtons(False)
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(False)
        self.tabs.setMovable(False)
        self.tabs.setTabBarAutoHide(False)
        self.tabs.setObjectName("tabs")
        self._data = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._data.sizePolicy().hasHeightForWidth())
        self._data.setSizePolicy(sizePolicy)
        self._data.setObjectName("_data")
        self.gridLayout_2 = QtWidgets.QGridLayout(self._data)
        self.gridLayout_2.setContentsMargins(0, 0, 2, 0)
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.data_result = QtWidgets.QTableWidget(self._data)
        self.data_result.setEnabled(True)
        self.data_result.setMinimumSize(QtCore.QSize(0, 609))
        font = QtGui.QFont()
        font.setFamily("Arial,Helvetica,sans-serif")
        font.setPointSize(10)
        self.data_result.setFont(font)
        self.data_result.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.data_result.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.data_result.setFrameShadow(QtWidgets.QFrame.Plain)
        self.data_result.setLineWidth(1)
        self.data_result.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.data_result.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.data_result.setTabKeyNavigation(False)
        self.data_result.setProperty("showDropIndicator", False)
        self.data_result.setDragDropOverwriteMode(False)
        self.data_result.setAlternatingRowColors(True)
        self.data_result.setShowGrid(True)
        self.data_result.setGridStyle(QtCore.Qt.SolidLine)
        self.data_result.setWordWrap(True)
        self.data_result.setCornerButtonEnabled(True)
        self.data_result.setObjectName("data_result")
        self.data_result.setColumnCount(0)
        self.data_result.setRowCount(0)
        self.gridLayout_2.addWidget(self.data_result, 0, 0, 1, 1)
        self.tabs.addTab(self._data, "")
        self._desc = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._desc.sizePolicy().hasHeightForWidth())
        self._desc.setSizePolicy(sizePolicy)
        self._desc.setObjectName("_desc")
        self.gridLayout_3 = QtWidgets.QGridLayout(self._desc)
        self.gridLayout_3.setContentsMargins(0, 0, 2, 0)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.desc_result = QtWidgets.QTableWidget(self._desc)
        self.desc_result.setMinimumSize(QtCore.QSize(0, 304))
        self.desc_result.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.desc_result.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.desc_result.setFrameShadow(QtWidgets.QFrame.Plain)
        self.desc_result.setLineWidth(1)
        self.desc_result.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.desc_result.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.desc_result.setTabKeyNavigation(False)
        self.desc_result.setProperty("showDropIndicator", False)
        self.desc_result.setDragDropOverwriteMode(False)
        self.desc_result.setAlternatingRowColors(True)
        self.desc_result.setShowGrid(True)
        self.desc_result.setGridStyle(QtCore.Qt.SolidLine)
        self.desc_result.setWordWrap(True)
        self.desc_result.setCornerButtonEnabled(True)
        self.desc_result.setObjectName("desc_result")
        self.desc_result.setColumnCount(0)
        self.desc_result.setRowCount(0)
        self.gridLayout_3.addWidget(self.desc_result, 0, 0, 1, 1)
        self.create_in = QtWidgets.QPlainTextEdit(self._desc)
        self.create_in.setMinimumSize(QtCore.QSize(0, 304))
        font = QtGui.QFont()
        font.setFamily("Arial,Helvetica,sans-serif")
        font.setPointSize(10)
        self.create_in.setFont(font)
        self.create_in.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.create_in.setFrameShadow(QtWidgets.QFrame.Plain)
        self.create_in.setLineWidth(1)
        self.create_in.setMidLineWidth(0)
        self.create_in.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.create_in.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.create_in.setUndoRedoEnabled(False)
        self.create_in.setReadOnly(True)
        self.create_in.setPlainText("")
        self.create_in.setBackgroundVisible(False)
        self.create_in.setCenterOnScroll(False)
        self.create_in.setPlaceholderText("")
        self.create_in.setObjectName("create_in")
        self.gridLayout_3.addWidget(self.create_in, 1, 0, 1, 1)
        self.tabs.addTab(self._desc, "")
        self._query = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._query.sizePolicy().hasHeightForWidth())
        self._query.setSizePolicy(sizePolicy)
        self._query.setObjectName("_query")
        self.gridLayout_4 = QtWidgets.QGridLayout(self._query)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setVerticalSpacing(4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.result_out = QtWidgets.QTableWidget(self._query)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_out.sizePolicy().hasHeightForWidth())
        self.result_out.setSizePolicy(sizePolicy)
        self.result_out.setMinimumSize(QtCore.QSize(0, 300))
        self.result_out.setMaximumSize(QtCore.QSize(16777215, 300))
        font = QtGui.QFont()
        font.setFamily("Arial,Helvetica,sans-serif")
        font.setPointSize(10)
        self.result_out.setFont(font)
        self.result_out.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.result_out.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.result_out.setFrameShadow(QtWidgets.QFrame.Plain)
        self.result_out.setLineWidth(1)
        self.result_out.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.result_out.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.result_out.setTabKeyNavigation(False)
        self.result_out.setProperty("showDropIndicator", False)
        self.result_out.setDragDropOverwriteMode(False)
        self.result_out.setAlternatingRowColors(True)
        self.result_out.setShowGrid(True)
        self.result_out.setGridStyle(QtCore.Qt.SolidLine)
        self.result_out.setWordWrap(True)
        self.result_out.setCornerButtonEnabled(False)
        self.result_out.setObjectName("result_out")
        self.result_out.setColumnCount(0)
        self.result_out.setRowCount(0)
        self.gridLayout_4.addWidget(self.result_out, 2, 0, 1, 1)
        self.query_in = QtWidgets.QPlainTextEdit(self._query)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.query_in.sizePolicy().hasHeightForWidth())
        self.query_in.setSizePolicy(sizePolicy)
        self.query_in.setMinimumSize(QtCore.QSize(0, 301))
        self.query_in.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial,Helvetica,sans-serif")
        font.setPointSize(11)
        self.query_in.setFont(font)
        self.query_in.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.query_in.setMouseTracking(False)
        self.query_in.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.query_in.setAutoFillBackground(False)
        self.query_in.setInputMethodHints(QtCore.Qt.ImhDate|QtCore.Qt.ImhDialableCharactersOnly|QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhEmailCharactersOnly|QtCore.Qt.ImhExclusiveInputMask|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhLatinOnly|QtCore.Qt.ImhLowercaseOnly|QtCore.Qt.ImhMultiLine|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoEditMenu|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhNoTextHandles|QtCore.Qt.ImhPreferLatin|QtCore.Qt.ImhPreferLowercase|QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhSensitiveData|QtCore.Qt.ImhTime|QtCore.Qt.ImhUppercaseOnly|QtCore.Qt.ImhUrlCharactersOnly)
        self.query_in.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.query_in.setFrameShadow(QtWidgets.QFrame.Plain)
        self.query_in.setLineWidth(1)
        self.query_in.setMidLineWidth(0)
        self.query_in.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.query_in.setPlainText("")
        self.query_in.setBackgroundVisible(False)
        self.query_in.setCenterOnScroll(False)
        self.query_in.setObjectName("query_in")
        self.gridLayout_4.addWidget(self.query_in, 1, 0, 1, 1)
        self.tabs.addTab(self._query, "")
        self.gridLayout.addWidget(self.tabs, 0, 1, 1, 2)
        self.console_out = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.console_out.setMinimumSize(QtCore.QSize(660, 130))
        self.console_out.setMaximumSize(QtCore.QSize(16777215, 130))
        font = QtGui.QFont()
        font.setFamily("Arial,Helvetica,sans-serif")
        font.setPointSize(12)
        self.console_out.setFont(font)
        self.console_out.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.console_out.setStyleSheet("border:1px solid lightgrey;")
        self.console_out.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.console_out.setFrameShadow(QtWidgets.QFrame.Plain)
        self.console_out.setLineWidth(1)
        self.console_out.setMidLineWidth(0)
        self.console_out.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.console_out.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.console_out.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.console_out.setUndoRedoEnabled(False)
        self.console_out.setReadOnly(True)
        self.console_out.setPlainText("")
        self.console_out.setBackgroundVisible(False)
        self.console_out.setCenterOnScroll(False)
        self.console_out.setObjectName("console_out")
        self.gridLayout.addWidget(self.console_out, 1, 1, 1, 2)
        self.openConsole = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial,Helvetica,sans-serif")
        font.setPointSize(10)
        self.openConsole.setFont(font)
        self.openConsole.setDefault(False)
        self.openConsole.setFlat(False)
        self.openConsole.setObjectName("openConsole")
        self.gridLayout.addWidget(self.openConsole, 2, 1, 1, 2)
        SQLMANAGER.setCentralWidget(self.centralwidget)
        self.actionImport_Query = QtWidgets.QAction(SQLMANAGER)
        self.actionImport_Query.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        self.actionImport_Query.setObjectName("actionImport_Query")
        self.actionExport_Query = QtWidgets.QAction(SQLMANAGER)
        self.actionExport_Query.setObjectName("actionExport_Query")
        self.actionCompile = QtWidgets.QAction(SQLMANAGER)
        self.actionCompile.setObjectName("actionCompile")
        self.actionExecute_Selected = QtWidgets.QAction(SQLMANAGER)
        self.actionExecute_Selected.setObjectName("actionExecute_Selected")
        self.actionAbout = QtWidgets.QAction(SQLMANAGER)
        self.actionAbout.setObjectName("actionAbout")
        self.actionDocuments = QtWidgets.QAction(SQLMANAGER)
        self.actionDocuments.setObjectName("actionDocuments")
        self.actionCopy = QtWidgets.QAction(SQLMANAGER)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(SQLMANAGER)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCrop = QtWidgets.QAction(SQLMANAGER)
        self.actionCrop.setObjectName("actionCrop")
        self.actionSelect_All = QtWidgets.QAction(SQLMANAGER)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionInvert_Selection = QtWidgets.QAction(SQLMANAGER)
        self.actionInvert_Selection.setObjectName("actionInvert_Selection")
        self.actionExit = QtWidgets.QAction(SQLMANAGER)
        self.actionExit.setObjectName("actionExit")
        self.actionRefresh_Database = QtWidgets.QAction(SQLMANAGER)
        self.actionRefresh_Database.setObjectName("actionRefresh_Database")

        self.retranslateUi(SQLMANAGER)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SQLMANAGER)
        SQLMANAGER.setTabOrder(self.tables_out, self.data_result)
        SQLMANAGER.setTabOrder(self.data_result, self.desc_result)
        SQLMANAGER.setTabOrder(self.desc_result, self.create_in)
        SQLMANAGER.setTabOrder(self.create_in, self.result_out)
        SQLMANAGER.setTabOrder(self.result_out, self.console_out)
        SQLMANAGER.setTabOrder(self.console_out, self.openConsole)
        SQLMANAGER.setTabOrder(self.openConsole, self.tabs)

    def retranslateUi(self, SQLMANAGER):
        _translate = QtCore.QCoreApplication.translate
        SQLMANAGER.setWindowTitle(_translate("SQLMANAGER", "SQL Manager"))
        self.tables_out.headerItem().setText(0, _translate("SQLMANAGER", "CONNECTION"))
        self.data_result.setSortingEnabled(False)
        self.tabs.setTabText(self.tabs.indexOf(self._data), _translate("SQLMANAGER", "Data"))
        self.desc_result.setSortingEnabled(False)
        self.tabs.setTabText(self.tabs.indexOf(self._desc), _translate("SQLMANAGER", "Fields"))
        self.result_out.setSortingEnabled(False)
        self.tabs.setTabText(self.tabs.indexOf(self._query), _translate("SQLMANAGER", "Query"))
        self.openConsole.setText(_translate("SQLMANAGER", "EXPAND LOG VISUALIZER"))
        self.actionImport_Query.setText(_translate("SQLMANAGER", "Load SQL File"))
        self.actionImport_Query.setShortcut(_translate("SQLMANAGER", "Ctrl+W"))
        self.actionExport_Query.setText(_translate("SQLMANAGER", "Execute SQL File"))
        self.actionExport_Query.setShortcut(_translate("SQLMANAGER", "Ctrl+E"))
        self.actionCompile.setText(_translate("SQLMANAGER", "Execute Query"))
        self.actionCompile.setShortcut(_translate("SQLMANAGER", "Ctrl+Return"))
        self.actionExecute_Selected.setText(_translate("SQLMANAGER", "Execute Selected"))
        self.actionExecute_Selected.setShortcut(_translate("SQLMANAGER", "Ctrl+Shift+Return"))
        self.actionAbout.setText(_translate("SQLMANAGER", "About"))
        self.actionDocuments.setText(_translate("SQLMANAGER", "Documents"))
        self.actionCopy.setText(_translate("SQLMANAGER", "Copy"))
        self.actionCopy.setShortcut(_translate("SQLMANAGER", "Ctrl+C"))
        self.actionPaste.setText(_translate("SQLMANAGER", "Paste"))
        self.actionPaste.setShortcut(_translate("SQLMANAGER", "Ctrl+V"))
        self.actionCrop.setText(_translate("SQLMANAGER", "Crop"))
        self.actionCrop.setShortcut(_translate("SQLMANAGER", "Ctrl+X"))
        self.actionSelect_All.setText(_translate("SQLMANAGER", "Select All"))
        self.actionSelect_All.setShortcut(_translate("SQLMANAGER", "Ctrl+A"))
        self.actionInvert_Selection.setText(_translate("SQLMANAGER", "Invert Selection"))
        self.actionInvert_Selection.setShortcut(_translate("SQLMANAGER", "Ctrl+Shift+A"))
        self.actionExit.setText(_translate("SQLMANAGER", "Exit"))
        self.actionRefresh_Database.setText(_translate("SQLMANAGER", "Refresh Database"))
        self.actionRefresh_Database.setShortcut(_translate("SQLMANAGER", "Ctrl+R"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SQLMANAGER = QtWidgets.QMainWindow()
    ui = Ui_SQLMANAGER()
    ui.setupUi(SQLMANAGER)
    SQLMANAGER.show()
    sys.exit(app.exec_())

