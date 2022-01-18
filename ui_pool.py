# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pool.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(529, 403)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(260, 20, 261, 181))
        self.ReportButton = QPushButton(self.centralwidget)
        self.ReportButton.setObjectName(u"ReportButton")
        self.ReportButton.setGeometry(QRect(10, 330, 241, 21))
        self.PoolName = QLabel(self.centralwidget)
        self.PoolName.setObjectName(u"PoolName")
        self.PoolName.setGeometry(QRect(0, 0, 541, 21))
        self.PoolName.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 20, 258, 301))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.LanesOccupancy = QLabel(self.widget)
        self.LanesOccupancy.setObjectName(u"LanesOccupancy")

        self.verticalLayout.addWidget(self.LanesOccupancy)

        self.LanesMap = QTableWidget(self.widget)
        self.LanesMap.setObjectName(u"LanesMap")

        self.verticalLayout.addWidget(self.LanesMap)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 529, 18))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ReportButton.setText(QCoreApplication.translate("MainWindow", u"GENERATE DAILY REPORT", None))
        self.PoolName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.LanesOccupancy.setText(QCoreApplication.translate("MainWindow", u"LANES OCCUPANCY", None))
    # retranslateUi

