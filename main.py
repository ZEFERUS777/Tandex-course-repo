from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6 import uic
import sqlite3
import sys


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.load_data()

    def load_data(self):
        try:
            conn = sqlite3.connect('coffee.sqlite')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM coffee")
            rows = cursor.fetchall()

            self.table.setRowCount(len(rows))
            self.table.setColumnCount(7)
            self.table.setHorizontalHeaderLabels([
                "ID", "Название", "Обжарка", "Тип",
                "Описание", "Цена", "Объем"
            ])

            for row_idx, row in enumerate(rows):
                for col_idx, value in enumerate(row):
                    self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

            conn.close()

        except sqlite3.Error as e:
            print("Database error:", e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())
