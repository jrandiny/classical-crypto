from enum import Enum
from typing import Union, TextIO


class DataType(Enum):
    FILE = 'file'
    TEXT = 'text'


class Data:
    def __init__(self, data_type: DataType, data: str, extended: bool = False):
        self.data_type = data_type
        if self.data_type == DataType.TEXT and not extended:
            self._data = data.lower()
        else:
            self._data = data

    def get_text(self) -> str:
        assert self.data_type == DataType.TEXT
        return self._data

    def get_file(self) -> TextIO:
        assert self.data_type == DataType.FILE
        abc = open('asdas', 'r')
        return self._data
