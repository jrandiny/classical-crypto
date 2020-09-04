from crypto.engine.engine_factory import *
from crypto.engine.data import *
from crypto.engine.key import *
from enum import Enum


class ModeType(Enum):
    ENCRYPT = 'Encrypt'
    DECRYPT = 'Decrypt'


class OutputType(Enum):
    NO_SPACE = 'Remove whitespace'
    GROUP = 'Group in 5'

    @staticmethod
    def list():
        return list(map(lambda out_type: out_type, OutputType))


class EncryptionParameter:
    __instance = None

    def __init__(self):
        if EncryptionParameter.__instance is not None:
            raise Exception('Only allowed 1 instance')
        else:
            EncryptionParameter.__instance = self
            self.method = ModeType.ENCRYPT
            self.engine_type = None
            self.key = None
            self.data = None
            self.output_configuration = OutputType.NO_SPACE

    def is_parameter_valid(self):
        return True

    @staticmethod
    def get_instance():
        if EncryptionParameter.__instance is None:
            EncryptionParameter()
        return EncryptionParameter.__instance
