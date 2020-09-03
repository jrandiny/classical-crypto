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

    expected_result = 'obyqmlqipbm'

    result = engine.encrypt(test_data, test_key)

    assert result == expected_result

    # encrypted_data = Data(DataType.TEXT, result)

    # decrypted_result = engine.decrypt(encrypted_data, test_key)

    # assert decrypted_result == 'exampletext'