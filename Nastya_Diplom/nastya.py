# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nastya.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QPropertyAnimation
import pandas as pd
from PyQt5.Qt import QProcess
from datetime import datetime
import os
import numpy as np
from about import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(525, 785)
        MainWindow.setMinimumSize(QtCore.QSize(525, 200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("QFrame {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 61))
        self.label.setStyleSheet("font: 75 26pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 231, 41))
        self.label_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.browse = QtWidgets.QPushButton(self.frame)
        self.browse.setGeometry(QtCore.QRect(310, 90, 201, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.browse.setFont(font)
        self.browse.setStyleSheet("QPushButton {\n"
"  background-color: rgb(209, 209, 209);\n"
"  border: none;\n"
"  color: black;\n"
"  padding: 16px 32px;\n"
"  text-align: center;\n"
"  font-size: 16px;\n"
"  margin: 4px 2px;\n"
"  opacity: 0.6;\n"
"  transition: 0.3s;\n"
"  display: inline-block;\n"
"  text-decoration: none;\n"
"  cursor: pointer;\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(156, 156, 156);\n"
"}")
        self.browse.setObjectName("browse")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 121, 61))
        self.label_3.setStyleSheet("font: 75 26pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 260, 381, 41))
        self.label_4.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.checkBox_8 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_8.setGeometry(QtCore.QRect(10, 310, 171, 41))
        self.checkBox_8.setStyleSheet("QCheckBox{\n"
"    font-size: 20px;\n"
"}\n"
"QCheckBox::indicator{\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_9.setGeometry(QtCore.QRect(10, 350, 221, 51))
        self.checkBox_9.setStyleSheet("QCheckBox{\n"
"    font-size: 20px;\n"
"}\n"
"QCheckBox::indicator{\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_10.setGeometry(QtCore.QRect(10, 400, 221, 41))
        self.checkBox_10.setStyleSheet("QCheckBox{\n"
"    font-size: 20px;\n"
"}\n"
"QCheckBox::indicator{\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_11.setGeometry(QtCore.QRect(10, 440, 241, 51))
        self.checkBox_11.setStyleSheet("QCheckBox{\n"
"    font-size: 20px;\n"
"}\n"
"QCheckBox::indicator{\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_12.setGeometry(QtCore.QRect(260, 310, 221, 41))
        self.checkBox_12.setStyleSheet("QCheckBox{\n"
"    font-size: 20px;\n"
"}\n"
"QCheckBox::indicator{\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_13.setGeometry(QtCore.QRect(260, 350, 241, 41))
        self.checkBox_13.setStyleSheet("QCheckBox{\n"
"    font-size: 20px;\n"
"}\n"
"QCheckBox::indicator{\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_14.setGeometry(QtCore.QRect(260, 400, 251, 41))
        self.checkBox_14.setStyleSheet("QCheckBox{\n"
"    font-size: 20px;\n"
"}\n"
"QCheckBox::indicator{\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_15 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_15.setGeometry(QtCore.QRect(260, 450, 161, 41))
        self.checkBox_15.setStyleSheet("QCheckBox{\n"
"    font-size: 20px;\n"
"}\n"
"QCheckBox::indicator{\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}")
        self.checkBox_15.setObjectName("checkBox_15")
        self.browse_2 = QtWidgets.QPushButton(self.frame)
        self.browse_2.setGeometry(QtCore.QRect(160, 520, 201, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.browse_2.setFont(font)
        self.browse_2.setStyleSheet("QPushButton {\n"
"  background-color: rgb(209, 209, 209);\n"
"  border: none;\n"
"  color: black;\n"
"  padding: 16px 32px;\n"
"  text-align: center;\n"
"  font-size: 16px;\n"
"  margin: 4px 2px;\n"
"  opacity: 0.6;\n"
"  transition: 0.3s;\n"
"  display: inline-block;\n"
"  text-decoration: none;\n"
"  cursor: pointer;\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(156, 156, 156);\n"
"}")
        self.browse_2.setObjectName("browse_2")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(20, 620, 491, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    background-color: rgb(195, 195, 195);\n"
"    border-radius: 10px;\n"
"    color: black;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    background-color:     qlineargradient(spread:pad, x1:1, y1:0.0227273, x2:0, y2:0, stop:0 rgba(0, 131, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.browse_3 = QtWidgets.QPushButton(self.frame)
        self.browse_3.setGeometry(QtCore.QRect(20, 680, 491, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.browse_3.setFont(font)
        self.browse_3.setStyleSheet("QPushButton {\n"
"  background-color: rgb(209, 209, 209);\n"
"  border: none;\n"
"  color: black;\n"
"  padding: 16px 32px;\n"
"  text-align: center;\n"
"  font-size: 16px;\n"
"  margin: 4px 2px;\n"
"  opacity: 0.6;\n"
"  transition: 0.3s;\n"
"  display: inline-block;\n"
"  text-decoration: none;\n"
"  cursor: pointer;\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(156, 156, 156);\n"
"}")
        self.browse_3.setObjectName("browse_3")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.name = None
        self.pressed = False
        self.animation = None
        self.algorithm()

        menuBar = MainWindow.menuBar()
        info = menuBar.addMenu('Программа')
        # info.triggered.connect(self.about)

        newFileAction = QtWidgets.QAction('О программе', MainWindow)
        info.addAction(newFileAction)
        info.triggered.connect(self.about)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def about(self):
        widget = QDialog()
        ui = Ui_Dialog()
        ui.setupUi(widget)
        widget.setFixedSize(400, 78)
        widget.setWindowTitle('О программе')
        widget.setWindowIcon(QIcon('icon.jpg'))
        widget.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Шаг 1"))
        self.label_2.setText(_translate("MainWindow", "Загрузите файл"))
        self.browse.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "Шаг 2"))
        self.label_4.setText(_translate("MainWindow", "Выберите нужные столбцы"))
        self.checkBox_8.setText(_translate("MainWindow", "Номенклатура"))
        self.checkBox_8.setChecked(True)
        self.checkBox_9.setText(_translate("MainWindow", "Классификатор\n"
                                                         "единиц измерения"))
        self.checkBox_9.setChecked(True)
        self.checkBox_10.setText(_translate("MainWindow", "Виды номенклатуры"))
        self.checkBox_10.setChecked(True)
        self.checkBox_11.setText(_translate("MainWindow", "Виды воспроизводства\n"
                                                          "номенклатуры"))
        self.checkBox_11.setChecked(True)
        self.checkBox_12.setText(_translate("MainWindow", "Количество единиц"))
        self.checkBox_13.setText(_translate("MainWindow", "Стандартное изделие"))
        self.checkBox_14.setText(_translate("MainWindow", "Полное наименование"))
        self.checkBox_15.setText(_translate("MainWindow", "Обозначение"))
        self.browse_2.setText(_translate("MainWindow", "Сохранить"))
        self.browse_3.setText(_translate("MainWindow", "Открыть папку с файлом"))

    def algorithm(self):
        self.create_new()
        self.browse.clicked.connect(self.browsefiles)
        self.browse_2.clicked.connect(self.create_file)

    def create_new(self):
        MainWindow.resize(300, 200)
        MainWindow.setMaximumSize(525, 785)
        self.label_3.setVisible(False)
        self.label_4.setVisible(False)
        self.checkBox_8.setVisible(False)
        self.checkBox_9.setVisible(False)
        self.checkBox_10.setVisible(False)
        self.checkBox_11.setVisible(False)
        self.checkBox_12.setVisible(False)
        self.checkBox_13.setVisible(False)
        self.checkBox_14.setVisible(False)
        self.checkBox_15.setVisible(False)
        self.browse_2.setVisible(False)
        self.progressBar.setVisible(False)
        self.browse_3.setVisible(False)

    def browsefiles(self):
        self.name = QFileDialog.getOpenFileName(MainWindow, 'Open file', 'G:\ML_2021\\Nastya_Diplom', 'Tables (*.xlsx , *.csv)')[0]
        print(self.name)
        self.pressed = True
        if self.pressed and self.name != '':
            # MainWindow.setFixedSize(525, 622)
            self.label_3.setVisible(True)
            self.label_4.setVisible(True)
            self.checkBox_8.setVisible(True)
            self.checkBox_9.setVisible(True)
            self.checkBox_10.setVisible(True)
            self.checkBox_11.setVisible(True)
            self.checkBox_12.setVisible(True)
            self.checkBox_13.setVisible(True)
            self.checkBox_14.setVisible(True)
            self.checkBox_15.setVisible(True)
            self.browse_2.setVisible(True)
            self.animation = QPropertyAnimation(MainWindow, b"minimumHeight")
            self.animation.setDuration(600)
            self.animation.setStartValue(200)
            self.animation.setEndValue(622)
            self.animation.start()

    def create_file(self):
        self.progressBar.setVisible(True)
        self.animation1 = QPropertyAnimation(MainWindow, b"minimumHeight")
        self.animation1.setDuration(300)
        self.animation1.setStartValue(622)
        self.animation1.setEndValue(675)
        self.animation1.start()

        self.progressBar.setValue(0)
        with open(self.name, 'r') as file:
            if "СТИК" in file.readline():
                df = pd.read_csv(self.name, skiprows=[0],
                                 sep=';', encoding='windows-1251')
            else:
                df = pd.read_csv(self.name, skiprows=[1],
                                 sep=';', encoding='windows-1251')
        len_columns = len(df.columns)
        self.progressBar.setValue(10)
        try:
            if self.checkBox_8.isChecked():
                df['Номенклатура'] = df['Наименование'] + ' ' + df['Обозначение']
        except KeyError:
            QMessageBox.critical(MainWindow, "Ошибка ",
                                 "Файл должен содержать колонки 'Наименование' и 'Обозначение'", QMessageBox.Ok)
            MainWindow.close()
        self.progressBar.setValue(20)
        try:
            if self.checkBox_9.isChecked():
                y = {'Штука': 'шт',
                     'Литр': 'л',
                     'Миллиграмм': 'мг',
                     'месяц': 'мес.',
                     'грамм': 'г',
                     'Единица': 'ед.',
                     'килограмм': 'кг',
                     'километр': 'км',
                     'километр квадратный': 'км2',
                     'метр': 'м',
                     'метр квадратный': 'м2',
                     'Метр кубический': 'м3',
                     'милиметр': 'мм',
                     'милиметр квадратный': 'мм2',
                     'милиметр кубический': 'мм3',
                     'киловатт': 'кВт.ч',
                     'комплект': 'компол',
                     'набор': 'наб.',
                     'рулон': 'рул.',
                     'упаковка': 'уп',
                     'ящик': 'ящ'
                     }
                df['Классификатор единиц измерения'] = df['Ед.изм.'].apply(
                    lambda x: x.replace(x, str(y[x])) if x in y.keys() else 'шт')
        except KeyError:
            df['Классификатор единиц измерения'] = np.nan

        self.progressBar.setValue(30)
        try:
            if self.checkBox_10.isChecked():
                z = {'Деталь': 'Детали',
                     'Материал': 'Материалы',
                     'Полуфабрикат': 'Полуфабрикаты',
                     'Продукция': 'Продукция',
                     'Прочее изделие': 'Прочие изделия',
                     'Сборочная единица': 'Сборочные единицы',
                     'Стандартное изделие': 'Стандартные изделия',
                     'Товар': 'Товар',
                     'Услуга': 'Услуга'
                     }
                df['Виды номенклатуры'] = df['Тип'].apply(
                    lambda x: x.replace(x, str(z[x])) if x in z.keys() else 'Прочие изделия')
        except KeyError:
            df['Виды номенклатуры'] = np.nan

        self.progressBar.setValue(40)
        try:
            if self.checkBox_11.isChecked():
                k = {'Изготовляемое': 'Производство',
                     'Покупное': 'Покупка',
                     'Не известно': 'Покупка'}
                df['Виды воспроизводства номенклатуры'] = df['Источник'].apply(lambda x: x.replace(x, str(k[x])))
        except KeyError:
            df['Виды воспроизводства номенклатуры'] = np.nan

        self.progressBar.setValue(50)
        try:
            if self.checkBox_12.isChecked():
                df['Количество единиц'] = df['Количество'].map('{0:g}'.format)
        except KeyError:
            df['Количество единиц'] = np.nan

        self.progressBar.setValue(60)
        try:
            if self.checkBox_13.isChecked():
                df['Стандартное'] = df['Стандартное'].astype(str)
                df['Стандартное изделие'] = df['Стандартное'].apply(lambda x: 'Нет' if x == 'nan' else x)
        except KeyError:
            df['Стандартное изделие'] = np.nan

        self.progressBar.setValue(70)
        try:
            if self.checkBox_14.isChecked():
                df['Полное наименование'] = df['Наименование'] + ' ' + df['Обозначение']
        except KeyError:
            df['Полное наименование'] = np.nan

        self.progressBar.setValue(80)
        try:
            if self.checkBox_15.isChecked():
                df = df.rename(columns={'Обозначение': 'Обозначение1'})
                df['Обозначение'] = df['Обозначение1']
        except KeyError:
            df['Обозначение'] = np.nan

        self.progressBar.setValue(90)
        df = df.drop(df.columns[:len_columns], axis=1)

        if not os.path.exists("Выгрузка"):
            os.makedirs("Выгрузка")

        current_datetime = datetime.now()
        current_datetime = str(current_datetime)[:-7]
        current_datetime = current_datetime.replace('-', '_')
        current_datetime = current_datetime.replace(':', '-')
        df.to_excel(f'Выгрузка\\Выгрузка_{current_datetime}.xlsx', index=False)
        self.progressBar.setValue(100)

        self.browse_3.setVisible(True)
        self.animation2 = QPropertyAnimation(MainWindow, b"minimumHeight")
        self.animation2.setDuration(300)
        self.animation2.setStartValue(675)
        self.animation2.setEndValue(785)
        self.animation2.start()
        self.browse_3.clicked.connect(self.open_directory)

    def open_directory(self):
        abs_path = os.getcwd()
        our_path = os.path.join(abs_path, 'Выгрузка')
        process = QProcess(MainWindow)
        process.start(f"explorer.exe {our_path}")
        MainWindow.close()

if __name__ == "__main__":
    import sys
    from PyQt5.QtGui import QIcon
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle('Обработчик файлов')
    MainWindow.setWindowIcon(QIcon('icon.jpg'))
    MainWindow.show()
    sys.exit(app.exec_())
