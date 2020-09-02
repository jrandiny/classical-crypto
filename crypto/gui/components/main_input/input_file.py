from PyQt5.QtWidgets import QWidget, QPushButton, QTextEdit, QHBoxLayout
from PyQt5.QtCore import QSize


class InputFile(QWidget):
    def __init__(self, btn_text: str, parent: QWidget = None):
        super(InputFile, self).__init__(parent=parent)
        self.btn_text = btn_text
        self.setupUi()

    def setupUi(self):
        self.text_edit = QTextEdit()
        self.copy_button = QPushButton(self.btn_text)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.text_edit)
        self.layout.addWidget(self.copy_button)

        self.setLayout(self.layout)
