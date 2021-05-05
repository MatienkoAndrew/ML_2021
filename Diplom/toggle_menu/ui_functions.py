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
from stocker import Stocker

from PyQt5.QtCore import QThread
import time
import fbprophet


class PlotStock(QThread):
    def __init__(self, mainwindow, parent=None):
        super(PlotStock, self).__init__(parent)
        self.mainwindow = mainwindow
        self.fig_stock = None

    def run(self):
        textboxValue = self.mainwindow.ui.lineEdit.text()
        if textboxValue != '':
            try:
                stock = pdr.get_data_yahoo(textboxValue,
                                           start=datetime.datetime(2006, 10, 1),
                                           end=datetime.datetime.now())
                print(stock)
                self.show_in_window(stock)
            except Exception as e:
                print(e)

    def show_in_window(self, stock):
        self.fig_stock = go.Figure()
        self.fig_stock.add_trace(
            go.Scatter(
                x=stock.index,
                y=stock['Adj Close'],
                mode='lines',
                # line=dict(width=4),
                name='Adj Close'
            ))
        self.fig_stock.update_layout(
                title=self.mainwindow.ui.lineEdit.text(),
                xaxis_title="time",
                yaxis_title="Price",
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="RebeccaPurple"
                )
            )


class PlotVolatility(QThread):
    def __init__(self, mainwindow, parent=None):
        super(PlotVolatility, self).__init__(parent)
        self.mainwindow = mainwindow
        self.fig_vol = None

    def run(self):
        textboxValue = self.mainwindow.ui.lineEdit.text()
        if textboxValue != '':
            stock = pdr.get_data_yahoo(textboxValue,
                                       start=datetime.datetime(2006, 10, 1),
                                       end=datetime.datetime.now())
            daily_close_px = stock['Adj Close']
            daily_pct_change = daily_close_px.pct_change()

            plot_month = self.mainwindow.ui.comboBox.currentText()
            quarter_pct_change = daily_pct_change.resample(f'{plot_month}M').mean()
            self.fig_vol = px.bar(quarter_pct_change)
            self.fig_vol.update_layout(
                title=self.mainwindow.ui.lineEdit.text(),
                xaxis_title="time",
                yaxis_title="pct_change",
                font=dict(
                    family="Courier New, monospace",
                    size=15,
                    color="RebeccaPurple"
                )
            )


class PlotSimpleStrategy(QThread):
    def __init__(self, mainwindow, parent=None):
        super(PlotSimpleStrategy, self).__init__(parent)
        self.mainwindow = mainwindow
        self.fig_strategy = None

    # простая стратегия
    def simple_trade_strategy(self, company, short_window=40, long_window=100):
        short_window = short_window
        long_window = long_window

        signals = pd.DataFrame(index=company.index)
        signals['signal'] = 0.0
        signals['short_mavg'] = company['Adj Close'].rolling(window=short_window, min_periods=1,
                                                             center=False).mean()
        signals['long_mavg'] = company['Adj Close'].rolling(window=long_window, min_periods=1, center=False).mean()

        signals['signal'][short_window:] = np.where(
            signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)
        signals['positions'] = signals['signal'].diff()
        return signals

    def run(self):
        textboxValue = self.mainwindow.ui.lineEdit.text()
        if textboxValue != '':
            stock = pdr.get_data_yahoo(textboxValue,
                                       start=datetime.datetime(2006, 10, 1),
                                       end=datetime.datetime.now())

            short_window = self.mainwindow.ui.spinBox_short.value()
            self.mainwindow.ui.horizontalSlider_short.setValue(short_window)
            long_window = self.mainwindow.ui.spinBox_long.value()
            self.mainwindow.ui.horizontalSlider_long.setValue(long_window)
            try:
                signals_company = self.simple_trade_strategy(stock, short_window, long_window)
                raw_symbols = SymbolValidator().values
                marker_triangle_up = raw_symbols[raw_symbols.index('triangle-up')]
                marker_triangle_down = raw_symbols[raw_symbols.index('triangle-down')]
                self.fig_strategy = go.Figure()
                self.fig_strategy.add_trace(
                    go.Scatter(
                        x=stock.index,
                        y=stock['Adj Close'],
                        mode='lines',
                        # line=dict(width=4),
                        name='Adj Close'
                    ))
                self.fig_strategy.add_trace(
                    go.Scatter(
                        x=signals_company.index,
                        y=signals_company['short_mavg'],
                        mode='lines',
                        name='short_mavg'
                    ))
                self.fig_strategy.add_trace(
                    go.Scatter(
                        x=signals_company.index,
                        y=signals_company['long_mavg'],
                        mode='lines',
                        name='long_mavg'
                    ))
                self.fig_strategy.add_trace(
                    go.Scatter(
                        x=signals_company.loc[signals_company.positions == 1.0].index,
                        y=signals_company.short_mavg[signals_company.positions == 1.0],
                        marker_symbol=marker_triangle_up,
                        mode='markers',
                        marker_size=10,
                        marker_color="yellowgreen",
                        name='buy'
                    ))
                self.fig_strategy.add_trace(
                    go.Scatter(
                        x=signals_company.loc[signals_company.positions == -1.0].index,
                        y=signals_company.short_mavg[signals_company.positions == -1.0],
                        marker_symbol=marker_triangle_down,
                        mode='markers',
                        marker_size=10,
                        marker_color="black",
                        name='sell'
                    ))
                self.fig_strategy.update_layout(
                    title=textboxValue + " simple strategy",
                    xaxis_title='Date',
                    yaxis_title='Price ($)'
                )
            except Exception as e:
                print(e)


