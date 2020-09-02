from PyQt5.QtWidgets import QWidget, QPushButton, QTextEdit, QVBoxLayout
from PyQt5.QtCore import QSize


class InputString(QWidget):
    def __init__(self, parent: QWidget = None):
        super(InputString, self).__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.text_edit = QTextEdit()
        self.copy_button = QPushButton('Copy to Clipboard')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text_edit)
        self.layout.addWidget(self.copy_button)

        self.setLayout(self.layout)
