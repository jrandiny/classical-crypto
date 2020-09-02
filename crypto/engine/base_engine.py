from abc import ABC, abstractmethod
from dataclasses import dataclass
from crypto.engine.data import Data
from crypto.engine.key import KeyType, Key


@dataclass
class EngineCapabilities:
    support_file: bool
    support_text: bool
    key_type: KeyType
    key_length: int


class BaseEngine(ABC):
    def __init__(self, engine_capabilities: EngineCapabilities):
        self.capabilities = engine_capabilities

    @abstractmethod
    def encrypt(self, data: Data, key: Key) -> Data:
        """Encrypt data"""
        pass

    @abstractmethod
    def decrypt(self, data: Data, key: Key) -> Data:
        """Decrypt data"""
        pass
