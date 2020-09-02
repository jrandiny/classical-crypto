from abc import ABC, abstractmethod
from dataclasses import dataclass
from engine.data import Data
from engine.key import KeyType, Key

@dataclass
class EngineCapabilities:
    support_file: bool
    support_text: bool
    key_type: KeyType
    key_length: int


class BaseEngine(ABC):
    @abstractmethod
    def encrypt(self, data: Data): Data:
        """Encrypt data"""
        pass

    @abstractmethod
    def decrypt(self, data: Data, key: Key): Data:
        """Decrypt data"""
        pass

    @abstractmethod
    def get_capabilities(self) -> EngineCapabilities:
        """Get engine capabilities"""
        pass
