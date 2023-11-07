from chal02UI import Ui_MainWindow
from PySide6.QtWidgets import *

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        pass

    def ledON(self):
        print("ON")

    def ledOFF(self):
        print("OFF")

    def setDial(self, val):
        self.lcdNumber.display(val)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()