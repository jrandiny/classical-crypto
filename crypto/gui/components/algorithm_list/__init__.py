from PyQt5.QtWidgets import QGroupBox, QWidget, QVBoxLayout, QButtonGroup, QRadioButton, QSizePolicy
from PyQt5.QtCore import QSize

from crypto.engine.engine_factory import EngineType
from crypto.gui.encryption_parms import EncryptionParms
from crypto.engine.engine_factory import EngineType


class AlgorithmList(QGroupBox):
    def __init__(self, parent: QWidget = None):
        super(AlgorithmList, self).__init__(parent=parent)

        self.list_of_algorithm = EngineType.list()
        self.setup_ui()

    def setup_ui(self):
        self.setTitle('Algorithms')
        self.layout = QVBoxLayout()

        self.btn_group = QButtonGroup()
        for i in range(len(self.list_of_algorithm)):
            radio_button = QRadioButton(self.list_of_algorithm[i].value)
            self.btn_group.addButton(radio_button, i)
            self.layout.addWidget(radio_button)

            if i == 0:
                radio_button.animateClick()

        self.setLayout(self.layout)
        self.layout.setSpacing(20)

        self.btn_group.idClicked.connect(self.set_engine_type)

    def set_engine_type(self, id):
        EncryptionParms.get_instance().update_engine_type(self.list_of_algorithm[id])
