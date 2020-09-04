from PyQt5.QtWidgets import QWidget, QPushButton, QTextEdit, QVBoxLayout
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QClipboard, QGuiApplication


class InputString(QWidget):
    def __init__(self, enabled: bool = True, parent: QWidget = None):
        super(InputString, self).__init__(parent=parent)
        self.enabled = enabled
        self.setup_ui()

    def setup_ui(self):
        self.text_edit = QTextEdit()
        self.text_edit.setEnabled(self.enabled)
        self.copy_button = QPushButton('Copy to Clipboard')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text_edit)
        self.layout.addWidget(self.copy_button)
        self.setLayout(self.layout)

        self.copy_button.clicked.connect(self.copy_to_clipboard)

    def copy_to_clipboard(self):
        text = self.text_edit.toPlainText()
        clip_board = QGuiApplication.clipboard()
        clip_board.clear(mode=clip_board.Clipboard)
        clip_board.setText(text, mode=clip_board.Clipboard)
