# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(534, 323)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 30, 511, 281))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 0, 391, 26))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_ac = QtWidgets.QPushButton(parent=self.widget)
        self.add_ac.setObjectName("add_ac")
        self.horizontalLayout.addWidget(self.add_ac)
        self.save_ac = QtWidgets.QPushButton(parent=self.widget)
        self.save_ac.setObjectName("save_ac")
        self.horizontalLayout.addWidget(self.save_ac)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CoffeSellect"))
        self.add_ac.setText(_translate("MainWindow", "Добавить запись"))
        self.save_ac.setText(_translate("MainWindow", "Сохранить изменения"))
