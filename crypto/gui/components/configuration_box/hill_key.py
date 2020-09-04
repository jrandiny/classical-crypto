from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy, QTableWidget, QSpinBox, QHeaderView

from crypto.gui.components.configuration_box.base_key import BaseKey
from crypto.engine.key import Key, KeyType


class HillKey(BaseKey):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.lbl_dim = QLabel('Matrix Dimension:')
        self.spin_box = QSpinBox()
        self.spin_box.setValue(2)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.lbl_dim)
        self.h_layout.addWidget(self.spin_box)

        self.matrix = QTableWidget()
        self.matrix.setRowCount(2)
        self.matrix.setColumnCount(2)
        self.matrix.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.matrix.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.matrix.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

        self.v_layout = QVBoxLayout()
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.matrix)
        self.setLayout(self.v_layout)

        self.spin_box.valueChanged.connect(self.update_matrix)

    def build_key(self):
        text = self.line_edit.text()
        return Key(KeyType.STRING, [text])

    def update_matrix(self, dim: int):
        self.matrix.setRowCount(dim)
        self.matrix.setColumnCount(dim)
        self.matrix.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.matrix.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
