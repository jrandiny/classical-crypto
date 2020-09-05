from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy, QTableWidget, QSpinBox, QHeaderView, QLineEdit, QSpacerItem
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

from crypto.gui.components.configuration_box.base_key import BaseKey
from crypto.engine.key import Key, KeyType

from typing import List
import string


class RotorSpinner(QSpinBox):
    def __init__(self, value_list: List[str]):
        self.value_list = value_list
        super().__init__()

    def valueFromText(self, text: str) -> int:
        if text.isdigit():
            return int(text)
        else:
            return 0

    def textFromValue(self, value: int) -> str:
        return self.value_list[value - 1]


class EnigmaKey(BaseKey):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        alphabet_validator = QRegExp('[a-z]')

        self.rotor_1_lbl = QLabel('Rotor 1:')
        self.rotor_1_spinner = RotorSpinner(
            ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII'])
        self.rotor_1_spinner.setMinimum(1)
        self.rotor_1_spinner.setMaximum(8)
        self.rotor_1_spinner.setValue(1)
        self.rotor_1_offset = QLineEdit()
        self.rotor_1_offset.setText('a')
        self.rotor_1_offset.setValidator(QRegExpValidator(alphabet_validator))
        self.rotor_1_offset.setMaxLength(1)

        self.rotor_1_group = QVBoxLayout()
        self.rotor_1_group.addWidget(self.rotor_1_lbl)
        self.rotor_1_group.addWidget(self.rotor_1_spinner)
        self.rotor_1_group.addWidget(self.rotor_1_offset)

        self.rotor_2_lbl = QLabel('Rotor 2:')
        self.rotor_2_spinner = RotorSpinner(
            ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII'])
        self.rotor_2_spinner.setMinimum(1)
        self.rotor_2_spinner.setMaximum(8)
        self.rotor_2_spinner.setValue(1)
        self.rotor_2_offset = QLineEdit()
        self.rotor_2_offset.setText('a')
        self.rotor_2_offset.setValidator(QRegExpValidator(alphabet_validator))
        self.rotor_2_offset.setMaxLength(1)

        self.rotor_2_group = QVBoxLayout()
        self.rotor_2_group.addWidget(self.rotor_2_lbl)
        self.rotor_2_group.addWidget(self.rotor_2_spinner)
        self.rotor_2_group.addWidget(self.rotor_2_offset)

        self.rotor_3_lbl = QLabel('Rotor 3:')
        self.rotor_3_spinner = RotorSpinner(
            ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII'])
        self.rotor_3_spinner.setMinimum(1)
        self.rotor_3_spinner.setMaximum(8)
        self.rotor_3_spinner.setValue(1)
        self.rotor_3_offset = QLineEdit()
        self.rotor_3_offset.setText('a')
        self.rotor_3_offset.setValidator(QRegExpValidator(alphabet_validator))
        self.rotor_3_offset.setMaxLength(1)

        self.rotor_3_group = QVBoxLayout()
        self.rotor_3_group.addWidget(self.rotor_3_lbl)
        self.rotor_3_group.addWidget(self.rotor_3_spinner)
        self.rotor_3_group.addWidget(self.rotor_3_offset)

        self.rotor_group = QHBoxLayout()
        self.rotor_group.addLayout(self.rotor_1_group)
        self.rotor_group.addLayout(self.rotor_2_group)
        self.rotor_group.addLayout(self.rotor_3_group)

        self.reflector_lbl = QLabel('Reflector:')
        self.reflector_spinner = RotorSpinner(['UKW-B', 'UKW-C'])
        self.reflector_spinner.setMinimum(1)
        self.reflector_spinner.setMaximum(2)
        self.reflector_spinner.setValue(1)
        self.reflector_group = QHBoxLayout()
        self.reflector_group.addWidget(self.reflector_lbl)
        self.reflector_group.addWidget(self.reflector_spinner)

        self.spacer = QSpacerItem(10, 10, QSizePolicy.Expanding,
                                  QSizePolicy.Expanding)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(QLabel('Based on Enigma Machine M3'))
        self.v_layout.addLayout(self.rotor_group)
        self.v_layout.addLayout(self.reflector_group)
        self.v_layout.addSpacerItem(self.spacer)
        self.setLayout(self.v_layout)

    def build_key(self):

        return Key(KeyType.NUMBER, [
            self.rotor_1_spinner.value() - 1,
            ord(self.rotor_1_offset.text()) - ord('a'),
            self.rotor_2_spinner.value() - 1,
            ord(self.rotor_2_offset.text()) - ord('a'),
            self.rotor_3_spinner.value() - 1,
            ord(self.rotor_3_offset.text()) - ord('a'),
            self.reflector_spinner.value() - 1
        ])
