import sys
from toggle_menu import Ui_MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui_functions import *
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtCore, QtGui

import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # TOGGLE MENU
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        self.ui.btnFind.clicked.connect(lambda: UIFunctions.on_click(self))
        self.show()

    def show_in_window(self, stock):
        fig = px.line(x=stock.index, y=stock.Close)
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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
