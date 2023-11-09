from PySide6.QtWidgets import *
from matplotUI import Ui_MainWindow
from matplotlib import pyplot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        self.figure = pyplot.Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.lay.addWidget(self.canvas)
        self.graph1 = self.figure.add_subplot(1, 3, 1)
        self.graph2 = self.figure.add_subplot(1, 3, 2)
        print(type(self.figure))
        print(type(self.graph1))

    def chart1(self):
        x = [1, 2, 3, 4, 5]
        y1 = [10, 20, 30, 43, 54]
        y2 = [32, 54, 7, 34, 65]
        self.graph1.plot(x, y1, linestyle='--', marker='o')
        self.graph1.plot(x, y2, linestyle=':', marker='*')
        self.graph1.legend(["BBQ", "KFC"])
        self.canvas.draw()

    def chart2(self):
        x = [1, 2, 3, 4, 5]
        y = [10, 1, 30, 43, 25]
        self.graph2.bar(x, y)
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()