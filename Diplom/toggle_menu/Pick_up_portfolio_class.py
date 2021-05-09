from PyQt5.QtWidgets import QMainWindow, QHeaderView
from pick_up_portfolio import Ui_MainWindow as Pick_up_portfolio_window
from PyQt5 import QtGui
from PyQt5.QtCore import QAbstractTableModel, Qt
import pandas as pd
import requests
from PyPortfolioOpt.pypfopt.efficient_frontier import EfficientFrontier
from PyPortfolioOpt.pypfopt import risk_models
from PyPortfolioOpt.pypfopt import expected_returns
from PyPortfolioOpt.pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

import warnings
warnings.filterwarnings('ignore')


class pandasModel(QAbstractTableModel):
    def __init__(self, data):
        super(pandasModel, self).__init__()
        self._data = data

    def rowCount(self, parent=None) -> int:
        return self._data.shape[0]

    def columnCount(self, parent=None) -> int:
        return self._data.shape[1]

    def data(self, index, role: int = Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role==Qt.DisplayRole:
            return self._data.columns[col]
        return None


'''
Подобрать портфель
'''


class PickUpPortfolio(QMainWindow):
    def __init__(self):
        super(PickUpPortfolio, self).__init__()
        self.ui = Pick_up_portfolio_window()
        self.ui.setupUi(self)
        self.portfolio = None
        self.initUI()

    def initUI(self):
        self.ui.pushButton.clicked.connect(self.get_portfolio)
        self.ui.backButton.clicked.connect(self.back)

    def get_portfolio(self):
        df = pd.read_csv('../datasets/tickers.csv')
        df = df.set_index(pd.DatetimeIndex(df['Date'].values))
        df.drop('Date', axis=1, inplace=True)
        assets = df.columns
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
        allocation, leftover = da.greedy_portfolio()  # allocation, leftover = da.lp_portfolio(solver='ECOS_BB')

        self.ui.label_2.setText("Expected annual return: {:.1f}%\n"
                                "Annual volatility: {:.1f}%\n"
                                "Sharpe Ratio: {:.2f}\n"
                                "Funds Remaining: {:.2f}$".format(100 * mu, 100 * sigma, sharpe, leftover))
        company_name = []
        for symbol in allocation:
            company_name.append(self.get_company_name(symbol))

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
        pass

    def get_company_name(self, symbol):
        url = 'http://d.yimg.com/autoc.finance.yahoo.com/autoc?query=' + symbol + '&region=1&lang=en'
        result = requests.get(url).json()
        for r in result['ResultSet']['Result']:
            if r['symbol'] == symbol:
                return r['name']

    def back(self):
        from main import Portfolio

        self.portfolio = Portfolio()
        self.portfolio.setWindowTitle("Stocker")
        self.portfolio.setWindowIcon(QtGui.QIcon("images\portfolio.png"))
        self.portfolio.show()
        self.close()
