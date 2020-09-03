from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout
from PyQt5.QtCore import QSize

from crypto.gui.components.algorithm_list import AlgorithmList
from crypto.gui.components.main_input import MainInput
from crypto.gui.components.configuration import Configuration

list_of_algorithm = [
    'Playfair Cipher', 'Auto-key Vigenere Cipher', 'Full Vigenere Cipher',
    'Vigenere Cipher Standard ', 'Affine Cipher', 'Hill Cipher',
    'Extended Vigenere Cipher', 'Super Encryption', 'Enigma Cipher'
]


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

        self.algorithm_list = AlgorithmList('Algorithm', list_of_algorithm,
                                            QSize(241, 512),
                                            self.central_widget)

        self.main_input = MainInput(QSize(361, 531), self.central_widget)

        self.configuration = Configuration('Configuration', QSize(221, 521),
                                           self.central_widget)

        self.layout.addWidget(self.algorithm_list)
        self.layout.addWidget(self.main_input)
        self.layout.addWidget(self.configuration)

        self.central_widget.setLayout(self.layout)

        self.setCentralWidget(self.central_widget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)