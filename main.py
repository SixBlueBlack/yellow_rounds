import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint
from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.point = False
        self.pushButton.clicked.connect(self.click)

    def click(self):
        self.point = True
        self.update()

    def paintEvent(self, event):
        if not self.point:
            return
        qp = QPainter()
        qp.begin(self)
        self.drawFlag(qp)
        qp.end()

    def drawFlag(self, qp):
        n = randint(1, 50)
        for _ in range(n):
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            a = randint(-10, 430)
            b = randint(-10, 430)
            qp.drawEllipse(a, b, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calendar = MyWidget()
    calendar.show()
    sys.exit(app.exec_())
