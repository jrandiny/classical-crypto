from abc import ABC, abstractmethod
from dataclasses import dataclass
from engine.data import Data


@dataclass
class EngineCapabilities:
    support_file: bool
    support_text: bool


class BaseEngine(ABC):
    @abstractmethod
    def encrypt(self, data: Data): Data:
        """Encrypt data"""
        pass

    @abstractmethod
    def decrypt(self, data: Data, key): Data:
        """Decrypt data"""
        pass

    @abstractmethod
    def get_capabilities(self) -> EngineCapabilities:
        """Get engine capabilities"""
        pass
