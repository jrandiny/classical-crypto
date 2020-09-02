from PyQt5.QtWidgets import QLineEdit, QLabel, QWidget, QVBoxLayout


class EncryptionKey(QWidget):
    def __init__(self, parent: QWidget = None):
        super(EncryptionKey, self).__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.key_lbl = QLabel()
        self.key_lbl.setText('Encryption Key')

        self.edit_text = QLineEdit()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.key_lbl)
        self.layout.addWidget(self.edit_text)
        self.setLayout(self.layout)