from chal03UI import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from random import randint


class MyApp(QMainWindow, Ui_MainWindow):
    cnt = 0  # click count
    cur = 0  # time
    boxRange = [0, 0, 0, 0]

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        pass

    def setRange(self):
        self.boxRange[0] = self.lbl.x()
        self.boxRange[1] = self.boxRange[0] + self.lbl.width()
        self.boxRange[2] = self.lbl.y()
        self.boxRange[3] = self.boxRange[2] + self.lbl.height()

    def start(self):
        self.cnt = 0
        self.cur = 0
        self.setRange()

        self.timer = QBasicTimer()
        self.timer.start(1000, self)

    def colorChange(self):
        color = QColorDialog.getColor().name()
        if color:
            self.lbl.setStyleSheet('background-color:%s' % color)

    def nameChange(self):
        name, res = QInputDialog.getText(self, "Label 메시지", "입력")
        if res:
            self.lbl.setText(name)
            self.lbl.adjustSize()

    def show_message(self):
        msg = QMessageBox()
        msg.about(self, "python", "1분동안 클릭 수: %d" % self.cnt)

    def timerEvent(self, event):
        if self.cur >= 10:
            self.timer.stop()
            self.show_message()

        self.cur += 1
        x = randint(0, self.frame.width() - self.lbl.width())
        y = randint(0, self.frame.height() - self.lbl.height())
        self.lbl.move(x, y)
        self.setRange()

    def mousePressEvent(self, event):
        x = event.x() - 9  # margin
        y = event.y() - 9
        if self.boxRange[0] <= x and x <= self.boxRange[1] and self.boxRange[2] <= y and y <= self.boxRange[3]:
            self.cnt += 1
            print(self.cnt)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()
