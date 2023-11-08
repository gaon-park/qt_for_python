# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chal02UI.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSlider, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(793, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 9, 771, 531))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 50))

        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)

        self.horizontalSlider = QSlider(self.gridLayoutWidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximumSize(QSize(300, 100))
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider, 3, 1, 1, 1)

        self.downBtn = QPushButton(self.gridLayoutWidget)
        self.downBtn.setObjectName(u"downBtn")
        self.downBtn.setMaximumSize(QSize(300, 100))

        self.gridLayout.addWidget(self.downBtn, 1, 1, 1, 1)

        self.progressBar = QProgressBar(self.gridLayoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(300, 0))
        self.progressBar.setLayoutDirection(Qt.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setValue(24)
        self.progressBar.setOrientation(Qt.Vertical)
        self.progressBar.setInvertedAppearance(True)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout.addWidget(self.progressBar, 0, 0, 4, 1)

        self.upBtn = QPushButton(self.gridLayoutWidget)
        self.upBtn.setObjectName(u"upBtn")
        self.upBtn.setMinimumSize(QSize(100, 100))
        self.upBtn.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.upBtn, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 793, 22))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        self.upBtn.pressed.connect(MainWindow.upPress)
        self.upBtn.released.connect(MainWindow.upRelease)
        self.downBtn.pressed.connect(MainWindow.downPress)
        self.downBtn.released.connect(MainWindow.downRelease)
        self.horizontalSlider.sliderMoved.connect(MainWindow.slideChange)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ubaa8\ud130 \uc18d\ub3c4 \uc81c\uc5b4", None))
        self.downBtn.setText(QCoreApplication.translate("MainWindow", u"DOWN", None))
        self.upBtn.setText(QCoreApplication.translate("MainWindow", u"UP", None))
    # retranslateUi

