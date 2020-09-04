from PyQt5.QtWidgets import QLineEdit, QLabel, QWidget, QVBoxLayout, QRadioButton, QButtonGroup, QSizePolicy, QSpacerItem


class PostProcessing(QWidget):
    def __init__(self, parent: QWidget = None):
        super(PostProcessing, self).__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.lbl_title = QLabel()
        self.lbl_title.setText('Output')
        self.lbl_title.setSizePolicy(QSizePolicy.Expanding,
                                     QSizePolicy.Minimum)

        self.btn_remove_whitespace = QRadioButton('Remove whitespace')
        self.btn_split = QRadioButton('Group in 5')

        self.btn_group = QButtonGroup()
        self.btn_group.addButton(self.btn_remove_whitespace)
        self.btn_group.addButton(self.btn_split)

        self.spacer = QSpacerItem(10, 10, QSizePolicy.Expanding,
                                  QSizePolicy.MinimumExpanding)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.lbl_title)
        self.layout.addWidget(self.btn_remove_whitespace)
        self.layout.addWidget(self.btn_split)
        self.layout.addSpacerItem(self.spacer)

        self.layout.setSpacing(20)
        self.setLayout(self.layout)