from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore
from main import MainWindow
import pandas_datareader as pdr
import datetime
import plotly.express as px
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtCore, QtGui
import pandas as pd
import numpy as np
from plotly.validators.scatter.marker import SymbolValidator
import plotly.graph_objects as go


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
        self.ui.comboBox.setVisible(False)
        UIFunctions.simple_strategy_utils_not_visible(self)
        textboxValue = self.ui.lineEdit.text()
        if textboxValue != '':
            try:
                stock = pdr.get_data_yahoo(textboxValue,
                                      start=datetime.datetime(2006, 10, 1),
                                      end=datetime.datetime.now())
                print(stock)
                UIFunctions.show_in_window(self, stock)
            except Exception as e:
                print(e)

    def show_in_window(self, stock):
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=stock.index,
                y=stock['Adj Close'],
                mode='lines',
                # line=dict(width=4),
                name='Adj Close'
            ))
        fig.update_layout(
                title=self.ui.lineEdit.text(),
                xaxis_title="time",
                yaxis_title="Price",
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="RebeccaPurple"
                )
            )
        self.ui.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))
        self.ui.stackedWidget.setCurrentWidget(self.ui.browser)

    # Изменение цены акций в процентах за квартал
    def plot_change_perc(self):
        self.ui.comboBox.setVisible(True) ##-- делаю видимым только для графика изменения процентов
        UIFunctions.simple_strategy_utils_not_visible(self)

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

    # простая стратегия
    def simple_trade_strategy(self, company, short_window=40, long_window=100):
        short_window = short_window
        long_window = long_window

        signals = pd.DataFrame(index=company.index)
        signals['signal'] = 0.0
        signals['short_mavg'] = company['Adj Close'].rolling(window=short_window, min_periods=1, center=False).mean()
        signals['long_mavg'] = company['Adj Close'].rolling(window=long_window, min_periods=1, center=False).mean()

        signals['signal'][short_window:] = np.where(
            signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)
        signals['positions'] = signals['signal'].diff()
        return signals

    def plot_simple_strategy(self):
        self.ui.comboBox.setVisible(False)
        UIFunctions.simple_strategy_utils_visible(self)
        textboxValue = self.ui.lineEdit.text()
        if textboxValue != '':
            stock = pdr.get_data_yahoo(textboxValue,
                                       start=datetime.datetime(2006, 10, 1),
                                       end=datetime.datetime.now())

            short_window = self.ui.spinBox_short.value()
            self.ui.horizontalSlider_short.setValue(short_window)
            long_window = self.ui.spinBox_long.value()
            self.ui.horizontalSlider_long.setValue(long_window)
            try:
                signals_company = UIFunctions.simple_trade_strategy(self, stock, short_window, long_window)
                raw_symbols = SymbolValidator().values
                marker_triangle_up = raw_symbols[raw_symbols.index('triangle-up')]
                marker_triangle_down = raw_symbols[raw_symbols.index('triangle-down')]
                fig = go.Figure()
                fig.add_trace(
                    go.Scatter(
                        x=stock.index,
                        y=stock['Adj Close'],
                        mode='lines',
                        # line=dict(width=4),
                        name='Adj Close'
                    ))
                fig.add_trace(
                    go.Scatter(
                        x=signals_company.index,
                        y=signals_company['short_mavg'],
                        mode='lines',
                        name='short_mavg'
                    ))
                fig.add_trace(
                    go.Scatter(
                        x=signals_company.index,
                        y=signals_company['long_mavg'],
                        mode='lines',
                        name='long_mavg'
                    ))
                fig.add_trace(
                    go.Scatter(
                        x=signals_company.loc[signals_company.positions == 1.0].index,
                        y=signals_company.short_mavg[signals_company.positions == 1.0],
                        marker_symbol=marker_triangle_up,
                        mode='markers',
                        marker_size=10,
                        marker_color="yellowgreen",
                        name='buy'
                    ))
                fig.add_trace(
                    go.Scatter(
                        x=signals_company.loc[signals_company.positions == -1.0].index,
                        y=signals_company.short_mavg[signals_company.positions == -1.0],
                        marker_symbol=marker_triangle_down,
                        mode='markers',
                        marker_size=10,
                        marker_color="black",
                        name='sell'
                    ))
                fig.update_layout(
                    title=textboxValue + " simple strategy",
                    xaxis_title='Date',
                    yaxis_title='Price ($)'
                )
                # fig.show()

                self.ui.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))
                self.ui.stackedWidget.setCurrentWidget(self.ui.browser)
            except Exception as e:
                print(e)


    def simple_strategy_utils_not_visible(self):
        self.ui.lineEdit_long.setVisible(False)
        self.ui.spinBox_long.setVisible(False)
        self.ui.horizontalSlider_long.setVisible(False)
        self.ui.lineEdit_short.setVisible(False)
        self.ui.spinBox_short.setVisible(False)
        self.ui.horizontalSlider_short.setVisible(False)

    def simple_strategy_utils_visible(self):
        self.ui.lineEdit_long.setVisible(True)
        self.ui.spinBox_long.setVisible(True)
        self.ui.horizontalSlider_long.setVisible(True)
        self.ui.lineEdit_short.setVisible(True)
        self.ui.spinBox_short.setVisible(True)
        self.ui.horizontalSlider_short.setVisible(True)




