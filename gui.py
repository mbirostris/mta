import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidget
from ui_pool import Ui_MainWindow
from main import load_pool


class SwimmingPoolWindow(QMainWindow):
    def __init__(self, parent=None):
        # super().__init__(parent)
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self._setupTableColumns()
        # self._setupTableRows()

    def _setupTableColumns(self):
        """
        Sets columns in the LanesMap depending on the Pool's lanes count.
        :return:
        """
        lanes = load_pool().lanes_number()
        self.ui.LanesMap.setColumnCount(lanes)

    # def _setupTableRows(self):
    #     """
    #     Sets rows in the LanesMap depending on the Pool's work hours.
    #     :return:
    #     """
    #     hours = SwimmingPool.work_hours()
    #
    # def calendarAction(self):
    #     self.ui.calendarWidget.clicked.connect()
    #     opr_date = self.ui.calendarWidget.selectedDate()


def guiMain(args):
    app = QApplication(args)
    window = SwimmingPoolWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)

