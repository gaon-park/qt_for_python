from chal04UI import Ui_MainWindow
from PySide6.QtWidgets import *
from gpiozero import PWMLED, LED

class MyApp(QMainWindow, Ui_MainWindow):
    led1 = LED(14)
    led2 = PWMLED(15)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        self.led1.off()
        self.led2.off()
        self.lcdNumber.display(0)
        pass

    def ledOn(self):
        self.led1.on()

    def ledOff(self):
        self.led1.on()

    def pwmChange(self, pwm):
        self.lcdNumber.display(pwm)
        self.led2.value = pwm / 100


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()