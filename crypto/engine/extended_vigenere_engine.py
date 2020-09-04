from crypto.engine.base_engine import BaseEngine, EngineCapabilities
from crypto.engine.data import *
from crypto.engine.key import *
from crypto.engine.vigenere_engine import VigenereEngine
from crypto.util.string_util import StringUtil
from nptyping import NDArray

import numpy as np
import random
import string


class ExtendedVigenereEngine(VigenereEngine):
    def __init__(self):
        super().__init__(
            EngineCapabilities(
                support_file=True, support_text=True, key_type=KeyType.STRING, key_length=1
            )
        )

    def _do_encrypt(self, data: Data, key: Key) -> Data:
        if data.data_type == DataType.TEXT:
            string_array = self._transform_text(data)
            full_key_array = self._transform_key(key, string_array)

            encrypted_array = string_array + full_key_array
            encrypted_array = np.mod(encrypted_array, 256)

            return Data(
                data_type=DataType.TEXT, data=''.join(map(chr, encrypted_array)), extended=True
            )
        elif data.data_type == DataType.FILE:
            pass

    def _do_decrypt(self, data: Data, key: Key) -> Data:
        if data.data_type == DataType.TEXT:
            string_array = self._transform_text(data)
            full_key_array = self._transform_key(key, string_array)

            decrypted_array = string_array - full_key_array
            decrypted_array = np.mod(decrypted_array, 256)

            return Data(data_type=DataType.TEXT, data=''.join(map(chr, decrypted_array)))
        elif data.data_type == DataType.FILE:
            pass

    def _transform_key(self, key: Key, string_array) -> NDArray[np.int32]:
        key_array = np.frombuffer(key.data[0].encode(), np.int8)
        return np.resize(key_array, len(string_array)).astype(np.int32)

    def _transform_text(self, data: Data) -> NDArray[np.int32]:
        raw_text = StringUtil.strip_non_ascii(data.get_text())
        return np.array([ord(ch) for ch in raw_text], dtype=np.int32)