from chal01UI import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        pass

    def run(self):
        self.progressBar.setValue(self.progressBar.value() + 1)
        if self.progressBar.value() == 100:
            self.timer.stop()

    def go(self):
        self.timer = QTimer()
        self.timer.setInterval(30)
        self.timer.timeout.connect(self.run)
        self.timer.start()

    def pause(self):
        self.timer.stop()


    def reset(self):
        self.progressBar.setValue(0)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()