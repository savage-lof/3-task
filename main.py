import random
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from untitled import Ui_Form


class WindowDraw(QWidget, Ui_Form):
    def init(self):
        super().init()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.qp.end()

    def run(self):
        self.qp.setBrush(QColor('#f7ff00'))
        i = random.randint(0, 500)
        j = random.randint(0, 500)
        const = random.randint(10, 60)
        self.qp.drawEllipse(i, j, const, const)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WindowDraw()
    ex.show()
    sys.exit(app.exec())
