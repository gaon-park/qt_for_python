# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chal05UI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(267, 451)
        MainWindow.setMaximumSize(QSize(300, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 251, 391))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.table = QTableWidget(self.verticalLayoutWidget)
        if (self.table.columnCount() < 8):
            self.table.setColumnCount(8)
        if (self.table.rowCount() < 8):
            self.table.setRowCount(8)
        self.table.setObjectName(u"table")
        self.table.setMaximumSize(QSize(350, 550))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setShowGrid(True)
        self.table.setWordWrap(True)
        self.table.setRowCount(8)
        self.table.setColumnCount(8)
        self.table.horizontalHeader().setVisible(False)
        self.table.horizontalHeader().setMinimumSectionSize(30)
        self.table.horizontalHeader().setDefaultSectionSize(30)
        self.table.horizontalHeader().setHighlightSections(False)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setMinimumSectionSize(30)
        self.table.verticalHeader().setHighlightSections(False)

        self.verticalLayout.addWidget(self.table)

        self.rSlider = QSlider(self.verticalLayoutWidget)
        self.rSlider.setObjectName(u"rSlider")
        self.rSlider.setMaximum(255)
        self.rSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.rSlider)

        self.gSlider = QSlider(self.verticalLayoutWidget)
        self.gSlider.setObjectName(u"gSlider")
        self.gSlider.setMaximum(255)
        self.gSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.gSlider)

        self.bSlider = QSlider(self.verticalLayoutWidget)
        self.bSlider.setObjectName(u"bSlider")
        self.bSlider.setMaximum(255)
        self.bSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.bSlider)

        self.flashBtn = QPushButton(self.verticalLayoutWidget)
        self.flashBtn.setObjectName(u"flashBtn")

        self.verticalLayout.addWidget(self.flashBtn)

        self.clearBtn = QPushButton(self.verticalLayoutWidget)
        self.clearBtn.setObjectName(u"clearBtn")

        self.verticalLayout.addWidget(self.clearBtn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 267, 22))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        self.flashBtn.clicked.connect(MainWindow.flash)
        self.clearBtn.clicked.connect(MainWindow.clear)
        self.rSlider.valueChanged.connect(MainWindow.rSliderChange)
        self.gSlider.valueChanged.connect(MainWindow.gSliderChange)
        self.bSlider.valueChanged.connect(MainWindow.bSliderChange)
        self.table.cellEntered.connect(MainWindow.click)
        self.table.cellPressed.connect(MainWindow.click)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.flashBtn.setText(QCoreApplication.translate("MainWindow", u"Flash", None))
        self.clearBtn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
    # retranslateUi

