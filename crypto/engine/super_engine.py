from crypto.engine.base_engine import BaseEngine, EngineCapabilities
from crypto.engine.data import *
from crypto.engine.key import *

from crypto.util.string_util import StringUtil

from nptyping import NDArray

import numpy as np


class SuperEngine(BaseEngine):
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__(
                EngineCapabilities(
                    support_file=False, support_text=True, key_type=KeyType.STRING, key_length=1
                )
            )
        else:
            super().__init__(args[0])

    def generate_random_key(self) -> Key:
        return Key(KeyType.STRING, [StringUtil.generate_random_string(8)])

    def _do_encrypt(self, data: Data, key: Key) -> Data:
        """Encrypt data"""
        string_array = self._transform_text(data)

        full_key_array = self._transform_key(key, string_array)

        encrypted_array = string_array + full_key_array

        encrypted_array = np.mod(encrypted_array, 26)

        encrypted_array += ord('a')

        transpose_key = len(key.data[0])

        output_str = ''

        for i in range(0, len(encrypted_array), transpose_key):
            end_index = i + transpose_key
            if end_index > len(encrypted_array):
                end_index = len(encrypted_array)

            flipped_array = np.flip(encrypted_array[i:end_index])
            output_str += ''.join(map(chr, flipped_array))

        return Data(data_type=DataType.TEXT, data=output_str)

    def _do_decrypt(self, data: Data, key: Key) -> Data:
        """Decrypt data"""

        string_array = self._transform_text(data)
        full_key_array = self._transform_key(key, string_array)

        transpose_key = len(key.data[0])

        transposed_array = []

        for i in range(0, len(string_array), transpose_key):
            end_index = i + transpose_key
            if end_index > len(string_array):
                end_index = len(string_array)

            flipped_array = np.flip(string_array[i:end_index])
            transposed_array.append(flipped_array)

        string_array = np.concatenate(transposed_array)

        decrypted_array = string_array - full_key_array

        decrypted_array = np.mod(decrypted_array, 26)

        decrypted_array += ord('a')

        return Data(data_type=DataType.TEXT, data=''.join(map(chr, decrypted_array)))

    def _transform_key(self, key: Key, string_array) -> NDArray[np.int32]:
        key_array = np.frombuffer(key.data[0].encode(), np.int8) - ord('a')
        return np.resize(key_array, len(string_array)).astype(np.int32)

    def _transform_text(self, data: Data) -> NDArray[np.int32]:
        raw_text = StringUtil.strip_non_alphabet(data.text).lower()
        return (np.frombuffer(raw_text.encode(), np.int8) - ord('a')).astype(np.int32)