from PyQt5.QtWidgets import QLineEdit, QLabel, QWidget, QVBoxLayout, QRadioButton, QButtonGroup


class PostProcessing(QWidget):
    def __init__(self, parent: QWidget = None):
        super(PostProcessing, self).__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.lbl_title = QLabel()
        self.lbl_title.setText('Output')

        self.btn_group = QButtonGroup()
        self.btn_remove_whitespace = QRadioButton('Remove whitespace')
        self.btn_split = QRadioButton('Group in 5')
        self.btn_group.addButton(self.btn_remove_whitespace)
        self.btn_group.addButton(self.btn_split)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.lbl_title)
        self.layout.addWidget(self.btn_remove_whitespace)
        self.layout.addWidget(self.btn_split)
        self.setLayout(self.layout)