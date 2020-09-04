from PyQt5.QtWidgets import QLineEdit, QLabel, QWidget, QVBoxLayout, QRadioButton, QButtonGroup, QSizePolicy, QSpacerItem, QGroupBox

from crypto.gui.encryption_parms import OutputType, EncryptionParms


class PostProcessing(QGroupBox):
    def __init__(self, parent: QWidget = None):
        super(PostProcessing, self).__init__(parent=parent)
        self.output_type_list = OutputType.list()
        self.setup_ui()

    def setup_ui(self):
        self.setTitle('Output Configuration')
        self.layout = QVBoxLayout()

        self.btn_group = QButtonGroup()

        for i in range(len(self.output_type_list)):
            radio_button = QRadioButton(self.output_type_list[i].value)
            self.btn_group.addButton(radio_button, i)
            self.layout.addWidget(radio_button)

            if i == 0:
                radio_button.animateClick()

        self.spacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)

        self.layout.addSpacerItem(self.spacer)
        self.layout.setSpacing(20)
        self.setLayout(self.layout)

        self.btn_group.idClicked.connect(self.set_output_type)

    def set_output_type(self, id):
        EncryptionParms.get_instance().output_conf = self.output_type_list[id]