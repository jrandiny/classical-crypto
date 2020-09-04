from crypto.engine.affine_engine import AffineEngine
from crypto.engine.base_engine import *
from crypto.engine.engine_factory import *
from crypto.util.string_util import StringUtil

import pytest


def test_init():
    engine = AffineEngine()
    assert engine.capabilities.key_length == 3
    assert engine.capabilities.key_type == KeyType.NUMBER
    assert engine.capabilities.support_file == False
    assert engine.capabilities.support_text == True


def test_capabilities_guard():
    engine = AffineEngine()
    invalid_key_type = Key(KeyType.STRING, ['avc'])
    invalid_key_length = Key(KeyType.NUMBER, [1, 2])
    invalid_key_parameter = Key(KeyType.NUMBER, [26, 14, 100])
    valid_key = Key(KeyType.NUMBER, [26, 15, 2])

    invalid_data = Data(DataType.FILE, 'fakepath')
    valid_data = Data(DataType.TEXT, 'test')

    with pytest.raises(Exception):
        engine.encrypt(valid_data, invalid_key_type)

    with pytest.raises(Exception):
        engine.encrypt(valid_data, invalid_key_length)

    with pytest.raises(Exception):
        engine.encrypt(invalid_data, valid_key)

    with pytest.raises(Exception):
        engine.encrypt(valid_data, invalid_key_parameter)

    engine.encrypt(valid_data, valid_key)


def test_generate_key():
    engine = AffineEngine()
    generated_key = engine.generate_random_key()

    assert generated_key.key_type == KeyType.NUMBER
    assert len(generated_key.data) == 3
    assert type(generated_key.data[0]) == int


def test_encrypt_decrypt():
    engine = AffineEngine()

    test_key = Key(KeyType.NUMBER, [26, 7, 10])
    test_data = Data(DataType.TEXT, 'kripto')

    expected_result = 'czolne'

    result = engine.encrypt(test_data, test_key)

    assert result.data_type == DataType.TEXT
    assert result.text == expected_result

    decrypted_result = engine.decrypt(result, test_key)

    assert decrypted_result.data_type == DataType.TEXT
    assert decrypted_result.text == 'kripto'