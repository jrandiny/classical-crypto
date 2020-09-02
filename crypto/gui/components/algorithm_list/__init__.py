from PyQt5.QtWidgets import QGroupBox, QWidget, QVBoxLayout, QButtonGroup, QRadioButton, QSizePolicy
from PyQt5.QtCore import QSize


class AlgorithmList(QGroupBox):
    def __init__(self,
                 title: str,
                 list_of_algorithm: list,
                 size: QSize,
                 parent: QWidget = None):
        super(AlgorithmList, self).__init__(parent=parent)

        self.list_of_algorithm = list_of_algorithm
        self.size = size
        self.title = title
        self.setupUi()

    def setupUi(self):
        self.setTitle(self.title)
        self.layout = QVBoxLayout()

        self.btn_group = QButtonGroup()
        for i in range(len(self.list_of_algorithm)):
            radio_button = QRadioButton(self.list_of_algorithm[i])
            self.btn_group.addButton(radio_button)
            self.layout.addWidget(radio_button)

        self.setLayout(self.layout)
        self.layout.setSpacing(20)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.setBaseSize(self.size.width(), self.size.height())
        print(self.size.width(), self.size.height())
        print(self.width(), self.height())