class PlotFBProphet(QThread):
    def __init__(self, mainwindow, parent=None, days=180):
        super(PlotFBProphet, self).__init__(parent)
        self.mainwindow = mainwindow
        self.fig_strategy = None
        self.days = days

    def run(self):
        model = fbprophet.Prophet(
            daily_seasonality=False,
            weekly_seasonality=False,
            yearly_seasonality=True,
            changepoint_prior_scale=0.05,
            changepoints=None,
        )
        model.add_seasonality(name="monthly", period=30.5, fourier_order=5)
        stock = pdr.get_data_yahoo(self.mainwindow.ui.lineEdit.text(), start=datetime.datetime(2006, 10, 1),
                                   end=datetime.datetime.now()).reset_index()
        stock["ds"] = stock["Date"]
        stock["y"] = stock["Adj Close"]
        max_date = max(stock["Date"])
        # Fit on the stock history for self.training_years number of years
        stock_history = stock[
            stock["Date"]
            > (max_date - pd.DateOffset(years=3))
            ]

        model.fit(stock_history)

        # Make and predict for next year with future dataframe
        future = model.make_future_dataframe(periods=self.days, freq="D")
        future = model.predict(future)

        title = "%s Historical and Predicted Stock Price" % self.mainwindow.ui.lineEdit.text()

        ##-- plotly
        self.fig_model = go.Figure([
            go.Scatter(x=stock_history["ds"],
                       y=stock_history["y"],
                       mode="lines", opacity=0.8,
                       name="Observations", line=dict(width=1.4, color='Black')),
            go.Scatter(x=future["ds"], y=future["yhat"],
                       name="Modeled", mode="lines", line=dict(width=2.4, color='Green')),
            go.Scatter(name="Upper Bound", x=future["ds"], y=future["yhat_upper"],
                       mode="lines", showlegend=False, line=dict(color='Green')),
            go.Scatter(name="Lower Bound", x=future["ds"], y=future["yhat_lower"],
                       mode="lines", fillcolor='rgba(67,255,1, 0.3)',
                       fill='tonexty', showlegend=False, line=dict(color='Green'))
        ])
        self.fig_model.update_layout(
            title=title,
            xaxis_title="Date",
            yaxis_title="Price",
            font=dict(
                family="Courier New, monospace",
                size=14,
                color="RebeccaPurple"
            )
        )


