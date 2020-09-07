from crypto.engine.data import *
from crypto.engine.key import *
from crypto.engine.vigenere_engine import VigenereEngine
from crypto.util.string_util import StringUtil

import numpy as np


class AutokeyVigenereEngine(VigenereEngine):
    def _do_encrypt(self, data: Data, key: Key) -> Data:
        data_string = StringUtil.strip_non_alphabet(data.text)
        key_string = key.data[0]

        delta = max(len(data_string) - len(key_string), 0)

        return super()._do_encrypt(
            data, Key(key_type=KeyType.STRING, data=[key_string + data_string[0:delta]])
        )

    def _do_decrypt(self, data: Data, key: Key) -> Data:
        string_array = self._transform_text(data)

        key_length = len(key.data[0])

        key_array = self._transform_key(key, key.data[0])

        output_str = ''

        for i in range(0, len(string_array), key_length):
            end_index = min(len(string_array), i + key_length)

            string_part = string_array[i:end_index]

            temp_decrypted_array = string_part - key_array[0:len(string_part)]
            temp_decrypted_array = np.mod(temp_decrypted_array, 26)

            key_array = np.array(temp_decrypted_array, copy=True)

            temp_decrypted_array += ord('a')

            output_str += ''.join(map(chr, temp_decrypted_array))

        return Data(data_type=DataType.TEXT, data=output_str)