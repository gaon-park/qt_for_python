from chal03UI import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class MyApp(QMainWindow, Ui_MainWindow):
    progress = []
    idx = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        self.progress.append(self.progressBar)
        self.progress.append(self.progressBar_2)
        self.progress.append(self.progressBar_3)
        self.progress.append(self.progressBar_4)
        self.progress.append(self.progressBar_5)
        for o in self.progress:
            o.setValue(0)

    def go(self):
        self.timer = QTimer()
        self.timer.setInterval(30)
        self.timer.timeout.connect(self.run)
        self.timer.start()

    def run(self):
        if self.idx >= 5:
            self.timer.stop()
            return

        self.progress[self.idx].setValue(self.progress[self.idx].value() + 1)
        if self.progress[self.idx].value() == 100:
            self.idx += 1


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()