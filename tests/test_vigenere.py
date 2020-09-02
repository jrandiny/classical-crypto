from crypto.engine.vigenere_engine import VigenereEngine
from crypto.engine.base_engine import *
from crypto.engine.engine_factory import *
from crypto.util.string_util import StringUtil

import pytest


def test_init():
    engine = VigenereEngine()
    assert engine.capabilities.key_length == 1
    assert engine.capabilities.key_type == KeyType.STRING
    assert engine.capabilities.support_file == False
    assert engine.capabilities.support_text == True


def test_capabilities_guard():
    engine = VigenereEngine()
    invalid_key_type = Key(KeyType.NUMBER, [1])
    invalid_key_length = Key(KeyType.STRING, ['a', 'b'])
    valid_key = Key(KeyType.STRING, ['a'])

    invalid_data = Data(DataType.FILE, 'fakepath')
    valid_data = Data(DataType.TEXT, 'test')

    with pytest.raises(Exception):
        engine.encrypt(valid_data, invalid_key_type)

    with pytest.raises(Exception):
        engine.encrypt(valid_data, invalid_key_length)

    with pytest.raises(Exception):
        engine.encrypt(invalid_data, valid_key)

    engine.encrypt(valid_data, valid_key)


def test_encrypt_decrypt():
    engine = VigenereEngine()

    test_key = Key(KeyType.STRING, ['key'])
    test_data = Data(DataType.TEXT, 'Example text')

    expected_result = 'obywtjoxchx'

    result = engine.encrypt(test_data, test_key)

    assert result == expected_result

    encrypted_data = Data(DataType.TEXT, result)

    decrypted_result = engine.decrypt(encrypted_data, test_key)

    assert decrypted_result == 'exampletext'