from crypto.engine.base_engine import BaseEngine, EngineCapabilities
from crypto.engine.data import *
from crypto.engine.key import *
from crypto.util.string_util import StringUtil
from crypto.util.matrix_util import MatrixUtil

import numpy as np
import random
import math
import sympy
from typing import List


class HillEngine(BaseEngine):
    def __init__(self):
        super().__init__(
            EngineCapabilities(
                support_file=False, support_text=True, key_type=KeyType.NUMBER, key_length=-1
            )
        )

    def generate_random_key(self) -> Key:
        # Key consists of consecutively n and one matrix object of n x n
        key_param = [3]
        for _ in range(9):
            key_param.append(random.randint(0, 25))
        return Key(KeyType.NUMBER, key_param)

    def _do_encrypt(self, data: Data, key: Key) -> Data:
        """Encrypt data"""
        self._check_key_valid(key)

        string_array = self._transform_text(data, key)
        key_matrix = self._transform_key(key)
        encrypted_array = np.array([], dtype=int)

        for plain in string_array:
            cipher = np.matmul(key_matrix, plain) % 26
            encrypted_array = np.concatenate((encrypted_array, cipher))

        encrypted_array += ord('a')

        return Data(data_type=DataType.TEXT, data=''.join(map(chr, encrypted_array)))

    def _do_decrypt(self, data: Data, key: Key) -> Data:
        """Decrypt data"""
        self._check_key_valid(key)

        string_array = self._transform_text(data, key)
        key_matrix = MatrixUtil.inverse_mod_matrix(self._transform_key(key))
        decrypted_array = np.array([], dtype=int)

        for cipher in string_array:
            plain = np.matmul(key_matrix, cipher) % 26
            decrypted_array = np.concatenate((decrypted_array, plain))

        decrypted_array += ord('a')

        return Data(data_type=DataType.TEXT, data=''.join(map(chr, decrypted_array)))

    def _check_key_valid(self, key: Key):
        key_length = len(key.data[1:])

        if key.data[0] != key_length / key.data[0]:
            raise Exception('Matrix must be square')

    def _transform_text(self, data: Data, key: Key):
        raw_text = StringUtil.strip_non_alphabet(data.text).lower()
        no_space_text = StringUtil.remove_space(raw_text)
        dim = key.data[0]

        if len(no_space_text) % 3 != 0:
            no_space_text += 'x' * (dim - len(no_space_text) % dim)

        transformed = np.frombuffer(no_space_text.encode(), np.int8) - ord('a')
        transformed = transformed.astype(int)
        return np.reshape(transformed, (len(transformed) // dim, dim))

    def _transform_key(self, key: Key):
        dim = key.data[0]
        key_array = np.array(key.data[1:])
        return np.reshape(key_array, (dim, dim)).astype(int)
