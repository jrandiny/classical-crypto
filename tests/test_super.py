from crypto.engine.super_engine import SuperEngine
from crypto.engine.base_engine import *
from crypto.engine.engine_factory import *
from crypto.util.string_util import StringUtil

import pytest


def test_init():
    engine = SuperEngine()
    assert engine.capabilities.key_length == 1
    assert engine.capabilities.key_type == KeyType.STRING
    assert engine.capabilities.support_file == False
    assert engine.capabilities.support_text == True


def test_generate_key():
    engine = SuperEngine()
    generated_key = engine.generate_random_key()

    assert generated_key.key_type == KeyType.STRING
    assert len(generated_key.data) == 1
    assert type(generated_key.data[0]) == str


def test_encrypt_decrypt():
    engine = SuperEngine()

    test_key = Key(KeyType.STRING, ['key'])
    test_data = Data(DataType.TEXT, 'Example text')

    expected_result = 'ybojtwcxoxh'

    result = engine.encrypt(test_data, test_key)

    assert result.data_type == DataType.TEXT
    assert result.text == expected_result

    decrypted_result = engine.decrypt(result, test_key)

    assert decrypted_result.data_type == DataType.TEXT
    assert decrypted_result.text == 'exampletext'