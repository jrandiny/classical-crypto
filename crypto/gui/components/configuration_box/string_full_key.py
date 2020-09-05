from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QSizePolicy, QTableWidget, QPushButton, QTableWidgetItem

from crypto.gui.components.configuration_box.base_key import BaseKey
from crypto.engine.key import Key, KeyType

import string
import random


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

        self.btn_generate = QPushButton('Generate Random Table')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.matrix)
        self.layout.addWidget(self.btn_generate)
        self.setLayout(self.layout)

        self.btn_generate.clicked.connect(self.generate_matrix)
        self.btn_generate.animateClick()

    def generate_matrix(self):
        alphabet = list(string.ascii_lowercase)
        for i in range(26):
            random.shuffle(alphabet)
            for j in range(26):
                item = QTableWidgetItem(alphabet[j])
                self.matrix.setItem(i, j, item)

    def build_key(self):
        key = [self.line_edit.text()]

        for i in range(26):
            for j in range(26):
                char = self.matrix.item(i, j).text()
                key.append(char)

        return Key(KeyType.STRING, key)
