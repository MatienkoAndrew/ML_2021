from create_portfolio_window import Ui_MainWindow as Create_Portfolio_window
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QMessageBox, QShortcut
from PyQt5 import QtWidgets
import pandas as pd
import requests
import pandas_datareader as pdr
import datetime

from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns

from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices
from PyQt5.QtCore import QAbstractTableModel, Qt

import plotly.graph_objects as go
import plotly.express as px
from PyQt5 import QtWebEngineWidgets
import okama as ok

'''
Окно "Создать портфель"
'''


def get_company_name(symbol):
    url = 'http://d.yimg.com/autoc.finance.yahoo.com/autoc?query=' + symbol + '&region=1&lang=en'
    result = requests.get(url).json()
    for r in result['ResultSet']['Result']:
        if r['symbol'] == symbol:
            return r['name']


class Create_Portfolio(QMainWindow):
    def __init__(self):
        super(Create_Portfolio, self).__init__()
        self.ui = Create_Portfolio_window()
        self.ui.setupUi(self)

        ##-- Переменные
        self.main = None
        self.weights = None
        self.ui.browser_page_4 = None
        self.ui.browser_page_5 = None
        self.ui.browser_page_6 = None
        self.all_tickers = set()
        self.company_names = list()

        ##-- Иконки на кнопки
        self.ui.btn_add.setIcon(QtGui.QIcon("images/add.png"))
        self.ui.button_back.setIcon(QtGui.QIcon("images/back.png"))

        ##-- Комбинация клавиш
        self.shortcut_create = QShortcut(QtGui.QKeySequence("Shift+Return"), self)
        self.shortcut_create.activated.connect(self.create_portfolio)

        ##-- Таблица
        self.ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.ui.progressBar.setVisible(False)
        self.initUI()

    def initUI(self):
        self.ui.button_back.clicked.connect(self.back)
        self.ui.btn_add.clicked.connect(self.add)
        self.ui.btn_create_portfolio.clicked.connect(self.create_portfolio)
        self.ui.btn_page_3.clicked.connect(self.plots)
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == Qt.Key_Return:
            self.add()
        if event.key() == Qt.Key_Tab:
            print("Tab")

    def add(self):
        ticker = self.ui.lineEdit.text()
        if ticker == '':
            return
        company_name = get_company_name(ticker)
        if company_name is None:
            QMessageBox.critical(self, "Ошибка ", "Данного тикера не существует", QMessageBox.Ok)
            return
        if ticker != '' and ticker not in self.all_tickers:
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)
            self.ui.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(ticker))
            self.ui.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(company_name))
            self.all_tickers.add(ticker)
            self.company_names.append(company_name)
            self.ui.lineEdit.setText("")

    def create_portfolio(self):
        if len(self.all_tickers) == 0:
            return
        self.ui.progressBar.setVisible(True)
        self.ui.progressBar.setValue(0)
        df = pd.DataFrame()

        all_tickers = list(self.all_tickers)
        num_all_tickers = len(all_tickers)
        part_each_ticker_progressBar = 90 / num_all_tickers
        for idx, symbol in enumerate(all_tickers):
            try:
                df[symbol] = pdr.get_data_yahoo(symbol, start=datetime.datetime(2006, 1, 1),
                                                end=datetime.datetime.now())["Adj Close"]
            except Exception as e:
                print(e)
                continue
            self.ui.progressBar.setValue((idx + 1) * part_each_ticker_progressBar)

        mu = expected_returns.mean_historical_return(df)
        S = risk_models.sample_cov(df)

        ef = EfficientFrontier(mu, S)
        ef.max_sharpe()
        cleaned_weights = ef.clean_weights()
        mu, sigma, sharpe = ef.portfolio_performance(verbose=False)

        portfolio_val = self.ui.spinBox.value()
        latest_prices = get_latest_prices(df)
        self.weights = cleaned_weights
        da = DiscreteAllocation(self.weights, latest_prices, total_portfolio_value=portfolio_val)
        allocation, leftover = da.greedy_portfolio()

        self.ui.progressBar.setValue(100)

        ##-- Page 2 <Parameters>
        from Pick_up_portfolio_class import pandasModel
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        self.ui.progressBar.setVisible(False)
        self.ui.label_2.setText("Ожидаемая годовая доходность: {:.1f}%\n"
                                "Годовая волатильность: {:.1f}%\n"
                                "Коэффициент Шарпа: {:.2f}\n"
                                "Остаток средств: {:.2f}$".format(100 * mu, 100 * sigma, sharpe, leftover))

        company_name = []
        for symbol in allocation:
            company_name.append(get_company_name(symbol))
        discrete_allocation_list = []
        for symbol in allocation:
            discrete_allocation_list.append(allocation.get(symbol))
        portfolio_df = pd.DataFrame(columns=['Название компании', 'Тикер компании', 'Количество активов'])
        portfolio_df['Название компании'] = company_name
        portfolio_df['Тикер компании'] = allocation
        portfolio_df['Количество активов'] = discrete_allocation_list
        portfolio_df = portfolio_df.sort_values(by='Количество активов', ascending=False)

        model = pandasModel(portfolio_df)
        self.ui.tableView.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.setModel(model)

    def plots(self):
        ##-- Page 3
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
        if self.weights is None or len(self.all_tickers) == 0:
            return
        tickers = [ticker + '.US' for ticker in self.all_tickers]
        weights = [weight for weight in self.weights.values()]
        portfolio_okama = ok.Portfolio(tickers, weights=weights, ccy='USD', last_date=datetime.datetime.now(), first_date="2006-01")

        self.ui.browser_page_4 = QtWebEngineWidgets.QWebEngineView(self)
        self.ui.stackedWidget_2.addWidget(self.ui.browser_page_4)
        self.ui.btn_page_4.clicked.connect(lambda: self.plot_forecast(portfolio_okama))
        self.ui.btn_page_5.clicked.connect(self.plot_assets)
        self.ui.btn_page_6.clicked.connect(self.plot_transition_map)
        # self.plot_forecast(portfolio_okama)
        pass

    def plot_forecast(self, portfolio, years: int = 1, percentiles=[10, 50, 90], distr="norm", n: int = 1000):
        wealth = portfolio.wealth_index
        x1 = portfolio.last_date
        x2 = x1.replace(year=x1.year + years)
        y_start_value = wealth["portfolio"].iloc[-1]
        y_end_values = portfolio.forecast_wealth(distr=distr, years=years, percentiles=percentiles, n=n)
        figure = go.Figure()
        figure.add_trace(
            go.Scatter(
                x=wealth.index.to_timestamp(),
                y=wealth["portfolio"],
                mode='lines',
                line=dict(width=1.5),
                name='Historical data'
            ))
        figure.update_layout(title='Прогнох портфеля', xaxis_title='Период времени', yaxis_title='$')
        for percentile in percentiles:
            x, y = [x1, x2], [y_start_value, y_end_values[percentile]]
            if percentile == 50:
                figure.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(width=2), name='Median'))
            else:
                figure.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(width=1, dash='dash'),
                                            name=f'Percentile {percentile}'))

        self.ui.browser_page_4.setHtml(figure.to_html(include_plotlyjs='cdn'))
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.browser_page_4)

    def plot_transition_map(self):
        tickers = [ticker + '.US' for ticker in self.all_tickers]
        portfolio = ok.EfficientFrontier(tickers)
        ef = portfolio.ef_points
        fig_transition_map = go.Figure()
        for ticker in tickers:
            fig_transition_map.add_trace(go.Scatter(x=ef.Risk,y=ef[ticker],mode='lines',name=ticker[:-3]))
        fig_transition_map.update_layout(title='Weights of stocks',xaxis_title='Risk (Volatility)',yaxis_title='Weights')
        self.ui.browser_page_4.setHtml(fig_transition_map.to_html(include_plotlyjs='cdn'))
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.browser_page_4)
        pass

    def plot_assets(self, kind: str = "cagr", pct_values=False):
        tickers = [ticker + '.US' for ticker in self.all_tickers]
        portfolio = ok.Plots(tickers, ccy='USD')
        risks = portfolio.risk_annual
        returns = portfolio.get_cagr().loc[portfolio.symbols]
        m = 100 if pct_values else 1
        figure_assets = go.Figure()
        asset_labels = portfolio.symbols
        for label, x, y in zip(asset_labels, risks, returns):
            figure_assets.add_trace(go.Scatter(x=[x * m], y=[y * m], mode="markers+text",
                                               text=label[:-3],
                                               marker=dict(size=10),
                                               showlegend=False,
                                               textposition="top center"))

        efficient = ok.EfficientFrontier(tickers)
        ef = efficient.ef_points
        figure_assets.add_trace(go.Scatter(x=ef.Risk, y=ef.CAGR, line=dict(width=3, dash='dash'),
                                           name="Граница эффективности",
                                           marker=dict(color='black')))
        figure_assets.update_layout(title='Доходность и риск каждого актива', xaxis_title='Риск', yaxis_title='Доходность')
        self.ui.browser_page_4.setHtml(figure_assets.to_html(include_plotlyjs='cdn'))
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.browser_page_4)

    def back(self):
        from Portfolio_class import Portfolio
        self.main = Portfolio()
        self.main.setWindowTitle("Stocker")
        self.main.setWindowIcon(QtGui.QIcon("images\portfolio.png"))
        self.main.show()
        self.close()
