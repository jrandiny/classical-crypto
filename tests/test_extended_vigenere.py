from crypto.engine.vigenere_engine import VigenereEngine
from crypto.engine.extended_vigenere_engine import ExtendedVigenereEngine
from crypto.engine.base_engine import *
from crypto.engine.engine_factory import *
from crypto.util.file_util import FileUtil
from crypto.util.string_util import StringUtil

import pytest
import hashlib
import os
import time


def test_init():
    engine = ExtendedVigenereEngine()
    assert engine.capabilities.key_length == 1
    assert engine.capabilities.key_type == KeyType.STRING
    assert engine.capabilities.support_file == True
    assert engine.capabilities.support_text == True


def test_encrypt_decrypt_text():
    engine = ExtendedVigenereEngine()

    test_key = Key(KeyType.STRING, ['key'])
    test_data = Data(DataType.TEXT, 'Example text')

    expected_result = 'ÐÝÚØÕåÐ\x85íÐÝí'

    result = engine.encrypt(test_data, test_key)

    assert result.data_type == DataType.TEXT
    assert result.text == expected_result

    decrypted_result = engine.decrypt(result, test_key)

    assert decrypted_result.data_type == DataType.TEXT
    assert decrypted_result.text == 'example text'


def test_encrypt_decrypt_file():
    engine = ExtendedVigenereEngine()

    current_dir = os.path.dirname(__file__)
    original_file_path = os.path.join(current_dir, 'file.jpg')
    encrypted_file_path = os.path.join(current_dir, 'test_encrypted.jpg')
    decrypted_file_path = os.path.join(current_dir, 'test_decrypted.jpg')

    test_key = Key(KeyType.STRING, ['key'])
    test_data = Data(DataType.FILE, original_file_path)

    result = engine.encrypt(test_data, test_key)

    result.move_file(encrypted_file_path)

    original_md5 = hashlib.md5()
    with open(original_file_path, "rb") as f:
        while block := f.read(8192):
            original_md5.update(block)

    encrypted_md5 = hashlib.md5()
    with open(encrypted_file_path, "rb") as f:
        while block := f.read(8192):
            encrypted_md5.update(block)

    assert original_md5.hexdigest() != encrypted_md5.hexdigest()
    assert result.data_type == DataType.FILE

    decrypted_result = engine.decrypt(result, test_key)

    decrypted_result.move_file(decrypted_file_path)

    decrypted_md5 = hashlib.md5()
    with open(decrypted_file_path, "rb") as f:
        while block := f.read(8192):
            decrypted_md5.update(block)

    assert original_md5.hexdigest() == decrypted_md5.hexdigest()
    assert decrypted_result.data_type == DataType.FILE

    os.remove(encrypted_file_path)
    os.remove(decrypted_file_path)