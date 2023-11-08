from chal02UI import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import *


class MyApp(QMainWindow, Ui_MainWindow):
    up = False
    down = False
    speed = 1

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        self.horizontalSlider.setValue(self.speed)
        self.timer = QTimer()
        self.timer.setInterval(30)
        self.timer.timeout.connect(self.run)
        self.timer.start()

    def run(self):
        if self.up and self.progressBar.value() < 100:
            self.progressBar.setValue(
                100 if self.progressBar.value() + self.speed > 100 else self.progressBar.value() + self.speed)
        elif self.down and self.progressBar.value() > 0:
            self.progressBar.setValue(
                0 if self.progressBar.value() - self.speed < 0 else self.progressBar.value() - self.speed)

    def upPress(self):
        self.up = True

    def upRelease(self):
        self.up = False

    def downPress(self):
        self.down = True

    def downRelease(self):
        self.down = False

    def slideChange(self, speed):
        self.speed = speed
        print(self.speed)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()
