from enum import Enum
from typing import Union, TextIO


class DataType(Enum):
    FILE = 'file'
    TEXT = 'text'

class Data:
    def __init__(self, data_type: DataType, data: str):
        self._data_type = data_type
        self._data = data

    def get_text()->str:
        assert self._data_type == DataType.TEXT
        return self._data

    def get_file()->:
        assert self._data_type == DataType.FILE
        abc = open('asdas', 'r')
        return self._data

