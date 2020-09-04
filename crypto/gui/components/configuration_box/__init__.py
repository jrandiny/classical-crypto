from PyQt5.QtWidgets import QWidget, QVBoxLayout, QButtonGroup, QRadioButton, QSizePolicy
from PyQt5.QtCore import QSize

from crypto.gui.components.configuration_box.encryption_key import EncryptionKey
from crypto.gui.components.configuration_box.post_processing import PostProcessing


class ConfigurationBox(QWidget):
    def __init__(self, parent: QWidget = None):
        super(ConfigurationBox, self).__init__(parent=parent)
        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout()

        self.encryption_key = EncryptionKey()
        self.encryption_key.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.post_processing = PostProcessing()
        self.post_processing.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.layout.addWidget(self.encryption_key)
        self.layout.addWidget(self.post_processing)

        self.setLayout(self.layout)
        self.layout.setSpacing(20)
        # self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)