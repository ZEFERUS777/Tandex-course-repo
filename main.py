from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGraphicsScene,
    QGraphicsEllipseItem,
    QPushButton,
    QGraphicsView,
    QVBoxLayout,
    QWidget
)
from PyQt6.QtGui import QColor, QBrush
import sys
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Random Circles")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)

        self.drawButton = QPushButton("Добавить окружность")
        self.drawArea = QGraphicsView()

        self.scene = QGraphicsScene()
        self.drawArea.setScene(self.scene)

        self.layout.addWidget(self.drawButton)
        self.layout.addWidget(self.drawArea)

        self.setCentralWidget(self.central_widget)
        self.drawButton.clicked.connect(self.add_circle)

    def add_circle(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        diameter = random.randint(10, 100)
        view_width = self.drawArea.viewport().width()
        view_height = self.drawArea.viewport().height()
        max_x = max(view_width - diameter, 0)
        max_y = max(view_height - diameter, 0)

        x = random.randint(0, max_x) if max_x > 0 else 0
        y = random.randint(0, max_y) if max_y > 0 else 0

        ellipse = QGraphicsEllipseItem(x, y, diameter, diameter)
        ellipse.setBrush(QBrush(QColor(r, g, b)))
        self.scene.addItem(ellipse)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
