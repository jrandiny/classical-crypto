from crypto.engine.full_vigenere_cipher import FullVigenereEngine
from crypto.engine.base_engine import *
from crypto.engine.engine_factory import *
from crypto.util.string_util import StringUtil

import pytest


def test_init():
    engine = FullVigenereEngine()
    assert engine.capabilities.key_length == 1 + (26 * 26)
    assert engine.capabilities.key_type == KeyType.STRING
    assert engine.capabilities.support_file == False
    assert engine.capabilities.support_text == True


def test_generate_key():
    engine = FullVigenereEngine()
    generated_key = engine.generate_random_key()

    assert generated_key.key_type == KeyType.STRING
    assert len(generated_key.data) == 1 + (26 * 26)
    assert len(generated_key.data[0]) > 1

    for i in range(1, 1 + (26 * 26), 26):
        assert len(set(generated_key.data[i:i + 26])) == 26


def test_encrypt_decrypt():
    engine = FullVigenereEngine()

    generated_key = Key(
        key_type=KeyType.STRING,
        data=[
            'key', 'q', 'c', 'a', 'g', 'r', 'f', 'd', 'l', 'v', 'n', 'y', 'u', 'w', 'o', 'h', 'p',
            'm', 'j', 'b', 'k', 't', 'z', 'x', 's', 'e', 'i', 'z', 'b', 'p', 'd', 'a', 'm', 'j',
            'v', 'o', 'q', 'c', 'g', 'n', 'f', 't', 'u', 'i', 'e', 's', 'w', 'y', 'r', 'k', 'x',
            'l', 'h', 'x', 'g', 'o', 'r', 'q', 'y', 'c', 'd', 't', 'u', 'h', 'w', 'l', 'z', 'k',
            'j', 'm', 'v', 'a', 'e', 'b', 'p', 'n', 's', 'f', 'i', 'd', 'u', 'e', 'a', 'o', 'b',
            'w', 'i', 's', 'k', 'c', 'h', 'q', 'f', 'r', 'n', 'p', 'y', 'v', 'z', 'g', 't', 'm',
            'j', 'l', 'x', 'g', 'f', 'c', 'r', 'm', 'd', 'a', 'x', 'p', 'o', 'w', 'i', 'y', 'j',
            'u', 'h', 'n', 'q', 'k', 'v', 'z', 'l', 'e', 's', 't', 'b', 'i', 's', 'j', 'e', 'n',
            'o', 'x', 'y', 'q', 'w', 'd', 'c', 'a', 'l', 't', 'v', 'k', 'u', 'z', 'h', 'f', 'r',
            'b', 'g', 'p', 'm', 's', 'b', 'n', 'm', 'd', 'x', 'h', 'w', 'u', 'j', 'a', 'i', 'k',
            'v', 'l', 'f', 'p', 'q', 'c', 't', 'g', 'e', 'o', 'z', 'r', 'y', 'f', 's', 'u', 'i',
            'w', 'm', 'x', 'y', 'e', 'r', 'd', 'o', 'q', 'h', 'c', 'l', 'b', 'n', 'j', 'k', 't',
            'a', 'p', 'g', 'z', 'v', 'j', 'm', 'f', 'e', 'u', 'x', 'q', 's', 'v', 'b', 'p', 'i',
            'c', 'z', 'l', 'n', 'h', 'd', 'k', 'o', 'g', 'a', 'w', 'r', 'y', 't', 'g', 'o', 'w',
            'u', 'j', 'z', 'b', 'v', 'f', 'l', 'i', 'd', 'q', 'c', 'n', 'r', 'a', 'p', 'k', 'm',
            'y', 'x', 't', 'h', 'e', 's', 'o', 'n', 'r', 'x', 'z', 'g', 'w', 'c', 'a', 's', 'd',
            'h', 'e', 'l', 'y', 'j', 'v', 'b', 't', 'q', 'm', 'k', 'i', 'f', 'u', 'p', 'd', 'o',
            'n', 'y', 'a', 'q', 'h', 't', 'e', 'r', 'm', 'f', 'j', 'i', 'l', 'p', 'k', 's', 'c',
            'u', 'z', 'w', 'b', 'g', 'x', 'v', 'z', 'x', 'e', 'o', 'q', 'b', 'y', 't', 'k', 'l',
            'p', 'c', 'g', 's', 'n', 'u', 'r', 'd', 'f', 'j', 'a', 'w', 'v', 'm', 'h', 'i', 'x',
            'i', 'z', 'k', 'd', 'h', 'p', 's', 't', 'l', 'n', 'o', 'q', 'e', 'g', 'r', 'j', 'w',
            'c', 'b', 'f', 'y', 'm', 'u', 'a', 'v', 'm', 'r', 'j', 'u', 'k', 'c', 'i', 'a', 'p',
            'e', 'l', 'y', 'q', 'z', 'n', 'h', 'v', 'b', 'd', 's', 'f', 'o', 'w', 'x', 't', 'g',
            'a', 'x', 'd', 'j', 'h', 'm', 'r', 'q', 'k', 'e', 'f', 'n', 'w', 'z', 'v', 'p', 'c',
            's', 'y', 'i', 't', 'b', 'l', 'o', 'u', 'g', 'p', 's', 't', 'v', 'o', 'a', 'k', 'd',
            'w', 'r', 'y', 'q', 'e', 'b', 'x', 'j', 'n', 'h', 'l', 'f', 'z', 'm', 'c', 'g', 'i',
            'u', 's', 'y', 'v', 'o', 'l', 'j', 'x', 'w', 'c', 'n', 'u', 'h', 'q', 'i', 'g', 'r',
            'k', 'p', 'e', 'm', 'z', 'a', 'd', 'f', 't', 'b', 'r', 'i', 'm', 'a', 's', 'v', 'q',
            'l', 'b', 'w', 'c', 'y', 'd', 'g', 'z', 'j', 'f', 'e', 'u', 'o', 'k', 'x', 'n', 'h',
            't', 'p', 'q', 'j', 'p', 'z', 'r', 'm', 'u', 'a', 'x', 's', 'y', 'w', 'v', 'c', 'b',
            'd', 'o', 'n', 'i', 'h', 'e', 'k', 'f', 'g', 'l', 't', 'd', 'u', 'n', 'k', 't', 'g',
            'p', 'q', 'c', 'f', 'j', 'r', 's', 'v', 'w', 'x', 'e', 'z', 'l', 'h', 'o', 'a', 'm',
            'y', 'i', 'b', 'y', 't', 'd', 's', 'i', 'z', 'n', 'f', 'v', 'g', 'u', 'l', 'b', 'q',
            'e', 'k', 'o', 'a', 'r', 'w', 'j', 'h', 'c', 'p', 'x', 'm', 'v', 'p', 'z', 'm', 'c',
            'j', 'h', 'o', 's', 'r', 'k', 'g', 'e', 'd', 't', 'q', 'l', 'f', 'x', 'n', 'w', 'a',
            'u', 'i', 'b', 'y', 'y', 'c', 'q', 's', 'l', 'u', 'a', 'v', 'k', 'z', 'e', 'p', 'g',
            'x', 'j', 'd', 'h', 'o', 'i', 't', 'n', 'r', 'f', 'w', 'm', 'b', 'm', 'a', 't', 'p',
            'd', 'o', 'u', 's', 'e', 'v', 'x', 'k', 'h', 'q', 'g', 'r', 'l', 'b', 'i', 'f', 'w',
            'c', 'n', 'j', 'y', 'z', 'f', 'r', 'n', 'k', 'x', 'h', 'g', 'i', 'o', 'e', 'y', 'w',
            't', 'm', 'j', 'c', 'a', 's', 'q', 'b', 'p', 'u', 'd', 'l', 'z', 'v'
        ]
    )
    test_data = Data(DataType.TEXT, 'Example text')

    encrypted_data = engine.encrypt(test_data, generated_key)

    assert encrypted_data.data_type == DataType.TEXT
    assert encrypted_data.get_text() == 'zsmehkzvdfv'

    decrypted_data = engine.decrypt(encrypted_data, generated_key)

    assert decrypted_data.data_type == DataType.TEXT
    assert decrypted_data.get_text() == 'exampletext'
