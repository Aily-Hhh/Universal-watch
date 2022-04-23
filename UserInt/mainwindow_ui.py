# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(517, 362)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.current_time = QtWidgets.QLabel(self.centralwidget)
        self.current_time.setAlignment(QtCore.Qt.AlignCenter)
        self.current_time.setObjectName("current_time")
        self.current_time.setFont(QFont("Century Gothic", 19))
        self.verticalLayout.addWidget(self.current_time)
        self.timezone_cb = QtWidgets.QComboBox(self.centralwidget)
        self.timezone_cb.setObjectName("timezone_cb")
        self.verticalLayout.addWidget(self.timezone_cb)
        self.time_remaining = QtWidgets.QLabel(self.centralwidget)
        self.time_remaining.setText("")
        self.time_remaining.setAlignment(QtCore.Qt.AlignCenter)
        self.time_remaining.setObjectName("time_remaining")
        self.time_remaining.setFont(QFont("Century Gothic", 8))
        self.verticalLayout.addWidget(self.time_remaining)
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setObjectName("stop")
        self.verticalLayout.addWidget(self.stop)
        self.db_btn = QtWidgets.QPushButton(self.centralwidget)
        self.db_btn.setObjectName("db_btn")
        self.verticalLayout.addWidget(self.db_btn)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.at_time_rb = QtWidgets.QRadioButton(self.centralwidget)
        self.at_time_rb.setObjectName("at_time_rb")
        self.gridLayout.addWidget(self.at_time_rb, 0, 0, 1, 1)
        self.at_time = QtWidgets.QTimeEdit(self.centralwidget)
        self.at_time.setTime(QtCore.QTime(5, 0, 0))
        self.at_time.setObjectName("at_time")
        self.gridLayout.addWidget(self.at_time, 0, 1, 1, 1)
        self.through_time_rb = QtWidgets.QRadioButton(self.centralwidget)
        self.through_time_rb.setObjectName("through_time_rb")
        self.gridLayout.addWidget(self.through_time_rb, 1, 0, 1, 1)
        self.through_time = QtWidgets.QTimeEdit(self.centralwidget)
        self.through_time.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.through_time.setTime(QtCore.QTime(0, 10, 0))
        self.through_time.setObjectName("through_time")
        self.gridLayout.addWidget(self.through_time, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.audio_selection = QtWidgets.QPushButton(self.centralwidget)
        self.audio_selection.setObjectName("audio_selection")
        self.verticalLayout.addWidget(self.audio_selection)
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setObjectName("start")
        self.verticalLayout.addWidget(self.start)
        self.i_woke_up = QtWidgets.QPushButton(self.centralwidget)
        self.i_woke_up.setObjectName("i_woke_up")
        self.verticalLayout.addWidget(self.i_woke_up)
        self.more_sleep = QtWidgets.QPushButton(self.centralwidget)
        self.more_sleep.setObjectName("more_sleep")
        self.verticalLayout.addWidget(self.more_sleep)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Будильник"))
        self.current_time.setText(_translate("MainWindow", "Time"))
        self.db_btn.setText(_translate("MainWindow", "Мои будильники"))
        self.at_time_rb.setText(_translate("MainWindow", "Установить на"))
        self.at_time.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.through_time_rb.setText(_translate("MainWindow", "Проснуться через"))
        self.through_time.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.audio_selection.setText(_translate("MainWindow", "Выбрать трек"))
        self.start.setText(_translate("MainWindow", "Установить"))
        self.stop.setText(_translate("MainWindow", "Отключить"))
        self.i_woke_up.setText(_translate("MainWindow", "Я проснулся"))
        self.more_sleep.setText(_translate("MainWindow", "Еще поспать"))
        self.time_remaining.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
