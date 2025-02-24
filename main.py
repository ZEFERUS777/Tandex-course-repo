import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QTableWidget, QWidget


class Add_Coffee(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('foem.ui', self)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.table: QTableWidget = self.table
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(
            ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах',
             'описание вкуса', 'цена', 'объем упаковки']
        )
        self.conn = sqlite3.connect('coffee.db')  # Сохраняем соединение
        self.curr = self.conn.cursor()
        self.setTable()
        self.table.resizeColumnsToContents()

        self.coff = None  # Переменная для хранения экземпляра Add_Coffee
        self.add_ac.clicked.connect(self.add_zapic)

    def setTable(self):
        try:
            result = self.curr.execute('SELECT * FROM coffee').fetchall()
            self.table.setRowCount(len(result))

            for row_idx, row in enumerate(result):
                for col_idx, value in enumerate(row):
                    self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        except sqlite3.Error as e:
            print(f"Ошибка при работе с базой данных: {e}")

    def add_zapic(self):
        if self.coff is None or not self.coff.isVisible():
            self.coff = Add_Coffee()
            self.coff.pushButton.clicked.connect(self.upt)  # Подключаем сигнал один раз
            self.coff.show()

    def upt(self):
        try:
            name = self.coff.lineEdit.text()
            ster = int(self.coff.lineEdit_2.text())
            ground_in_grains = self.coff.lineEdit_3.text()
            description = self.coff.lineEdit_4.text()
            price = int(self.coff.lineEdit_5.text())
            volume = int(self.coff.lineEdit_6.text())
            self.coff.close()

            # Используем обратные кавычки для имен столбцов с пробелами
            self.curr.execute(
                '''INSERT INTO coffee (`name of the variety`, `degree of roasting`, `ground/in grains`, 
                description, price, volume) VALUES (?, ?, ?, ?, ?, ?)''',
                (name, ster, ground_in_grains, description, price, volume))
            self.conn.commit()
            self.setTable()

        except Exception as e:
            print(e)

    def closeEvent(self, event):
        # Закрываем соединение с базой данных при закрытии главного окна
        self.conn.close()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
