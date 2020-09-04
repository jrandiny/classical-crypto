from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import QSize


class InputFile(QWidget):
    def __init__(self, btn_text: str, parent: QWidget = None):
        super(InputFile, self).__init__(parent=parent)
        self.btn_text = btn_text
        self.setupUi()

    def setupUi(self):
        self.line_edit = QLineEdit()
        self.line_edit.setEnabled(False)
        self.line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.copy_button = QPushButton(self.btn_text)
        self.copy_button.setSizePolicy(QSizePolicy.Minimum,
                                       QSizePolicy.Minimum)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.copy_button)

        self.setLayout(self.layout)
