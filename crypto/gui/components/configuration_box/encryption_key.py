from PyQt5.QtWidgets import QLineEdit, QLabel, QWidget, QVBoxLayout, QSizePolicy, QSpacerItem, QGroupBox

from crypto.gui.encryption_parameter import EncryptionParms


class EncryptionKey(QGroupBox):
    def __init__(self, parent: QWidget = None):
        super(EncryptionKey, self).__init__(parent=parent)
        self.setup_ui()

    def setup_ui(self):
        self.setTitle('Encryption Key')

        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText('Input your encryption key')
        self.key_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.spacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.key_input)
        self.layout.addSpacerItem(self.spacer)
        self.layout.setSpacing(20)

        self.setLayout(self.layout)
        self.key_input.textEdited.connect(self.on_key_change)

    def on_key_change(self, text):
        EncryptionParms.get_instance().raw_key = text