class UIFunctions(MainWindow):
    def toggleMenu(self, maxWidth, enable):
        if enable:
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            if width == 70:
                widthExtended = maxExtend
                self.ui.Btn_page_2.setText("Волатильность")
                self.ui.Btn_page_3.setText("Простая стратегия")
            else:
                widthExtended = standard
                self.ui.Btn_page_2.setText("Вола-\nтильность")
                self.ui.Btn_page_3.setText("Простая\nстратегия")

            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.start()

    def plot_stock_when_finish_thread(self):
        self.thread_plot_stock.finished.connect(lambda: UIFunctions.plot_stock(self))

    def plot_stock(self):
        UIFunctions.plot_stock_visible(self)
        self.ui.browser.setHtml(self.thread_plot_stock.fig_stock.to_html(include_plotlyjs='cdn'))
        self.ui.stackedWidget.setCurrentWidget(self.ui.browser)

    def plot_change_perc_finish_thread(self):
        self.thread_plot_volatility.finished.connect(lambda: UIFunctions.plot_change_perc(self))

    # Изменение цены акций в процентах за квартал
    def plot_change_perc(self):
        UIFunctions.plot_change_perc_visible(self)
        self.ui.browser.setHtml(self.thread_plot_volatility.fig_vol.to_html(include_plotlyjs='cdn'))
        self.ui.stackedWidget.setCurrentWidget(self.ui.browser)

    def plot_simple_strategy_finish_thread(self):
        self.thread_simple_strategy.finished.connect(lambda: UIFunctions.plot_simple_strategy(self))

    def plot_simple_strategy(self):
        UIFunctions.plot_simple_strategy_visible(self)
        self.ui.browser.setHtml(self.thread_simple_strategy.fig_strategy.to_html(include_plotlyjs='cdn'))
        self.ui.stackedWidget.setCurrentWidget(self.ui.browser)

    def plot_fbprophet_finish_thread(self):
        self.thread_plot_fbprophet.finished.connect(lambda: UIFunctions.plot_fbprophet(self))

    def plot_fbprophet(self):
        UIFunctions.plot_fbprophet_visible(self)
        self.ui.browser.setHtml(self.thread_plot_fbprophet.fig_model.to_html(include_plotlyjs='cdn'))
        self.ui.stackedWidget.setCurrentWidget(self.ui.browser)

    def simple_strategy_utils_not_visible(self):
        self.ui.lineEdit_long.setVisible(False)
        self.ui.spinBox_long.setVisible(False)
        self.ui.horizontalSlider_long.setVisible(False)
        self.ui.lineEdit_short.setVisible(False)
        self.ui.spinBox_short.setVisible(False)
        self.ui.horizontalSlider_short.setVisible(False)
        self.ui.spinBox_fbprophet.setVisible(False)

    def simple_strategy_utils_visible(self):
        self.ui.lineEdit_long.setVisible(True)
        self.ui.spinBox_long.setVisible(True)
        self.ui.horizontalSlider_long.setVisible(True)
        self.ui.lineEdit_short.setVisible(True)
        self.ui.spinBox_short.setVisible(True)
        self.ui.horizontalSlider_short.setVisible(True)

    def plot_stock_visible(self):
        self.ui.comboBox.setVisible(False)
        self.ui.button_fb.setVisible(False)
        UIFunctions.simple_strategy_utils_not_visible(self)

    def plot_change_perc_visible(self):
        self.ui.spinBox_fbprophet.setVisible(False)
        self.ui.comboBox.setVisible(True)
        UIFunctions.simple_strategy_utils_not_visible(self)

    def plot_simple_strategy_visible(self):
        self.ui.comboBox.setVisible(False)
        self.ui.spinBox_fbprophet.setVisible(False)
        self.ui.button_fb.setVisible(False)
        UIFunctions.simple_strategy_utils_visible(self)

    def plot_fbprophet_visible(self):
        self.ui.lineEdit_long.setVisible(False)
        self.ui.spinBox_long.setVisible(False)
        self.ui.horizontalSlider_long.setVisible(False)
        self.ui.lineEdit_short.setVisible(False)
        self.ui.spinBox_short.setVisible(False)
        self.ui.horizontalSlider_short.setVisible(False)
        self.ui.spinBox_fbprophet.setVisible(False)
        self.ui.comboBox.setVisible(False)
        self.ui.button_fb.setVisible(True)
        self.ui.spinBox_fbprophet.setVisible(True)
