# Form 레이아웃에 2개 widget 배치하기
# 다른 레이아웃 이용해서 widget을 여러 개 배치하면 된다.

from PySide6.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.setWindowTitle("Qt GUI App")
        self.setGeometry(0, 0, 300, 150)
        self.form = QFormLayout(self)
        self._name = QLineEdit()
        _name_hlay = QHBoxLayout()
        _name_hlay.addWidget(self._name)
        self.form.addRow("name", _name_hlay)

        self._age = QLineEdit()
        self._age_chk = QPushButton("나이 확인")
        self._age_chk.clicked.connect(self.age_submit)
        _age_hlay = QHBoxLayout()
        _age_hlay.addWidget(self._age)
        _age_hlay.addWidget(self._age_chk)
        self.form.addRow("age", _age_hlay)

        self._warn = QLabel()
        self._warn.setText("경고: 나이가 너무 많습니다")
        self._warn.setVisible(False)
        _warn_hlay = QHBoxLayout()
        _warn_hlay.addWidget(self._warn)
        self.form.addRow(_warn_hlay)

        self._submit = QPushButton("회원가입", self)
        self._submit.clicked.connect(self.form_submit)
        _submit_hlay = QHBoxLayout()
        _submit_hlay.addWidget(self._submit)
        self.form.addRow(_submit_hlay)

    def form_submit(self):
        if len(self._name.text()) > 4:
            self.msg = QMessageBox()
            self.msg.setText("이름이 너무 깁니다.")
            self.msg.exec()


    def age_submit(self):
        if int(self._age.text()) < 1 or int(self._age.text()) > 30:
            self._warn.setVisible(True)
        else:
            self._warn.setVisible(False)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()
