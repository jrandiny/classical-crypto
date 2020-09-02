from PyQt5.QtWidgets import QPushButton, QWidget


class ToggleButton(QPushButton):
    def __init__(self, state_name: list, parent: QWidget = None):
        super(ToggleButton, self).__init__(parent=parent)
        assert len(state_name) == 2
        self.current_state = False
        self.state_name = state_name
        self.setupUi()

    def setupUi(self):
        self.toogle()

    def toogle(self):
        self.current_state = not self.current_state
        if self.current_state:
            self.setText(self.state_name[0])
        else:
            self.setText(self.state_name[1])
