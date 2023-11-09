#openCV 로 이미지 가공하고, Qt로 출력하는 샘플코드

import cv2
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from opencv_testUI import Ui_MainWindow
import numpy

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        self.img = QImage('burger.png')
        pixmap_img = QPixmap(self.img)
        self.origin_lbl.setPixmap(pixmap_img)

    def printImage(self, imgBGR):
        imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
        h, w, byte = imgRGB.shape
        img = QImage(imgRGB, w, h, byte*w, QImage.Format_RGB888)
        self.openCV_lbl.setPixmap(QPixmap(img))

    def blur(self):
        self.openCV_img = cv2.imread('burger.png')
        self.blurImg = cv2.blur(self.openCV_img, (55,55))
        self.printImage(self.blurImg)
        print('blur')

    def gray(self):
        self.openCV_img = cv2.imread('burger.png')
        self.grayImg = cv2.cvtColor(self.openCV_img, cv2.COLOR_BGR2GRAY)
        self.printImage(self.grayImg)
        print('gray')

    def morpho(self):
        self.openCV_img = cv2.imread('burger.png')
        self.grayImg = cv2.cvtColor(self.openCV_img, cv2.COLOR_BGR2GRAY)
        kernel = numpy.ones((3,3))
        self.morphoImg = cv2.morphologyEx(self.grayImg, cv2.MORPH_GRADIENT, kernel)
        self.printImage(self.morphoImg)
        print('morphology')

    def thresh(self):
        self.openCV_img = cv2.imread('burger.png')
        self.grayImg = cv2.cvtColor(self.openCV_img, cv2.COLOR_BGR2GRAY)
        ret, self.thresholdImg = cv2.threshold(self.grayImg, 120, 255, cv2.THRESH_BINARY)
        self.printImage(self.thresholdImg)
        print('threshold')

    def canny(self):
        self.openCV_img = cv2.imread('burger.png')
        self.grayImg = cv2.cvtColor(self.openCV_img, cv2.COLOR_BGR2GRAY)
        self.cannyImg = cv2.Canny(self.grayImg, 50, 200)
        self.printImage(self.cannyImg)
        print('canny')

    def clear(self):
        self.openCV_lbl.clear()
        print('clear')

if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()