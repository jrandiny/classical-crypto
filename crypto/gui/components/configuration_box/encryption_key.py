from PyQt5.QtWidgets import QLineEdit, QLabel, QWidget, QVBoxLayout, QSizePolicy, QSpacerItem


class EncryptionKey(QWidget):
    def __init__(self, parent: QWidget = None):
        super(EncryptionKey, self).__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.lbl_key = QLabel()
        self.lbl_key.setText('Encryption Key')
        self.lbl_key.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.key_input = QLineEdit()
        self.key_input.setSizePolicy(QSizePolicy.Expanding,
                                     QSizePolicy.Minimum)

        self.spacer = QSpacerItem(10, 10, QSizePolicy.Expanding,
                                  QSizePolicy.MinimumExpanding)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.lbl_key)
        self.layout.addWidget(self.key_input)
        self.layout.addSpacerItem(self.spacer)
        self.setLayout(self.layout)