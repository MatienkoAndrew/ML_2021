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
        textboxValue = self.ui.lineEdit.text()
        if textboxValue != '':
            try:
                stock = pdr.get_data_yahoo(textboxValue,
                                      start=datetime.datetime(2006, 10, 1),
                                      end=datetime.datetime.now())
                print(stock)
                self.show_in_window(stock)
            except Exception as e:
                print(e)

    # Изменение цены акций в процентах за квартал
    def plot_change_perc(self):
        textboxValue = self.ui.lineEdit.text()
        if textboxValue != '':
            stock = pdr.get_data_yahoo(textboxValue,
                                       start=datetime.datetime(2006, 10, 1),
                                       end=datetime.datetime.now())
            daily_close_px = stock['Adj Close']
            daily_pct_change = daily_close_px.pct_change()

            plot_month = self.ui.comboBox.currentText()
            quarter_pct_change = daily_pct_change.resample(f'{plot_month}M').mean()
            fig = px.bar(quarter_pct_change)
            fig.update_layout(
                title=self.ui.lineEdit.text(),
                xaxis_title="time",
                yaxis_title="pct_change",
                font=dict(
                    family="Courier New, monospace",
                    size=15,
                    color="RebeccaPurple"
                )
            )
            self.ui.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))
            self.ui.stackedWidget.setCurrentWidget(self.ui.browser)





