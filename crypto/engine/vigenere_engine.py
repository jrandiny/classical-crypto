from crypto.engine.base_engine import BaseEngine, EngineCapabilities
from crypto.engine.data import Data
from crypto.engine.key import *


class VigenereEngine(BaseEngine):
    def __init__(self):
        super().__init__(
            EngineCapabilities(
                support_file=False, support_text=True, key_type=KeyType.STRING, key_length=1
            )
        )
        pass

    def encrypt(self, data: Data, key: Key) -> Data:
        """Encrypt data"""
        pass

    def decrypt(self, data: Data, key: Key) -> Data:
        """Decrypt data"""
        pass
