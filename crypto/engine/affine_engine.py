from crypto.engine.base_engine import BaseEngine, EngineCapabilities
from crypto.engine.data import *
from crypto.engine.key import *
from crypto.util.string_util import StringUtil

import numpy as np
import random
import math
import sympy
from typing import List


class AffineEngine(BaseEngine):
    def __init__(self):
        super().__init__(
            EngineCapabilities(support_file=False,
                               support_text=True,
                               key_type=KeyType.NUMBER,
                               key_length=3))

    def generate_random_key(self) -> Key:
        # Key consists of consecutively n, m, b, hence length=3
        return Key(KeyType.NUMBER, [
            26,
            random.choice([1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23]),
            random.randint(1, 25)
        ])

    def _do_encrypt(self, data: Data, key: Key) -> Data:
        """Encrypt data"""
        self._check_key_valid(key)

        string_array = self._transform_text(data)
        n = key.data[0]
        m = key.data[1]
        b = key.data[2]

        encrypted_array = (string_array * m + b) % n
        encrypted_array += ord('a')

        return Data(data_type=DataType.TEXT,
                    data=''.join(map(chr, encrypted_array)))

    def _do_decrypt(self, data: Data, key: Key) -> Data:
        """Decrypt data"""
        self._check_key_valid(key)

        string_array = self._transform_text(data)
        n = key.data[0]
        m_inverse = sympy.mod_inverse(key.data[1], n)
        b = key.data[2]

        decrypted_array = (string_array - b) * m_inverse % n
        decrypted_array += ord('a')

        return Data(data_type=DataType.TEXT,
                    data=''.join(map(chr, decrypted_array)))

    def _check_key_valid(self, key: Key):
        n = key.data[0]
        m = key.data[1]
        b = key.data[2]

        if not n > m:
            raise Exception('n must be bigger than m')
        elif math.gcd(m, n) != 1:
            raise Exception('n and m must be relative prime')

    def _transform_text(self, data: Data):
        raw_text = StringUtil.strip_non_alphabet(data.get_text()).lower()
        no_space_text = StringUtil.remove_space(raw_text)

        transformed = np.frombuffer(raw_text.encode(), np.int8) - ord('a')
        return transformed.astype(int)