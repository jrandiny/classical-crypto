from crypto.engine.vigenere_engine import VigenereEngine
from crypto.engine.key import *
import numpy as np


class AutokeyVigenereEngine(VigenereEngine):
    def _transform_key(self, key: Key, string_array):
        key_array = np.frombuffer(key.data[0].lower().encode(), np.int8) - ord('a')

        key_delta = len(string_array) - len(key_array)

        return np.concatenate([key_array, np.resize(string_array, key_delta)])
