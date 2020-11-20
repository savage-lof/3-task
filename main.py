import random
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from ui_file import Ui_MainWindow



class WindowDraw(QWidget):
    def init(self):
        super().init()
        self.setupUi(self)
        self.setMouseTracking(True)
        self.coord = []
        self.attr = None


    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.draw(self.attr)
        self.qp.end()


    def draw(self, attr):
        const = random.randint(10, 200)
        mass = [i for i in range(0, 256)]
        self.qp.setBrush(QColor(random.choice(mass), random.choice(mass), random.choice(mass)))
        if attr == 'left':
            self.qp.drawEllipse(*self.coord, const, const)
        elif attr == 'right':
            self.qp.drawRect(*self.coord, const, const)
        elif attr == 'space':
            self.qp.drawPolygon(QPoint(self.coord[0] - (const * 1.3), self.coord[1]),
                                QPoint(self.coord[0] + const, self.coord[1] + const),
                                QPoint(self.coord[0] + const, self.coord[1] - const))

    def mouseMoveEvent(self, event):
        self.coord = [event.x(), event.y()]

    def mousePressEvent(self, event):
        self.coord = [event.x(), event.y()]
        if event.button() == Qt.LeftButton:
            self.attr = 'left'
        elif event.button() == Qt.RightButton:
            self.attr = 'right'
        self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.attr = 'space'
        self.update()


if name == 'main':
    app = QApplication(sys.argv)
    ex = WindowDraw()
    ex.show()
    sys.exit(app.exec())