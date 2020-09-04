from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

from crypto.gui.components.main_input.input_string import InputString
from crypto.gui.components.main_input.input_mode import InputMode
from crypto.gui.encryption_parms import EncryptionParms


class TabString(QWidget):
    def __init__(self, parent: QWidget = None):
        super(TabString, self).__init__(parent=parent)
        self.setup_ui()

    def setup_ui(self):
        self.input_string = InputString()
        self.input_string.text_edit.setPlaceholderText('Input your plain text (e.g. this is not tucil)')
        self.output_string = InputString(enabled=False)
        self.input_mode = InputMode()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.input_string)
        self.layout.addWidget(self.input_mode)
        self.layout.addWidget(self.output_string)

        self.setLayout(self.layout)
        self.input_string.text_edit.textChanged.connect(self.on_input_change)

    def on_input_change(self):
        text = self.input_string.text_edit.toPlainText()
        EncryptionParms.get_instance().raw_input = text
