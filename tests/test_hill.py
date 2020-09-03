from crypto.engine.hill_engine import HillEngine
from crypto.engine.base_engine import *
from crypto.engine.engine_factory import *
from crypto.util.string_util import StringUtil

import pytest


def test_init():
    engine = HillEngine()
    assert engine.capabilities.key_length == -1
    assert engine.capabilities.key_type == KeyType.NUMBER
    assert engine.capabilities.support_file == False
    assert engine.capabilities.support_text == True


def test_capabilities_guard():
    engine = HillEngine()
    invalid_key_type = Key(KeyType.STRING, ['avc'])
    # invalid_key_length = Key(KeyType.NUMBER, [1, 2]) # bypassed
    invalid_key_parameter = Key(KeyType.NUMBER, [26, 14, 100])
    valid_key = Key(KeyType.NUMBER, [3, 17, 17, 5, 21, 18, 21, 2, 2, 19])

    invalid_data = Data(DataType.FILE, 'fakepath')
    valid_data = Data(DataType.TEXT, 'test')

    with pytest.raises(Exception):
        engine.encrypt(valid_data, invalid_key_type)

    # with pytest.raises(Exception):
    #     engine.encrypt(valid_data, invalid_key_length) # bypassed

    with pytest.raises(Exception):
        engine.encrypt(invalid_data, valid_key)

    with pytest.raises(Exception):
        engine.encrypt(valid_data, invalid_key_parameter)

    engine.encrypt(valid_data, valid_key)


def test_generate_key():
    engine = HillEngine()
    generated_key = engine.generate_random_key()

    assert generated_key.key_type == KeyType.NUMBER
    assert len(generated_key.data) == 10
    assert type(generated_key.data[0]) == int


def test_encrypt_decrypt():
    engine = HillEngine()

    test_key = Key(KeyType.NUMBER, [3, 17, 17, 5, 21, 18, 21, 2, 2, 19])
    test_data = Data(DataType.TEXT, 'paymoremoney')

    expected_result = 'lnshdlewmtrw'

    result = engine.encrypt(test_data, test_key)

    assert result.data_type == DataType.TEXT
    assert result.get_text() == expected_result

    decrypted_result = engine.decrypt(result, test_key)

    assert decrypted_result.data_type == DataType.TEXT
    assert decrypted_result.get_text() == 'paymoremoney'