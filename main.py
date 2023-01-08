import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.circles)

    def circles(self):
        print("Hello")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())