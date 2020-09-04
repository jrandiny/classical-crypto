from enum import Enum


class ModeType(Enum):
    ENCRYPT = 'Encrypt'
    DECRYPT = 'Decrypt'


class EncryptionParameter:
    __instance = None

    def __init__(self):
        if EncryptionParameter.__instance is not None:
            raise Exception('Only allowed 1 instance')
        else:
            EncryptionParameter.__instance = self
            self.method = ModeType.ENCRYPT

    def is_parameter_valid(self):
        return True

    @staticmethod
    def get_instance():
        if EncryptionParameter.__instance is None:
            EncryptionParameter()
        return EncryptionParameter.__instance
