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
        SQLMANAGER.resize(942, 723)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SQLMANAGER.sizePolicy().hasHeightForWidth())
        SQLMANAGER.setSizePolicy(sizePolicy)
        SQLMANAGER.setWindowOpacity(1.0)
        SQLMANAGER.setAutoFillBackground(False)
        SQLMANAGER.setStyleSheet("/*  ---------------------------- ALL OTHERS WIDGETS ---------------------------- */\n"
"*{\n"
"font-family: Arial, Helvetica, sans-serif;\n"
"selection-background-color: rgb(0, 93, 170);\n"
"selection-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/*  ---------------------------- MAIN WINDOW, WIDGET ---------------------------- */\n"
"QMainWindow,QWidget\n"
"{\n"
"color:rgb(0,0,0);\n"
"background:rgb(255,255,255);\n"
"}\n"
"\n"
"/*  ---------------------------- MENU BAR ---------------------------- */\n"
"QMenuBar\n"
"{\n"
"color:rgb(120,120,120);\n"
"background:rgb(230,230,230);\n"
"}\n"
"QMenuBar::item:selected\n"
"{\n"
"color:rgb(100,100,100);\n"
"background:rgb(200,200,200);\n"
"}\n"
"/*  ---------------------------- CONTEXT MENU ---------------------------- */\n"
"QMenu\n"
"{\n"
"color:rgb(90,90,90);\n"
"background:rgb(230,230,230);\n"
"padding: 3;\n"
"}\n"
"QMenu::item:selected \n"
"{\n"
"color:rgb(90,90,90);\n"
"background:rgb(200,200,200);\n"
"}\n"
"QMenu::separator {\n"
"background:rgb(200,200,200);\n"
"height:1px;\n"
"}\n"
"\n"
"\n"
"/*  ---------------------------- TAB WIDGET ---------------------------- */\n"
"QTabBar::tab {\n"
"color:rgb(150,150,150);\n"
"background:rgb(240,240,240);\n"
"}\n"
"QTabBar::tab:selected {\n"
"background:white;\n"
"color:rgb(100,100,100);\n"
"}\n"
"\n"
"/*  ---------------------------- LINE_EDIT TEXT BROWSER TEXT_EDIT PLAIN_TEXT ---------------------------- */\n"
"QLineEdit,QTextBrowser,QTextEdit,QPlainTextEdit \n"
"{\n"
"color:rgb(20,20,20);\n"
"background-color:white;\n"
"border:1px solid lightgrey;\n"
"}\n"
"\n"
"/*  ---------------------------- CHECK/COMBO BOX ----------------------------*/\n"
"QComboBox {\n"
"border: transparent;\n"
"padding: 1px 18px 1px 3px;\n"
"min-width: 6em;\n"
"color:black;\n"
"background-color:white;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"background:white;\n"
"border:1px solid black;\n"
" }\n"
"\n"
" /* QComboBox gets the \"on\" state when the popup is open */\n"
" QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"     background: rgb(230,230,230);\n"
" }\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"padding-top: 3px;\n"
"padding-left: 4px;\n"
"color:rgb(0, 93, 170);;\n"
" }\n"
"\n"
"QComboBox::drop-down {\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
"width: 15px;\n"
"border-left-width: 2px;\n"
"border-left-color: darkgray;\n"
"border-left-style: solid; /* just a single line */\n"
"border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"border-bottom-right-radius: 3px;\n"
"background-color:rgb(0, 93, 170);;\n"
" }\n"
"\n"
"QCheckBox,QRadioButton\n"
"{\n"
"background: white;\n"
"color:rgb(40,40,40);\n"
"padding: 5;\n"
"border:1px solid rgb(230,230,230);\n"
"}\n"
"\n"
"/* ----------------------------  TOOL BOX  ----------------------------  */\n"
"QToolBox::tab\n"
"{\n"
"color:darkgrey;\n"
"background:lightgrey;\n"
"}\n"
"QToolBox::tab::selected\n"
"{\n"
"color:grey;\n"
"background:rgb(250, 250,250);\n"
"}\n"
"QToolBox::tab::hover\n"
"{\n"
"color:white;\n"
"background:rgb(0, 93, 170);\n"
"}\n"
"/*  ---------------------------- PROGRESS BAR ---------------------------- */\n"
"QProgressBar {\n"
"color:grey;\n"
"text-align: center;\n"
"font-size:13px;\n"
"}\n"
"QProgressBar::chunk {\n"
"background:rgb(0, 193, 50);\n"
"}\n"
"\n"
"\n"
"/*  ---------------------------- PUSHBUTTON ---------------------------- */\n"
"QPushButton\n"
"{\n"
"border: 1px solid lightgrey;\n"
"color:white;\n"
"background:rgb(0, 93, 170);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"border: 1px solid lightgrey;\n"
"color:white;\n"
"background:rgb(0, 120, 210);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"border: 1px solid lightgrey;\n"
"color:white;\n"
"background:rgb(0, 53, 100);\n"
"}\n"
"\n"
"\n"
"\n"
"/* -------------------------- QDIALOG BUTTON BOX ----------------------------------- */\n"
"\n"
"QDialogButtonBox\n"
"{\n"
"min-height: 35px;\n"
"min-width: 50px;\n"
"}\n"
"\n"
"\n"
"/*  ----------------------------  LCD NUMBER ---------------------------- */\n"
"QLCDNumber\n"
"{\n"
"color:rgb(0, 93, 170);\n"
"border:2 solid rgb(100,100,100);\n"
"}\n"
"\n"
"/*  ---------------------------- TABLE_LIST_TABLE ---------------------------- */\n"
"QTableView,QTableWidget\n"
"{\n"
"    alternate-background-color: rgb(230, 230, 230);\n"
"}\n"
"QTreeView\n"
"{\n"
"    background: rgb(250,250,250);\n"
"    color: rgb(180,180,180);\n"
"}\n"
"QTableView::item:selected, QListView::item:selected,QTableView::item:hover, QListView::item:hover, QTreeView::item:hover \n"
"{\n"
"background:rgb(0, 93, 170);\n"
"color:rgb(250,250,250);\n"
"}\n"
"QTableView::item, QListView::item, QTreeView::item\n"
"{\n"
"color:rgb(100,100,100);\n"
"}\n"
"QTreeView::item:selected,QListView::item:selected,QTableView::item:selected\n"
"{\n"
"color:rgb(37, 62, 71);\n"
"background:rgb(209, 241, 252);\n"
"}\n"
"\n"
"/*  ---------------------------- HEADER VIEW ---------------------------- */\n"
"QHeaderView::section \n"
"{\n"
"color:darkgrey;\n"
"background:white;\n"
"border:1px solid rgb(240,240,240);\n"
"text-align:center;\n"
"padding:1;\n"
"}\n"
"\n"
"/* ------------------------------- CALENDAR -------------------------------------------------- */\n"
"\n"
"QCalendarView\n"
"{ \n"
"color: rgb(20,20,20); \n"
"background-color: rgb(240,240,240);\n"
"alternate-background-color: rgb(0, 93, 170);\n"
"selection-background-color: white; \n"
"selection-color: black;\n"
"}\n"
"QAbstractItemView\n"
"{\n"
"color:rgb(200,200,200);\n"
"}\n"
"\n"
"/* ---------------------------------------- SLIDER HORIZONTAL ----------------------------------------------- */\n"
"\n"
"QSlider::groove:horizontal,QSlider::add-page:horizontal \n"
"{\n"
"background: rgb(70,70,70);\n"
"height: 17px;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"height: 10px;\n"
"background: rgb(100,100,100);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"margin-right: -10px;\n"
"margin-left: -10px;\n"
"background: rgb(150,150,150);\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"background:rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* --------------------------------  VERTICAL SLIDER -------------------------------------------------------------- */\n"
"\n"
"QSlider::handle\n"
"{\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::groove:vertical,QSlider::add-page:vertical\n"
"{\n"
"width: 20px;\n"
"background: rgb(70,70,70);\n"
"}\n"
"QSlider::sub-page:vertical \n"
"{\n"
"background: rgb(100,100,100);\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"margin-top: -10px;\n"
"margin-bottom: -10px;\n"
"background: rgb(150,150,150);\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"background: white;\n"
"}\n"
"\n"
"/* --------------------------------- SCROLLBAR HORIZONTAL -------------------------------------- */\n"
"\n"
"QScrollBar::groove:horizontal{\n"
"background: white;\n"
"height: 17px;\n"
"}\n"
"QScrollBar::sub-page:horizontal,QScrollBar::add-page:horizontal  {\n"
"height: 10px;\n"
"background: rgb(100,100,100);\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"margin-right: -5px;\n"
"background: rgb(150,150,150);\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"background: white;\n"
"}\n"
"\n"
"/* --------------------------------------- SCROLLBAR VERTICAL ---------------------------------------------- */\n"
"\n"
"QScrollBar::groove:vertical\n"
"{\n"
"width: 20px;\n"
"}\n"
"QScrollBar::sub-page:vertical,QScrollBar::add-page:vertical\n"
"{\n"
"background: rgb(100,100,100);\n"
"}\n"
"QScrollBar::handle:vertical \n"
"{\n"
"margin-top: -3px;\n"
"margin-bottom: -3px;\n"
"background: rgb(150,150,150);\n"
"}\n"
"QScrollBar::handle:vertical:hover \n"
"{\n"
"background: white;\n"
"}\n"
"\n"
"/* ---------------------------------------------------------------------------------------------- */\n"
"\n"
"QToolBar {\n"
"    background: rgb(50, 50, 50);\n"
"    spacing: 4;\n"
"}\n"
"/* QToolBar:separator\n"
"{\n"
"    background: rgb(80, 80, 80);\n"
"} */\n"
"\n"
"/* ---------------------------------------------------------------------------------------------- */\n"
"\n"
"QToolButton\n"
"{\n"
"margin: 3;\n"
"color:rgb(255, 255, 255);\n"
"background:transparent;\n"
"}\n"
"QToolButton:hover\n"
"{\n"
"margin: 0;\n"
"color:white;\n"
"background:rgb(50,50,50);\n"
"}\n"
"QToolButton:pressed\n"
"{\n"
"margin: 0;\n"
"color:white;\n"
"background:rgb(29, 29, 29);\n"
"}")
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
        self.tables_out.setMaximumSize(QtCore.QSize(266, 16777215))
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
        self.tabs.setIconSize(QtCore.QSize(24, 24))
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
        self.gridLayout_4.addWidget(self.query_in, 0, 0, 1, 1)
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
        self.gridLayout_4.addWidget(self.result_out, 1, 0, 1, 1)
        self.tabs.addTab(self._query, "")
        self.gridLayout.addWidget(self.tabs, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setMinimumSize(QtCore.QSize(409, 22))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: lightgrey;")
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
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
        self.openConsole.setMinimumSize(QtCore.QSize(81, 22))
        self.openConsole.setMaximumSize(QtCore.QSize(81, 22))
        font = QtGui.QFont()
        font.setFamily("Arial,Helvetica,sans-serif")
        font.setPointSize(10)
        self.openConsole.setFont(font)
        self.openConsole.setStyleSheet("border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;")
        self.openConsole.setDefault(False)
        self.openConsole.setFlat(False)
        self.openConsole.setObjectName("openConsole")
        self.gridLayout.addWidget(self.openConsole, 2, 2, 1, 1)
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
        self.tabs.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(SQLMANAGER)
        SQLMANAGER.setTabOrder(self.tables_out, self.data_result)
        SQLMANAGER.setTabOrder(self.data_result, self.desc_result)
        SQLMANAGER.setTabOrder(self.desc_result, self.query_in)
        SQLMANAGER.setTabOrder(self.query_in, self.create_in)
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
        self.openConsole.setText(_translate("SQLMANAGER", "VIEW LOG"))
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

