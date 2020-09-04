from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

from crypto.gui.components.main_input.input_string import InputString
from crypto.gui.components.main_input.input_mode import InputMode


class TabString(QWidget):
    def __init__(self, parent: QWidget = None):
        super(TabString, self).__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.input_string = InputString()
        self.output_string = InputString()
        self.input_mode = InputMode()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.input_string)
        self.layout.addWidget(self.input_mode)
        self.layout.addWidget(self.output_string)

        self.setLayout(self.layout)
