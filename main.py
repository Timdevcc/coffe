import sqlite3
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5 import uic


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.curs = sqlite3.connect("coffe.db").cursor()
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.set_row()
    
    def set_row(self):
        res = self.curs.execute("select * from cof ").fetchall()
        self.tableWidget.setRowCount(len(res))
        for i, row in enumerate(res):
            for j, val in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())