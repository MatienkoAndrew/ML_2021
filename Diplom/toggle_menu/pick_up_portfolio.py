# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\ui\pick_up_portfolio.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 650)
        MainWindow.setMinimumSize(QtCore.QSize(500, 650))
        MainWindow.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 100))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Times New Roman\";")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    color: #FFF;\n"
"    background-color: rgb(62, 180, 158);\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 1px solid rgb(48, 50, 62);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(162, 180, 158);\n"
"    padding-top: 5px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 2, 1)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 3, 0, 1, 3)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setMinimumSize(QtCore.QSize(0, 76))
        self.backButton.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    color: #FFF;\n"
"    background-color: rgb(62, 180, 158);\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 1px solid rgb(48, 50, 62);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(162, 180, 158);\n"
"    padding-top: 5px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/back1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(60, 60))
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 5, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(90, 50))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MingLiU_HKSCS-ExtB\";\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setEnabled(True)
        self.spinBox.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("MingLiU_HKSCS-ExtB")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MingLiU_HKSCS-ExtB\";")
        self.spinBox.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhLatinOnly)
        self.spinBox.setWrapping(False)
        self.spinBox.setFrame(False)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox.setSpecialValueText("")
        self.spinBox.setMaximum(999999999)
        self.spinBox.setProperty("value", 1000)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Подобрать"))
        self.backButton.setText(_translate("MainWindow", "Вернуться"))
        self.label.setText(_translate("MainWindow", "Money,$:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
