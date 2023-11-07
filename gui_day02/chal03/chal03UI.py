# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chal03UI.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setMinimumSize(QSize(400, 500))
        MainWindow.setMaximumSize(QSize(400, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.nameBtn = QPushButton(self.centralwidget)
        self.nameBtn.setObjectName(u"nameBtn")

        self.gridLayout.addWidget(self.nameBtn, 3, 0, 1, 1)

        self.startBtn = QPushButton(self.centralwidget)
        self.startBtn.setObjectName(u"startBtn")

        self.gridLayout.addWidget(self.startBtn, 3, 2, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lbl = QLabel(self.frame)
        self.lbl.setObjectName(u"lbl")
        self.lbl.setGeometry(QRect(130, 80, 48, 16))
        self.lbl.setStyleSheet(u"background-color: rgb(255, 255, 0);")

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 3)

        self.colorBtn = QPushButton(self.centralwidget)
        self.colorBtn.setObjectName(u"colorBtn")

        self.gridLayout.addWidget(self.colorBtn, 3, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.nameBtn.clicked.connect(MainWindow.nameChange)
        self.colorBtn.clicked.connect(MainWindow.colorChange)
        self.startBtn.clicked.connect(MainWindow.start)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.nameBtn.setText(QCoreApplication.translate("MainWindow", u"\uc774\ub984 \ubcc0\uacbd", None))
        self.startBtn.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791", None))
        self.lbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">KFC</span></p></body></html>", None))
        self.colorBtn.setText(QCoreApplication.translate("MainWindow", u"\ubc30\uacbd\uc0c9 \ubcc0\uacbd", None))
    # retranslateUi

