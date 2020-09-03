from crypto.engine.vigenere_engine import VigenereEngine
from crypto.engine.extended_vigenere_engine import ExtendedVigenereEngine
from crypto.engine.base_engine import *
from crypto.engine.engine_factory import *
from crypto.util.string_util import StringUtil

import pytest


def test_init():
    engine = ExtendedVigenereEngine()
    assert engine.capabilities.key_length == 1
    assert engine.capabilities.key_type == KeyType.STRING
    assert engine.capabilities.support_file == True
    assert engine.capabilities.support_text == True


def test_encrypt_decrypt():
    engine = ExtendedVigenereEngine()

    test_key = Key(KeyType.STRING, ['key'])
    test_data = Data(DataType.TEXT, 'Example text')

    expected_result = 'ÐÝÚØÕåÐ\x85íÐÝí'

    result = engine.encrypt(test_data, test_key)

    assert result.data_type == DataType.TEXT
    assert result.get_text() == expected_result

    decrypted_result = engine.decrypt(result, test_key)

    assert decrypted_result.data_type == DataType.TEXT
    assert decrypted_result.get_text() == 'example text'