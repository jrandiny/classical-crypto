from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy, QSpinBox, QComboBox

from crypto.gui.components.configuration_box.base_key import BaseKey
from crypto.engine.key import Key, KeyType

allowed_values = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]


class AffineKey(BaseKey):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setup_ui()
        self.m_shift = 1

    def setup_ui(self):
        self.lbl_mul = QLabel('Multiplicative Shift:')
        self.lbl_add = QLabel('Additive Shift:')

        self.spin_box = QSpinBox()
        self.spin_box.setValue(0)

        self.combo_box = QComboBox()
        self.combo_box.addItems(map(str, allowed_values))

        self.h_layout_1 = QHBoxLayout()
        self.h_layout_1.addWidget(self.lbl_mul)
        self.h_layout_1.addWidget(self.combo_box)

        self.h_layout_2 = QHBoxLayout()
        self.h_layout_2.addWidget(self.lbl_add)
        self.h_layout_2.addWidget(self.spin_box)

        self.v_layout = QVBoxLayout()
        self.v_layout.addLayout(self.h_layout_1)
        self.v_layout.addLayout(self.h_layout_2)
        self.setLayout(self.v_layout)

        self.combo_box.currentTextChanged.connect(self.update_m_shift)

    def update_m_shift(self, value: str):
        self.m_shift = int(value)

    def build_key(self):
        b = self.spin_box.value()
        m = self.m_shift
        return Key(KeyType.NUMBER, [26, m, b])
