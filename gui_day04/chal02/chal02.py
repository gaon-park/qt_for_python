from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from chal02UI import Ui_MainWindow
import cv2
import numpy
from time import sleep
import os

del os.environ['QT_QPA_PLATFORM_PLUGIN_PATH']


class MyThread(QThread):
    mySignal = Signal(QPixmap, QPixmap)
    mode = ''

    # Thread 시작 시 촬영
    def __init__(self):
        super().__init__()
        self.cam = cv2.VideoCapture(0)
        self.cam.set(3, 480)
        self.cam.set(4, 320)

    flag = False

    def run(self):
        self.flag = True
        while self.flag:
            ret, self.img = self.cam.read()
            if ret:
                self.printImage(self.img)
            sleep(0.1)

    def stop(self):
        self.flag = False

    def printImage(self, imgBGR):
        imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
        h, w, byte = imgRGB.shape
        img = QImage(imgRGB, w, h, byte * w, QImage.Format_RGB888)
        q_img1 = QPixmap(img)

        grayImg = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2GRAY)
        convertImg = cv2.Canny(grayImg, 50, 200)
        if self.mode == 'blur':
            convertImg = cv2.blur(imgBGR, (55,55))
        elif self.mode == 'gray':
            convertImg = grayImg
        elif self.mode == 'morpho':
            convertImg = cv2.morphologyEx(grayImg, cv2.MORPH_GRADIENT, numpy.ones((3, 3)))
        elif self.mode == 'thresh':
            convertImg = cv2.threshold(grayImg, 120, 255, cv2.THRESH_BINARY)

        imgRGB = cv2.cvtColor(convertImg, cv2.COLOR_BGR2RGB)
        h, w, byte = imgRGB.shape
        img = QImage(imgRGB, w, h, byte * w, QImage.Format_RGB888)
        q_img2 = QPixmap(img)

        self.mySignal.emit(q_img1, q_img2)


class MyApp(QMainWindow, Ui_MainWindow):
    cur_mode = ['blur', 'gray', 'morpho', 'canny']
    idx = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        self.th = MyThread()
        self.th.mySignal.connect(self.setImage)

    def setImage(self, img, img2):
        self.cam_lbl.setPixmap(img)
        self.openCV_lbl.setPixmap(img2)

    def play(self):
        print('play')
        if self.th.flag:
            self.th.stop()
        else:
            self.th.start()

    def mode(self):
        self.idx = 0 if self.idx + 1 >= 4 else self.idx + 1
        self.th.mode = self.cur_mode[self.idx]

    def closeEvent(self, event):
        self.th.stop()
        # self.th.wait(3000)
        self.close()


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec_()
