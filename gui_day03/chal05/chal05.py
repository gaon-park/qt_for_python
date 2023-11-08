from chal05UI import Ui_MainWindow
from PySide6.QtWidgets import *
from sense_hat import SenseHat

class MyApp(QMainWindow, Ui_MainWindow):
    r = 0
    g = 0
    b = 0
    sense = SenseHat()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        pass

    def click(self, row, col):
        self.sense.set_pixel(row, col, (self.r, self.g, self.b))

    def rSliderChange(self, val):
        self.r = val

    def gSliderChange(self, val):
        self.g = val

    def bSliderChange(self, val):
        self.b = val

    def flash(self):
        for r in range(0, 8):
            for c in range(0, 8):
                self.sense.set_pixel(r, c, (self.r, self.g, self.b))

    def clear(self):
        self.sense.clear()


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()