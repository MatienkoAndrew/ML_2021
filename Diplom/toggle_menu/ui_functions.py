from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore
from main import MainWindow
import pandas_datareader as pdr
import datetime
import plotly.express as px
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtCore, QtGui

class UIFunctions(MainWindow):

    def toggleMenu(self, maxWidth, enable):
        if enable:
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.start()

    def on_click(self):

        self.ui.browser = QtWebEngineWidgets.QWebEngineView(self)
        # self.ui.verticalLayout_2.addWidget(self.ui.browser)
        self.ui.stackedWidget.addWidget(self.ui.browser)
        self.ui.stackedWidget.setCurrentWidget(self.ui.browser)
        textboxValue = self.ui.lineEdit.text()
        print(textboxValue)
        try:
            stock = pdr.get_data_yahoo(textboxValue,
                                  start=datetime.datetime(2006, 10, 1),
                                  end=datetime.datetime.now())
            print(stock)
            self.show_in_window(stock)
        except Exception as e:
            print(e)






