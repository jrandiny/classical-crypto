from PyQt5.QtWidgets import QGroupBox, QWidget, QVBoxLayout, QButtonGroup, QRadioButton, QSizePolicy
from PyQt5.QtCore import QSize

from crypto.gui.components.configuration.encryption_key import EncryptionKey
from crypto.gui.components.configuration.post_processing import PostProcessing


class Configuration(QGroupBox):
    def __init__(self, title: str, size: QSize, parent: QWidget = None):
        super(Configuration, self).__init__(parent=parent)

        self.size = size
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
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.setBaseSize(self.size.width(), self.size.height())
        print(self.size.width(), self.size.height())
        print(self.width(), self.height())