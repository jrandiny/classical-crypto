from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout

from crypto.gui.components.main_input.input_file import InputFile
from crypto.gui.components.main_input.toggle_button import ToggleButton


class TabFile(QWidget):
    def __init__(self, parent: QWidget = None):
        super(TabFile, self).__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.input = InputFile('Import')
        self.output = InputFile('Browse')

        self.mode_toggle = ToggleButton(['Encrypt', 'Decrypt'])
        self.btn_execute = QPushButton('Execute')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.output)
        self.layout.addWidget(self.mode_toggle)
        self.layout.addWidget(self.btn_execute)

        self.setLayout(self.layout)
