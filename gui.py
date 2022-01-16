import sys
from PySide2.QtUiTools import QUiLoader
from PySide2 import QtWidgets, QMainWindow
from PySide2.QtWidgets import QApplication, QDialog, QTableWidget
from ui_pool import Ui_MainWindow
from swimming_pool import SwimmingPool


class SwimmingPoolWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._setupTableColumns()
        self._setupTableRows()

    def _setupTableColumns(self):
        """
        Sets columns in the LanesMap depending on the Pool's lanes count.
        :return:
        """
        lanes = SwimmingPool.lanes_number()
        self.ui.LanesMap.setColumnCount(lanes)

    def _setupTableRows(self):
        """
        Sets rows in the LanesMap depending on the Pool's work hours.
        :return:
        """
        hours = SwimmingPool.work_hours()

    def calendarAction(self):
        self.ui.calendarWidget.clicked.connect()
        opr_date = self.ui.calendarWidget.selectedDate()

    def


def guiMain(args):
    app = QtWidgets.QApplication(args)
    window = QUiLoader.load("table.ui", None)
    window = SwimmingPoolWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)

