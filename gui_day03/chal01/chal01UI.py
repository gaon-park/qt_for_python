# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chal01UI.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(793, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 771, 531))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.progressBar = QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 250))
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.goBtn = QPushButton(self.verticalLayoutWidget)
        self.goBtn.setObjectName(u"goBtn")
        self.goBtn.setMinimumSize(QSize(0, 100))

        self.horizontalLayout.addWidget(self.goBtn)

        self.pauseBtn = QPushButton(self.verticalLayoutWidget)
        self.pauseBtn.setObjectName(u"pauseBtn")
        self.pauseBtn.setMinimumSize(QSize(0, 100))

        self.horizontalLayout.addWidget(self.pauseBtn)

        self.resetBtn = QPushButton(self.verticalLayoutWidget)
        self.resetBtn.setObjectName(u"resetBtn")
        self.resetBtn.setMinimumSize(QSize(0, 100))

        self.horizontalLayout.addWidget(self.resetBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 793, 22))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        self.goBtn.clicked.connect(MainWindow.go)
        self.pauseBtn.clicked.connect(MainWindow.pause)
        self.resetBtn.clicked.connect(MainWindow.reset)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.goBtn.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.pauseBtn.setText(QCoreApplication.translate("MainWindow", u"PAUSE", None))
        self.resetBtn.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
    # retranslateUi

