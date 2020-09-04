from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QWidget
from dataclasses import dataclass
from crypto.engine.key import *


class BaseKey(QWidget):
    def __init__(self, parent: QWidget = None):
        super(BaseKey, self).__init__(parent=parent)

    @abstractmethod
    def build_key(self) -> Key:
        pass
