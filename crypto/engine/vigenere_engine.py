from crypto.engine.base_engine import BaseEngine, EngineCapabilities
from crypto.engine.data import Data
from crypto.engine.key import *


class VigenereEngine(BaseEngine):
    def __init__(self):
        pass

    def get_capabilities(self) -> EngineCapabilities:
        """Get engine capabilities"""
        return EngineCapabilities(
            support_file=False, support_text=False, key_type=KeyType.STRING, key_length=1
        )

    def encrypt(self, data: Data, key: Key) -> Data:
        """Encrypt data"""
        pass

    def decrypt(self, data: Data, key: Key) -> Data:
        """Decrypt data"""
        pass
