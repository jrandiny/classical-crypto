from PyQt5.QtWidgets import QLineEdit, QLabel, QWidget, QVBoxLayout, QSizePolicy, QGroupBox

from crypto.gui.encryption_parms import EncryptionParms
from crypto.gui.components.configuration_box.key_widget_factory import *
from crypto.engine.engine_factory import EngineType
from crypto.engine.key import Key


class EncryptionBox(QGroupBox):
    def __init__(self, parent: QWidget = None):
        super(EncryptionBox, self).__init__(parent=parent)
        self.engine_type_list = EngineType.list()
        self.setup_ui()

    def setup_ui(self):
        self.setTitle('Encryption Key')

        self.key_input = KeyWidgetFactory.create_widget(EngineType.VIGENERE)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.key_input)
        self.layout.setSpacing(20)

        self.setLayout(self.layout)

    def get_key(self) -> Key:
        return self.key_input.build_key()

    def on_update_key_widget(self, id: int):
        self.layout.removeWidget(self.key_input)
        self.key_input.deleteLater()
        engine_type = self.engine_type_list[id]
        self.key_input = KeyWidgetFactory.create_widget(engine_type)
        self.layout.addWidget(self.key_input)
