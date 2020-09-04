from PyQt5.QtWidgets import QGroupBox, QWidget, QVBoxLayout, QButtonGroup, QRadioButton, QSizePolicy
from PyQt5.QtCore import QSize

from crypto.gui.components.configuration_box.encryption_key import EncryptionKey
from crypto.gui.components.configuration_box.post_processing import PostProcessing


class ConfigurationBox(QGroupBox):
    def __init__(self, title: str, parent: QWidget = None):
        super(ConfigurationBox, self).__init__(parent=parent)

        self.title = title
        self.setupUi()

    def setupUi(self):
        self.setTitle(self.title)
        self.layout = QVBoxLayout()

        self.encryption_key = EncryptionKey()
        self.post_processing = PostProcessing()

        self.layout.addWidget(self.encryption_key)
        self.layout.addWidget(self.post_processing)

        self.setLayout(self.layout)
        self.layout.setSpacing(20)
        # self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)