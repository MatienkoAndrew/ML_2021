from toggle_menu import Ui_MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui_functions import *
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWebEngineWidgets
from PyQt5.Qt import Qt
import sys
import time
# import OpenGL

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.browser = QtWebEngineWidgets.QWebEngineView(self)
        self.ui.stackedWidget.addWidget(self.ui.browser)

        ##-- Видимость
        self.ui.comboBox.setVisible(False)
        UIFunctions.simple_strategy_utils_not_visible(self)
        self.ui.button_fb.setVisible(False)

        # Смена значений
        ##-- меняется значение в ComboBox - перестраивается график
        self.ui.comboBox.currentIndexChanged.connect(lambda: self.thread_plot_volatility.start())
        self.ui.comboBox.currentIndexChanged.connect(lambda: UIFunctions.plot_change_perc_finish_thread(self))

        ##-- меняется значение в Short - перестраивается график
        self.ui.spinBox_short.valueChanged.connect(self.spinBox_short_changed)
        self.ui.horizontalSlider_short.valueChanged.connect(self.slider_short_changed)
        self.ui.spinBox_long.valueChanged.connect(self.spinBox_long_changed)
        self.ui.horizontalSlider_long.valueChanged.connect(self.slider_long_changed)
        ##-- меняется значение в spinBox_fbprophet - перестраивается график
        self.ui.button_fb.clicked.connect(self.spinBox_fb_changed)

        ## Потоки
        self.thread_plot_stock = PlotStock(mainwindow=self)
        self.thread_plot_volatility = PlotVolatility(mainwindow=self)
        self.thread_simple_strategy = PlotSimpleStrategy(mainwindow=self)
        self.thread_plot_fbprophet = PlotFBProphet(mainwindow=self)

        # TOGGLE MENU
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        self.ui.btnFind.clicked.connect(self.threads_start)
        self.ui.btnFind.clicked.connect(lambda: UIFunctions.plot_stock_when_finish_thread(self))
        self.ui.Btn_page_1.clicked.connect(lambda: UIFunctions.plot_stock(self))
        self.ui.Btn_page_2.clicked.connect(lambda: UIFunctions.plot_change_perc(self))
        self.ui.Btn_page_3.clicked.connect(lambda: UIFunctions.plot_simple_strategy(self))
        self.ui.Btn_page_4.clicked.connect(lambda: UIFunctions.plot_fbprophet(self))
        self.show()

    ## Запуск всех потоков нажатием кнопки "Find"
    def threads_start(self):
        self.thread_plot_stock.start()
        self.thread_plot_volatility.start()
        self.thread_simple_strategy.start()
        self.thread_plot_fbprophet.start()

    def spinBox_short_changed(self):
        try:
            new_short_value = self.ui.spinBox_short.value()
            self.ui.horizontalSlider_short.setValue(new_short_value)
            self.thread_simple_strategy.start()
            UIFunctions.plot_simple_strategy_finish_thread(self)
        except Exception as e:
            print(e)

    def spinBox_long_changed(self):
        try:
            new_long_value = self.ui.spinBox_long.value()
            self.ui.horizontalSlider_long.setValue(new_long_value)
            self.thread_simple_strategy.start()
            UIFunctions.plot_simple_strategy_finish_thread(self)
        except Exception as e:
            print(e)

    def slider_short_changed(self):
        try:
            self.ui.spinBox_short.setValue(self.ui.horizontalSlider_short.value())
        except Exception as e:
            print(e)

    def slider_long_changed(self):
        try:
            self.ui.spinBox_long.setValue(self.ui.horizontalSlider_long.value())
        except Exception as e:
            print(e)

    def spinBox_fb_changed(self):
        try:
            new_value = self.ui.spinBox_fbprophet.value()
            self.ui.spinBox_fbprophet.setValue(new_value)
            self.thread_plot_fbprophet.days = new_value
            self.thread_plot_fbprophet.start()
            UIFunctions.plot_fbprophet_finish_thread(self)
        except Exception as e:
            print(e)

    # def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
    #     if event.key() == Qt.Key_Enter:
    #         UIFunctions.toggleMenu(self, 250, True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
