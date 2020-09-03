from crypto.engine.base_engine import BaseEngine, EngineCapabilities
from crypto.engine.data import *
from crypto.engine.key import *
from crypto.util.string_util import StringUtil

import numpy as np


class PlayfairEngine(BaseEngine):
    def __init__(self):
        super().__init__(
            EngineCapabilities(support_file=False,
                               support_text=True,
                               key_type=KeyType.STRING,
                               key_length=1))

    def generate_random_key(self) -> Key:
        return Key(KeyType.STRING, [StringUtil.generate_random_string(8)])

    def _do_encrypt(self, data: Data, key: Key) -> Data:
        """Encrypt data"""
        string_array = self._transform_text(data)

        full_key_array = self._transform_key(key)

        encrypted_text = ''

        for bigram in string_array:
            cipher = ''
            first_pos = list(
                map(lambda x: x[0], np.where(full_key_array == bigram[0])))
            second_pos = list(
                map(lambda x: x[0], np.where(full_key_array == bigram[1])))

            if first_pos[0] == second_pos[0]:
                cipher = full_key_array[first_pos[0]][(first_pos[1] + 1) % 5]
                cipher += full_key_array[second_pos[0]][(second_pos[1] + 1) %
                                                        5]
            elif first_pos[1] == second_pos[1]:
                cipher = full_key_array[(first_pos[0] + 1) % 5][first_pos[1]]
                cipher += full_key_array[(second_pos[0] + 1) %
                                         5][second_pos[1]]
            else:
                cipher = full_key_array[first_pos[0]][second_pos[1]]
                cipher += full_key_array[second_pos[0]][first_pos[1]]

            encrypted_text += cipher

        return Data(data_type=DataType.TEXT, data=encrypted_text)

    def _do_decrypt(self, data: Data, key: Key) -> Data:
        """Decrypt data"""
        string_array = self._transform_text(data)

        full_key_array = self._transform_key(string_array)

        encrypted_array = string_array - full_key_array

        encrypted_array = np.mod(encrypted_array, 26)

        encrypted_array += ord('a')

        return Data(data_type=DataType.TEXT,
                    data=''.join(map(chr, encrypted_array)))

    def _transform_key(self, key: Key):
        original_key = StringUtil.get_unique_char(key.data[0].lower())
        normalized_key = StringUtil.strip_non_alphabet(original_key)
        normalized_key = StringUtil.remove_space(normalized_key)
        padded_key = StringUtil.pad_alphabet(normalized_key)
        padded_key = StringUtil.remove_char(padded_key, 'j')

        key_array = np.array(list(padded_key))

        return np.reshape(key_array, (5, 5))

    def _transform_text(self, data: Data):
        raw_text = StringUtil.strip_non_alphabet(data.get_text()).lower()
        no_space_text = StringUtil.remove_space(raw_text)
        grouped_text = []

        current_char = ''
        is_first_char = True
        i = 0
        while (i < len(no_space_text)):
            if is_first_char:
                current_char = no_space_text[i]
                is_first_char = False
                i += 1

                if i >= len(no_space_text):
                    current_char += 'x'
                    grouped_text.append(current_char)

            else:
                if no_space_text[i] != current_char:
                    current_char += no_space_text[i]
                    grouped_text.append(current_char)
                    current_char = ''
                    i += 1

                else:
                    current_char += 'x'
                    grouped_text.append(current_char)

                is_first_char = True

        return np.array(grouped_text)


if __name__ == "__main__":
    engine = PlayfairEngine()
    test_key = Key(KeyType.STRING, ['JALAN GANESHA SEPULUH'])
    test_data = Data(DataType.TEXT, 'temui ibu nanti malam')

    print(engine._transform_key(test_key))
    print(engine._transform_text(test_data))
    result = engine._do_encrypt(test_data, test_key)
    print(result.get_text())