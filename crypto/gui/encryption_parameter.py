from __future__ import annotations
from enum import Enum

from crypto.engine.engine_factory import *
from crypto.engine.base_engine import BaseEngine
from crypto.engine.data import *
from crypto.engine.key import *


class ModeType(Enum):
    ENCRYPT = 'Encrypt'
    DECRYPT = 'Decrypt'


class OutputType(Enum):
    NO_SPACE = 'Remove whitespace'
    GROUP = 'Group in 5'

    @staticmethod
    def list():
        return list(map(lambda out_type: out_type, OutputType))


class EncryptionParms:
    __instance = None

    def __init__(self):
        if EncryptionParms.__instance is not None:
            raise Exception('Only allowed 1 instance')
        else:
            EncryptionParms.__instance = self
            self.mode = None
            self.engine_type = None
            self.output_conf = None
            self.raw_input = None
            self.raw_key = None
            self.file_in_path = None
            self.file_out_path = None

    def print_info(self):
        print('***Encryption Parameters***')
        print('Mode:', self.mode)
        print('Engine Type:', self.engine_type)
        print('Raw Input:', self.raw_input)
        print('Raw Key:', self.raw_key)
        print('Input File Path:', self.file_in_path)
        print('Output File Path:', self.file_out_path)
        print('Output Configuration:', self.output_conf)
        print('***************************')

    def is_parameter_valid(self) -> bool:
        return True

    def get_engine(self) -> BaseEngine:
        return EngineFactory.create_engine(self.engine_type)

    @staticmethod
    def get_instance() -> EncryptionParms:
        if EncryptionParms.__instance is None:
            EncryptionParms()
        return EncryptionParms.__instance
