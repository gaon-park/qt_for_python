# Form 레이아웃에 2개 widget 배치하기
# 다른 레이아웃 이용해서 widget을 여러 개 배치하면 된다.

from PySide6.QtWidgets import *
from PySide6.QtGui import *


class MyApp(QMainWindow):
    friends = []

    def __init__(self):
        super().__init__()
        self.main()

    def show_friends(self):
        for name in self.friends:
            self.friendsLay.addRow(QLabel(name))

    def add_name(self):
        if self._name.text() in self.friends:
            self.bar.showMessage("이미 등록된 사람입니다")
        elif len(self.friends) == 10:
            self.bar.showMessage("인맥이 꽉 찼습니다")
        else:
            self.friends.append(self._name.text())
            self.friendsLay.addWidget(QLabel(self._name.text()))
            self.bar.showMessage("추가되었습니다")

    def del_name(self):
        idx = -1
        for i, obj in enumerate(self.friends):
            if obj == self._name.text():
                idx = i
                break
        if idx >= 0:
            self.friends.remove(self._name.text())
            self.friendsLay.removeRow(idx)
            self.bar.showMessage("제거되었습니다")
        else:
            self.bar.showMessage("없는 사람입니다")

    def exit(self):
        quit(0)

    def main(self):
        self.setWindowTitle("My Friends")
        self.setGeometry(0, 0, 300, 400)

        mainLay = QVBoxLayout()
        self.form = QFormLayout(self)
        self._name = QLineEdit()
        _name_hlay = QHBoxLayout()
        _name_hlay.addWidget(self._name)
        self.form.addRow("name", _name_hlay)

        self._add = QPushButton("추가")
        self._add.clicked.connect(self.add_name)

        self._del = QPushButton("제거")
        self._del.clicked.connect(self.del_name)

        _btn_hlay = QHBoxLayout()
        _btn_hlay.addWidget(self._add)
        _btn_hlay.addWidget(self._del)
        self.form.addRow(_btn_hlay)

        self.friendsLay = QFormLayout()
        self.show_friends()

        mainLay.addLayout(self.form)
        mainLay.addLayout(self.friendsLay)
        mainWidget = QWidget()
        mainWidget.setLayout(mainLay)
        self.setCentralWidget(mainWidget)

        # menuBar
        self._menuBar = self.menuBar()
        self._menu = self._menuBar.addMenu("메뉴")

        # QAction
        self.exitAction = QAction("종료", self)
        self.exitAction.triggered.connect(self.exit)

        self.addAction = QAction("추가", self)
        self.addAction.triggered.connect(self.add_name)

        self.delAction = QAction("제거", self)
        self.delAction.triggered.connect(self.del_name)

        self._menu.addAction(self.addAction)
        self._menu.addAction(self.delAction)
        self._menuBar.addAction(self.exitAction)

        # status
        self.bar = self.statusBar()


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()
