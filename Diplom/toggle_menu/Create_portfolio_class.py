from create_portfolio_window import Ui_MainWindow as Create_Portfolio_window
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QMessageBox
from PyQt5 import QtWidgets
import requests

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

        self.all_tickers = set()

        self.ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.initUI()

    def initUI(self):
        self.ui.button_back.clicked.connect(self.back)
        self.ui.btn_add.clicked.connect(self.add)

    def add(self):
        ticker = self.ui.lineEdit.text()
        company_name = get_company_name(ticker)
        error = 0
        if company_name is None:
            QMessageBox.critical(self, "Ошибка ", "Данного тикера не существует", QMessageBox.Ok)
            error = 1
        if ticker != '' and ticker not in self.all_tickers and error == 0:
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)
            self.ui.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(ticker))
            self.ui.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(company_name))
            self.all_tickers.add(ticker)

    def back(self):
        from Portfolio_class import Portfolio
        self.main = Portfolio()
        self.main.setWindowTitle("Stocker")
        self.main.setWindowIcon(QtGui.QIcon("images\portfolio.png"))
        self.main.show()
        self.close()
