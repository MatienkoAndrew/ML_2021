from create_portfolio_window import Ui_MainWindow as Create_Portfolio_window
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QMessageBox
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
import plotly.express as px

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
        self.main = None
        self.ui.progressBar.setVisible(False)

        self.all_tickers = set()
        self.company_names = list()

        self.ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.initUI()

    def initUI(self):
        self.ui.button_back.clicked.connect(self.back)
        self.ui.btn_add.clicked.connect(self.add)
        self.ui.btn_create_portfolio.clicked.connect(self.create_portfolio)
        self.ui.btn_parameters.clicked.connect(self.parameters_portfolio)

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
        weights = ef.max_sharpe()
        cleaned_weights = ef.clean_weights()
        mu, sigma, sharpe = ef.portfolio_performance(verbose=False)

        portfolio_val = self.ui.spinBox.value()
        latest_prices = get_latest_prices(df)
        weights = cleaned_weights
        da = DiscreteAllocation(weights, latest_prices, total_portfolio_value=portfolio_val)
        allocation, leftover = da.greedy_portfolio()

        self.ui.progressBar.setValue(100)

        ##-- Page 2 <Parameters>
        from Pick_up_portfolio_class import pandasModel
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        self.ui.progressBar.setVisible(False)
        self.ui.label_2.setText("Expected annual return: {:.1f}%\n"
                                "Annual volatility: {:.1f}%\n"
                                "Sharpe Ratio: {:.2f}\n"
                                "Funds Remaining: {:.2f}$".format(100 * mu, 100 * sigma, sharpe, leftover))

        company_name = []
        for symbol in allocation:
            company_name.append(get_company_name(symbol))
        discrete_allocation_list = []
        for symbol in allocation:
            discrete_allocation_list.append(allocation.get(symbol))
        portfolio_df = pd.DataFrame(columns=['Company_name', 'Company_Ticker', 'Discrete_val_' + str(portfolio_val)])
        portfolio_df['Company_name'] = company_name
        portfolio_df['Company_Ticker'] = allocation
        portfolio_df['Discrete_val_' + str(portfolio_val)] = discrete_allocation_list
        portfolio_df = portfolio_df.sort_values(by='Discrete_val_' + str(portfolio_val), ascending=False)

        model = pandasModel(portfolio_df)
        self.ui.tableView.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.setModel(model)
        # self.ui.tableView.setHorizontalHeader()

    def parameters_portfolio(self):
        pass
        # ##-- Page 2 <Parameters>
        # from Pick_up_portfolio_class import pandasModel
        # self.ui.btn_create_portfolio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        # self.ui.progressBar.setVisible(False)
        # self.ui.label_2.setText("Expected annual return: {:.1f}%\n"
        #                         "Annual volatility: {:.1f}%\n"
        #                         "Sharpe Ratio: {:.2f}\n"
        #                         "Funds Remaining: {:.2f}$".format(100 * mu, 100 * sigma, sharpe, leftover))
        #
        # company_name = []
        # for symbol in allocation:
        #     company_name.append(get_company_name(symbol))
        # discrete_allocation_list = []
        # for symbol in allocation:
        #     discrete_allocation_list.append(allocation.get(symbol))
        # portfolio_df = pd.DataFrame(columns=['Company_name', 'Company_Ticker', 'Discrete_val_' + str(portfolio_val)])
        # portfolio_df['Company_name'] = company_name
        # portfolio_df['Company_Ticker'] = allocation
        # portfolio_df['Discrete_val_' + str(portfolio_val)] = discrete_allocation_list
        # portfolio_df = portfolio_df.sort_values(by='Discrete_val_' + str(portfolio_val), ascending=False)
        #
        # model = pandasModel(portfolio_df)
        # self.ui.tableView.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.ui.tableView.setModel(model)


    def back(self):
        from Portfolio_class import Portfolio
        self.main = Portfolio()
        self.main.setWindowTitle("Stocker")
        self.main.setWindowIcon(QtGui.QIcon("images\portfolio.png"))
        self.main.show()
        self.close()
