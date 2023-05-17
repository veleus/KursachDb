# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accidentsMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        MainWindow.setSizeIncrement(QtCore.QSize(1000, 600))
        MainWindow.setBaseSize(QtCore.QSize(1000, 600))
        MainWindow.setStyleSheet("\n"
"background-color: rgb(132, 37, 200);\n"
"font: 75 12pt \"Fixedsys\";\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 981, 351))
        self.tableWidget.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"border-radius: 5px;")
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.Dell = QtWidgets.QPushButton(self.centralwidget)
        self.Dell.setGeometry(QtCore.QRect(20, 470, 111, 31))
        self.Dell.setStyleSheet("background-color: rgb(255, 207, 64);\n"
"")
        self.Dell.setObjectName("Dell")
        self.Add = QtWidgets.QPushButton(self.centralwidget)
        self.Add.setGeometry(QtCore.QRect(20, 390, 111, 31))
        self.Add.setStyleSheet("background-color: rgb(255, 207, 64);\n"
"")
        self.Add.setObjectName("Add")
        self.Change = QtWidgets.QPushButton(self.centralwidget)
        self.Change.setGeometry(QtCore.QRect(20, 430, 111, 31))
        self.Change.setStyleSheet("background-color: rgb(255, 207, 64);\n"
"")
        self.Change.setObjectName("Change")
        self.Open = QtWidgets.QPushButton(self.centralwidget)
        self.Open.setGeometry(QtCore.QRect(20, 550, 111, 31))
        self.Open.setStyleSheet("background-color: rgb(255, 207, 64);\n"
"")
        self.Open.setObjectName("Open")
        self.Sort = QtWidgets.QPushButton(self.centralwidget)
        self.Sort.setGeometry(QtCore.QRect(20, 510, 111, 31))
        self.Sort.setStyleSheet("background-color: rgb(255, 207, 64);\n"
"")
        self.Sort.setObjectName("Sort")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(900, 580, 101, 20))
        self.Back.setStyleSheet("background-color: rgb(255, 207, 64);\n"
"")
        self.Back.setObjectName("Back")
        self.DellLine = QtWidgets.QLineEdit(self.centralwidget)
        self.DellLine.setGeometry(QtCore.QRect(140, 470, 101, 31))
        self.DellLine.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"border-radius: 5px;")
        self.DellLine.setObjectName("DellLine")
        self.AddLine = QtWidgets.QLineEdit(self.centralwidget)
        self.AddLine.setGeometry(QtCore.QRect(140, 390, 101, 31))
        self.AddLine.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"border-radius: 5px;")
        self.AddLine.setObjectName("AddLine")
        self.AddLine_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.AddLine_1.setGeometry(QtCore.QRect(250, 390, 101, 31))
        self.AddLine_1.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"border-radius: 5px;")
        self.AddLine_1.setObjectName("AddLine_1")
        self.AddLine_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.AddLine_2.setGeometry(QtCore.QRect(360, 390, 101, 31))
        self.AddLine_2.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"border-radius: 5px;")
        self.AddLine_2.setObjectName("AddLine_2")
        self.AddLine_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.AddLine_3.setGeometry(QtCore.QRect(480, 390, 101, 31))
        self.AddLine_3.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"border-radius: 5px;")
        self.AddLine_3.setObjectName("AddLine_3")
        self.AddLine_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.AddLine_4.setGeometry(QtCore.QRect(590, 390, 101, 31))
        self.AddLine_4.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"border-radius: 5px;")
        self.AddLine_4.setObjectName("AddLine_4")
        self.ChangeLine_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.ChangeLine_4.setGeometry(QtCore.QRect(580, 430, 101, 31))
        self.ChangeLine_4.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"border-radius: 5px;")
        self.ChangeLine_4.setObjectName("ChangeLine_4")
        self.ChangeLine_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.ChangeLine_1.setGeometry(QtCore.QRect(250, 430, 101, 31))
        self.ChangeLine_1.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"border-radius: 5px;")
        self.ChangeLine_1.setObjectName("ChangeLine_1")
        self.ChangeLine_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.ChangeLine_2.setGeometry(QtCore.QRect(360, 430, 101, 31))
        self.ChangeLine_2.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"border-radius: 5px;")
        self.ChangeLine_2.setObjectName("ChangeLine_2")
        self.ChangeLine_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.ChangeLine_3.setGeometry(QtCore.QRect(470, 430, 101, 31))
        self.ChangeLine_3.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"border-radius: 5px;")
        self.ChangeLine_3.setObjectName("ChangeLine_3")
        self.ChangeLine = QtWidgets.QLineEdit(self.centralwidget)
        self.ChangeLine.setGeometry(QtCore.QRect(140, 430, 101, 31))
        self.ChangeLine.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"border-radius: 5px;")
        self.ChangeLine.setObjectName("ChangeLine")
        self.ChangeLine_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.ChangeLine_5.setGeometry(QtCore.QRect(690, 430, 101, 31))
        self.ChangeLine_5.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"border-radius: 5px;")
        self.ChangeLine_5.setObjectName("ChangeLine_5")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(140, 510, 101, 31))
        self.lineEdit_13.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"border-radius: 5px;")
        self.lineEdit_13.setObjectName("lineEdit_13")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Accidents"))
        self.Dell.setText(_translate("MainWindow", "Удалить"))
        self.Add.setText(_translate("MainWindow", "Добавть"))
        self.Change.setText(_translate("MainWindow", "Изменить"))
        self.Open.setText(_translate("MainWindow", "Открыть"))
        self.Sort.setText(_translate("MainWindow", "Сортировать"))
        self.Back.setText(_translate("MainWindow", "Назад"))
