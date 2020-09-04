from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel

from crypto.gui.components.main_input.input_file import InputFile
from crypto.gui.components.main_input.input_mode import InputMode


class TabFile(QWidget):
    def __init__(self, parent: QWidget = None):
        super(TabFile, self).__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.input_file = InputFile('Import')
        self.output_file = InputFile('Browse')
        self.input_mode = InputMode()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.input_file)
        self.layout.addWidget(self.output_file)
        self.layout.addWidget(self.input_mode)

        self.setLayout(self.layout)
