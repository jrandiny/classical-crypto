from crypto.engine.base_engine import BaseEngine, EngineCapabilities
from crypto.engine.data import Data
from crypto.engine.key import *
from crypto.util.string_util import StringUtil

import numpy as np


class VigenereEngine(BaseEngine):
    def __init__(self):
        super().__init__(
            EngineCapabilities(
                support_file=False, support_text=True, key_type=KeyType.STRING, key_length=1
            )
        )

    def _do_encrypt(self, data: Data, key: Key) -> Data:
        """Encrypt data"""
        string_array = self._transform_text(data)

        full_key_array = self._transform_key(key, string_array)

        encrypted_array = string_array + full_key_array

        encrypted_array = np.mod(encrypted_array, 26)

        encrypted_array += ord('a')

        return ''.join(map(chr, encrypted_array))

    def _do_decrypt(self, data: Data, key: Key) -> Data:
        """Decrypt data"""
        string_array = self._transform_text(data)

        full_key_array = self._transform_key(key, string_array)

        encrypted_array = string_array - full_key_array

        encrypted_array = np.mod(encrypted_array, 26)

        encrypted_array += ord('a')

        return ''.join(map(chr, encrypted_array))

    def _transform_key(self, key: Key, string_array):
        key_array = np.frombuffer(key.data[0].lower().encode(), np.int8) - ord('a')
        return np.resize(key_array, len(string_array))

    def _transform_text(self, data: Data):
        raw_text = StringUtil.strip_non_alphabet(data.get_text()).lower()
        return np.frombuffer(raw_text.encode(), np.int8) - ord('a')