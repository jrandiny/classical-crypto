from PyQt5.QtWidgets import QWidget, QPushButton, QTextEdit, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QClipboard, QGuiApplication

from crypto.engine.data import Data, DataType
from crypto.gui.encryption_parms import OutputType
from crypto.util.string_util import StringUtil


class InputString(QWidget):
    def __init__(self, enabled: bool = True, parent: QWidget = None):
        super(InputString, self).__init__(parent=parent)
        self.enabled = enabled
        self.setup_ui()

    def setup_ui(self):
        self.text_edit = QTextEdit()
        self.text_edit.setEnabled(self.enabled)
        self.text_edit.setAcceptRichText(False)
        self.text_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

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

    def get_data(self) -> Data:
        text = self.text_edit.toPlainText()
        return Data(DataType.TEXT, text)

    def on_result_update(self, result: Data):
        self.text_edit.setPlainText(result.text)

    def on_change_format(self, id: int):
        mode = OutputType.list()[id]
        text = self.text_edit.toPlainText()

        if mode == OutputType.NO_SPACE:
            updated_text = StringUtil.remove_space(text)
        else:
            updated_text = StringUtil.split_to_group(text, 5)

        self.text_edit.setPlainText(updated_text)