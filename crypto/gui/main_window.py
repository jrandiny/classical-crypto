from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout
from PyQt5.QtCore import QSize

from crypto.gui.components.algorithm_list import AlgorithmList
from crypto.gui.components.main_input import MainInput
from crypto.gui.components.configuration_box import ConfigurationBox
from crypto.engine.engine_factory import EngineType


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(869, 600)
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("central_widget")

        self.layout = QHBoxLayout()
        self.algorithm_list = AlgorithmList('Algorithm', EngineType.list(),
                                            self.central_widget)

        self.main_input = MainInput(self.central_widget)

        self.configuration_box = ConfigurationBox(self.central_widget)

        self.layout.addWidget(self.algorithm_list)
        self.layout.addWidget(self.main_input)
        self.layout.addWidget(self.configuration_box)

        self.central_widget.setLayout(self.layout)

        self.setCentralWidget(self.central_widget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)