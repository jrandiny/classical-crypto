from PyQt5.QtWidgets import QLineEdit, QLabel, QWidget, QVBoxLayout, QCheckBox


class PostProcessing(QWidget):
    def __init__(self, parent: QWidget = None):
        super(PostProcessing, self).__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.lbl_title = QLabel()
        self.lbl_title.setText('Output')

        self.btn_remove_whitespace = QCheckBox()
        self.btn_remove_whitespace.setText('Remove whitespace')
        self.btn_group = QCheckBox()
        self.btn_group.setText('Group in 5 Characters')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.lbl_title)
        self.layout.addWidget(self.btn_remove_whitespace)
        self.layout.addWidget(self.btn_group)
        self.setLayout(self.layout)