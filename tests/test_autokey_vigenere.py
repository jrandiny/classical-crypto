from crypto.engine.autokey_vigenere_engine import AutokeyVigenereEngine
from crypto.engine.base_engine import *
from crypto.engine.engine_factory import *
from crypto.util.string_util import StringUtil

import pytest


def test_init():
    engine = AutokeyVigenereEngine()
    assert engine.capabilities.key_length == 1
    assert engine.capabilities.key_type == KeyType.STRING
    assert engine.capabilities.support_file == False
    assert engine.capabilities.support_text == True


def test_encrypt_decrypt():
    engine = AutokeyVigenereEngine()

    test_key = Key(KeyType.STRING, ['key'])
    test_data = Data(DataType.TEXT, 'Example text')
    # completed_key = engine.complete_key(test_data, test_key)

    expected_result = 'obyqmlqipbm'

    result = engine.encrypt(test_data, test_key)

    assert result.data_type == DataType.TEXT
    assert result.text == expected_result

    decrypted_result = engine.decrypt(result, test_key)

    assert decrypted_result.data_type == DataType.TEXT
    assert decrypted_result.text == 'exampletext'