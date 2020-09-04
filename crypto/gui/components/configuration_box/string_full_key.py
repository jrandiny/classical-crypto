from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QSizePolicy, QTableWidget

from crypto.gui.components.configuration_box.base_key import BaseKey
from crypto.engine.key import Key, KeyType


class StringFullKey(BaseKey):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText('Input your encryption key')
        self.line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.matrix = QTableWidget()
        self.matrix.setRowCount(26)
        self.matrix.setColumnCount(26)
        self.matrix.resizeColumnsToContents()
        self.matrix.resizeRowsToContents()
        self.matrix.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.matrix)
        self.setLayout(self.layout)

    def build_key(self):
        text = self.line_edit.text()
        return Key(KeyType.STRING, [text])
