
(marta_term_project) C:\Users\marta\PycharmProjects\marta_term_project>python C:\Users\marta\anaconda3\envs\marta_term_project\Library\bin\pyside2-uic pool.ui 
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pool.ui',
# licensing of 'pool.ui' applies.
#
# Created: Wed Jan 12 21:56:35 2022
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 403)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LanesMap = QtWidgets.QTableWidget(self.centralwidget)
        self.LanesMap.setGeometry(QtCore.QRect(10, 10, 241, 291))
        self.LanesMap.setObjectName("LanesMap")
        self.LanesMap.setColumnCount(0)
        self.LanesMap.setRowCount(0)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(270, 10, 211, 151))
        self.calendarWidget.setObjectName("calendarWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 490, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
