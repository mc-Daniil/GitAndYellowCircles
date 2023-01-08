import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.run)
        self.f = False

    def run(self):
        self.f = True
        self.repaint()
        self.f = False

    def paintEvent(self, event):
        if self.f:
            qp = QPainter()
            qp.begin(self)
            self.circles(qp)
            qp.end()

    def circles(self, qp):
        qp.setBrush(QColor("Yellow"))
        for _ in range(randint(1, 10)):
            r = randint(100, 800)
            qp.drawEllipse(randint(100, 800), randint(100, 800), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())