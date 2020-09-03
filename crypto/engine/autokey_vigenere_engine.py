from crypto.engine.data import *
from crypto.engine.key import *
from crypto.engine.vigenere_engine import VigenereEngine
from crypto.util.string_util import StringUtil

import numpy as np


class AutokeyVigenereEngine(VigenereEngine):
    def _do_encrypt(self, data: Data, key: Key) -> Data:
        data_string = StringUtil.strip_non_alphabet(data.get_text())
        key_string = key.data[0]

        if len(data_string) != len(key_string):
            raise Exception('Invalid key length')

        return super()._do_encrypt(data, key)

    def complete_key(self, data: Data, key: Key):
        data_string = StringUtil.strip_non_alphabet(data.get_text())
        key_string = key.data[0]

        delta_length = len(data_string) - len(key_string)

        if delta_length > 0:
            new_key_string = key_string + data_string[:delta_length]
            return Key(KeyType.STRING, [new_key_string])
        else:
            return key