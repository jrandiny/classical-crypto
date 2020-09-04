from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QFileDialog

from crypto.gui.components.main_input.input_file import InputFile
from crypto.gui.components.main_input.input_mode import InputMode
from crypto.gui.encryption_parameter import EncryptionParms


class TabFile(QWidget):
    def __init__(self, parent: QWidget = None):
        super(TabFile, self).__init__(parent=parent)
        self.setup_ui()

    def setup_ui(self):
        self.input_file = InputFile('Import')
        self.output_file = InputFile('Browse')
        self.input_mode = InputMode()

        self.layout = QVBoxLayout()
        self.layout.addSpacerItem(QSpacerItem(30, 30, QSizePolicy.Expanding, QSizePolicy.MinimumExpanding))
        self.layout.addWidget(self.input_file)
        self.layout.addWidget(self.output_file)
        self.layout.addSpacerItem(QSpacerItem(30, 50, QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.layout.addWidget(self.input_mode)
        self.layout.addSpacerItem(QSpacerItem(30, 30, QSizePolicy.Expanding, QSizePolicy.MinimumExpanding))

        self.setLayout(self.layout)
        self.input_file.btn_browse.clicked.connect(lambda: self.get_directory(is_input=True))
        self.output_file.btn_browse.clicked.connect(lambda: self.get_directory(is_input=False))

    def get_directory(self, is_input: bool):
        if is_input:
            filepath, _ = QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.currentPath(), '*')
            if filepath:
                EncryptionParms.get_instance().file_in_path = filepath
                self.input_file.line_edit.setText(filepath)
        else:
            default_name = 'cipher_out'
            filepath, _ = QFileDialog.getSaveFileName(self, 'Save File', QtCore.QDir.currentPath() + '/' + default_name)
            if filepath:
                EncryptionParms.get_instance().file_out_path = filepath
                self.output_file.line_edit.setText(filepath)
