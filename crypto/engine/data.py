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

    @property
    def text(self) -> str:
        assert self.data_type == DataType.TEXT
        return self._data

    @property
    def file_handle(self) -> TextIO:
        assert self.data_type == DataType.FILE
        return open('asd', 'r')

    @property
    def path(self) -> str:
        assert self.data_type == DataType.FILE
        return self._data
