from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsEllipseItem, QPushButton, QGraphicsView
from PyQt6.QtGui import QColor, QBrush
from PyQt6 import uic
import sys
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.drawButton = self.findChild(QPushButton, 'drawButton')
        self.drawArea = self.findChild(QGraphicsView, 'drawArea')
        self.scene = QGraphicsScene()
        self.drawArea.setScene(self.scene)
        self.drawButton.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(10, 100)
        view_width = self.drawArea.viewport().width()
        view_height = self.drawArea.viewport().height()
        max_x = max(view_width - diameter, 0)
        max_y = max(view_height - diameter, 0)
        x = random.randint(0, max_x) if max_x > 0 else 0
        y = random.randint(0, max_y) if max_y > 0 else 0
        ellipse = QGraphicsEllipseItem(x, y, diameter, diameter)
        ellipse.setBrush(QBrush(QColor(255, 255, 0)))
        self.scene.addItem(ellipse)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
