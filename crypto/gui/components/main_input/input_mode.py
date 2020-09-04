from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel


class InputMode(QWidget):
    def __init__(self, parent=None):
        super(InputMode, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.btn_switch = QPushButton('Switch Mode')
        self.btn_execute = QPushButton('Execute')
        self.lbl_mode_title = QLabel('Mode:')
        self.lbl_mode_value = QLabel('Encrypt')

        self.h_layout_1 = QHBoxLayout()
        self.h_layout_2 = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.h_layout_1.addWidget(self.lbl_mode_title)
        self.h_layout_1.addWidget(self.lbl_mode_value)
        self.h_layout_2.addWidget(self.btn_switch)
        self.h_layout_2.addWidget(self.btn_execute)

        self.v_layout.addLayout(self.h_layout_1)
        self.v_layout.addLayout(self.h_layout_2)

        self.setLayout(self.v_layout)