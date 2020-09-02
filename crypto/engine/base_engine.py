from abc import ABC, abstractmethod
from dataclasses import dataclass
from crypto.engine.data import *
from crypto.engine.key import *


@dataclass
class EngineCapabilities:
    support_file: bool
    support_text: bool
    key_type: KeyType
    key_length: int


class BaseEngine(ABC):
    def __init__(self, engine_capabilities: EngineCapabilities):
        self.capabilities = engine_capabilities

    def _check_data_supported(self, data: Data):
        if data.data_type == DataType.FILE and not self.capabilities.support_file:
            raise Exception('Engine doesn\'t support file input')
        if data.data_type == DataType.TEXT and not self.capabilities.support_text:
            raise Exception('Engine doesn\'t support text input')

    def _check_key_format(self, key: Key):
        if key.key_type != self.capabilities.key_type:
            raise Exception('Invalid key type')
        if len(key.data) != self.capabilities.key_length:
            raise Exception('Invalid key length')

    @abstractmethod
    def encrypt(self, data: Data, key: Key) -> Data:
        """Encrypt data"""
        pass

    @abstractmethod
    def decrypt(self, data: Data, key: Key) -> Data:
        """Decrypt data"""
        pass
