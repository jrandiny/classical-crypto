from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy, QTableWidget, QSpinBox, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import Qt

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
        self.spin_box.setMinimum(1)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.lbl_dim)
        self.h_layout.addWidget(self.spin_box)

        self.matrix = QTableWidget()
        self.matrix.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.matrix.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.matrix.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

        self.v_layout = QVBoxLayout()
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.matrix)
        self.setLayout(self.v_layout)

        self.spin_box.valueChanged.connect(self.update_matrix)
        self.matrix.itemChanged.connect(self.update_alignment)
        self.update_matrix(2)

    def apply_key(self, key):
        dim = key.data[0]
        self.spin_box.setValue(key.data[0])
        for i in range(dim):
            for j in range(dim):
                el = QTableWidgetItem(str(key.data[i * dim + j + 1]))
                self.matrix.setItem(i, j, el)

    def build_key(self):
        dim = self.spin_box.value()
        key = [dim]

        for i in range(dim):
            for j in range(dim):
                el = self.matrix.item(i, j)
                key.append(int(el.text()))

        return Key(KeyType.NUMBER, key)

    def update_matrix(self, dim: int):
        self.matrix.setRowCount(dim)
        self.matrix.setColumnCount(dim)
        self.matrix.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.matrix.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def update_alignment(self, item: QTableWidgetItem):
        item.setTextAlignment(Qt.AlignCenter)
