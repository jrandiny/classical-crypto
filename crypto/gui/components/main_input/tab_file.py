from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel

from crypto.gui.components.main_input.input_file import InputFile


class TabFile(QWidget):
    def __init__(self, parent: QWidget = None):
        super(TabFile, self).__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.input = InputFile('Import')
        self.output = InputFile('Browse')

        self.btn_switch = QPushButton('Switch Mode')
        self.btn_execute = QPushButton('Execute')
        self.lbl_mode_title = QLabel('Mode:')
        self.lbl_mode_value = QLabel('Encrypt')

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.lbl_mode_title)
        self.h_layout.addWidget(self.lbl_mode_value)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.input)
        self.v_layout.addWidget(self.output)
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.btn_switch)
        self.v_layout.addWidget(self.btn_execute)

        self.setLayout(self.v_layout)
