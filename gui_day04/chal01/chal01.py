from PySide6.QtWidgets import *
from chal01UI import Ui_MainWindow
from matplotlib import pyplot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import random


class MyApp(QMainWindow, Ui_MainWindow):
    data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
    names = list(data.keys())
    values = list(data.values())

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
        self.graph3 = self.figure.add_subplot(1, 3, 3)
        print(type(self.figure))
        print(type(self.graph1))

    def draw(self):
        # clear
        self.graph1.cla()
        self.graph2.cla()
        self.graph3.cla()


        # redraw
        self.graph1.bar(self.names, self.values)
        self.canvas.draw()
        self.graph2.scatter(self.names, self.values)
        self.canvas.draw()
        self.graph3.plot(self.names, self.values)
        self.canvas.draw()

    def func(self):
        for idx, obj in enumerate(self.values):
            self.values[idx] = random.randint(0, 50)
        self.draw()

if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()