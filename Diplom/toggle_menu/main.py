import sys
from toggle_menu import Ui_MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui_functions import *
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWebEngineWidgets
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.browser = QtWebEngineWidgets.QWebEngineView(self)
        # self.ui.verticalLayout_2.addWidget(self.ui.browser)
        self.ui.stackedWidget.addWidget(self.ui.browser)

        self.ui.comboBox.currentIndexChanged.connect(lambda: UIFunctions.plot_change_perc(self))
        # TOGGLE MENU
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        self.ui.btnFind.clicked.connect(lambda: UIFunctions.on_click(self))
        self.ui.Btn_page_1.clicked.connect(lambda: UIFunctions.on_click(self))
        self.ui.Btn_page_2.clicked.connect(lambda: UIFunctions.plot_change_perc(self))
        self.show()

    def show_in_window(self, stock):
        fig = px.line(x=stock.index, y=stock['Adj Close'])
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
        # fig.update_traces(quartilemethod="exclusive")  # or "inclusive", or "linear" by default
        self.ui.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))
        self.ui.stackedWidget.setCurrentWidget(self.ui.browser)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
