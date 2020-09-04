from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

from crypto.gui.components.main_input.input_string import InputString


class TabString(QWidget):
    def __init__(self, parent: QWidget = None):
        super(TabString, self).__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.input = InputString()
        self.output = InputString()
        self.btn_switch = QPushButton('Switch Mode')
        self.btn_execute = QPushButton('Execute')
        self.lbl_mode_title = QLabel('Mode:')
        self.lbl_mode_value = QLabel('Encrypt')

        self.h_layout_1 = QHBoxLayout()
        self.h_layout_2 = QHBoxLayout()
        self.h_layout_1.addWidget(self.lbl_mode_title)
        self.h_layout_1.addWidget(self.lbl_mode_value)
        self.h_layout_2.addWidget(self.btn_switch)
        self.h_layout_2.addWidget(self.btn_execute)
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.input)
        self.v_layout.addLayout(self.h_layout_1)
        self.v_layout.addLayout(self.h_layout_2)
        self.v_layout.addWidget(self.output)

        self.setLayout(self.v_layout)
