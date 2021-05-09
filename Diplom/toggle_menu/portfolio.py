# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'portfolio.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(500, 0))
        self.frame.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(300, 80))
        self.frame_2.setStyleSheet("QFrame {\n"
"    border: 2px solid rgb(35,35,35);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(35, 35, 35);\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.button_pick_up = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pick_up.sizePolicy().hasHeightForWidth())
        self.button_pick_up.setSizePolicy(sizePolicy)
        self.button_pick_up.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_pick_up.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 20px;\n"
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
        icon.addPixmap(QtGui.QPixmap("images/robot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_pick_up.setIcon(icon)
        self.button_pick_up.setIconSize(QtCore.QSize(60, 60))
        self.button_pick_up.setObjectName("button_pick_up")
        self.verticalLayout_3.addWidget(self.button_pick_up)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(300, 80))
        self.frame_3.setStyleSheet("QFrame {\n"
"    border: 2px solid rgb(35,35,35);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(35, 35, 35);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_create = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_create.sizePolicy().hasHeightForWidth())
        self.button_create.setSizePolicy(sizePolicy)
        self.button_create.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 20px;\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/coin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_create.setIcon(icon1)
        self.button_create.setIconSize(QtCore.QSize(60, 60))
        self.button_create.setAutoRepeat(False)
        self.button_create.setObjectName("button_create")
        self.gridLayout_2.addWidget(self.button_create, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(300, 80))
        self.frame_4.setStyleSheet("QFrame {\n"
"    border: 2px solid rgb(35,35,35);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(35, 35, 35);\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.button_back = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_back.sizePolicy().hasHeightForWidth())
        self.button_back.setSizePolicy(sizePolicy)
        self.button_back.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 20px;\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_back.setIcon(icon2)
        self.button_back.setIconSize(QtCore.QSize(60, 60))
        self.button_back.setObjectName("button_back")
        self.gridLayout_3.addWidget(self.button_back, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_4, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_pick_up.setText(_translate("MainWindow", "Подобрать портфель"))
        self.button_create.setText(_translate("MainWindow", "Создать портфель"))
        self.button_back.setText(_translate("MainWindow", "Вернуться"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
