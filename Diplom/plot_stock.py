from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
import pandas_datareader as pdr
import datetime
import plotly.express as px
import sys, os
import plotly.offline
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtWebEngineWidgets

# from matplotlib.figure import Figure
# from matplotlib.animation import TimedAnimation
# from matplotlib.lines import Line2D
# from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("line_edit.ui", self)
        self.title = 'Тест'
        self.left = 200
        self.top = 200
        self.width = 400
        self.height = 140
        self.textbox = None
        self.browser = QtWebEngineWidgets.QWebEngineView(self)
        self.verticalLayout_3.addWidget(self.browser)
        # vlayout = QtWidgets.QVBoxLayout(self)
        # vlayout.addWidget(self.pushButton)
        # vlayout.addWidget(self.browser)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.pushButton.clicked.connect(self.on_click)
        self.show()

    def on_click(self):
        textboxValue = self.lineEdit.text()
        print(textboxValue)
        try:
            stock = pdr.get_data_yahoo(textboxValue, #'AAPL'
                                  start=datetime.datetime(2006, 10, 1),
                                  end=datetime.datetime.now())
            self.show_in_window(stock)
        except Exception as e:
            print(e)

    def show_in_window(self, stock):
        fig = px.line(x=stock.index, y=stock.Close)
        fig.update_layout(
            title=self.lineEdit.text(),
            xaxis_title="time",
            yaxis_title="Price",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="RebeccaPurple"
            )
        )
        # fig.update_traces(quartilemethod="exclusive")  # or "inclusive", or "linear" by default
        self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))

        # plotly.offline.plot(fig, filename='../name.html', auto_open=False)
        #
        # app1 = QApplication(sys.argv)
        # web = QWebEngineView()
        # file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../name.html"))
        # web.load(QUrl.fromLocalFile(file_path))
        # web.show()
        # sys.exit(app1.exec_())


class Test:
    def show_in_window(self, stock):
        plotly.offline.plot(fig, filename='../name.html', auto_open=False)

        app1 = QApplication(sys.argv)

        web = QWebEngineView()
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../name.html"))
        web.load(QUrl.fromLocalFile(file_path))
        web.show()
        sys.exit(app1.exec_())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.resize(1100, 800)
    widget.show()
    sys.exit(app.exec_())


