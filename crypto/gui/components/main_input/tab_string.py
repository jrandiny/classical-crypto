from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout

from crypto.gui.components.main_input.input_string import InputString
from crypto.gui.components.main_input.toggle_button import ToggleButton


class TabString(QWidget):
    def __init__(self, parent: QWidget = None):
        super(TabString, self).__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.input = InputString()
        self.output = InputString()
        self.mode_toggle = ToggleButton(['Encrypt', 'Decrypt'])
        self.btn_execute = QPushButton('Execute')

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.mode_toggle)
        self.h_layout.addWidget(self.btn_execute)
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.input)
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.output)

        self.setLayout(self.v_layout)
