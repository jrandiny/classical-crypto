from PyQt5.QtWidgets import QGroupBox, QWidget, QVBoxLayout, QTabWidget, QSizePolicy
from PyQt5.QtCore import QSize

from crypto.gui.components.main_input.tab_file import TabFile
from crypto.gui.components.main_input.tab_string import TabString
from crypto.engine.data import Data


class MainInput(QTabWidget):
    def __init__(self, parent: QWidget = None):
        super(MainInput, self).__init__(parent=parent)
        self.setup_ui()

    def setup_ui(self):
        self.tab_string = TabString()
        self.tab_file = TabFile()
        self.addTab(self.tab_string, 'String Input')
        self.addTab(self.tab_file, 'File Input')
        self.setCurrentIndex(0)

    def get_data(self) -> Data:
        if self.currentWidget() == self.tab_string:
            return self.tab_string.build_data()
        else:
            return self.tab_file.build_data()

    def get_output_path(self) -> str:
        if self.currentWidget() == self.tab_file:
            return self.tab_file.output_file.line_edit.text()
        else:
            raise Exception('Can\'t get output of string input')
