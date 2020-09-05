from crypto.engine.enigma_engine import *


def test_init():
    pass


def test_rotor_init():
    rotor_1 = EnigmaRotor('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ['B'])

    # A -> r-rotor-l -> E
    assert rotor_1.route(0) == 4

    # Y -> r-rotor-l -> C
    assert rotor_1.route(24) == 2

    # J -> r-rotor-l -> Z
    assert rotor_1.route(9) == 25

    assert not rotor_1.rotate()

    # A -> r-rotor-l -> K
    assert rotor_1.route(0) == 9

    assert rotor_1.rotate()

    # J -> l-rotor-r -> X
    assert rotor_1.route(9, True) == 2


def test_generate_key():
    engine = EnigmaEngine()
    generated_key = engine.generate_random_key()

    assert generated_key.key_type == KeyType.NUMBER
    assert len(generated_key.data) == 7
    assert generated_key.data[0] >= 0 and generated_key.data[0] <= 7
    assert generated_key.data[1] >= 0 and generated_key.data[1] <= 25
    assert generated_key.data[2] >= 0 and generated_key.data[2] <= 7
    assert generated_key.data[3] >= 0 and generated_key.data[3] <= 25
    assert generated_key.data[4] >= 0 and generated_key.data[4] <= 7
    assert generated_key.data[5] >= 0 and generated_key.data[5] <= 25
    assert generated_key.data[6] >= 0 and generated_key.data[5] <= 1


def test_encrypt_decrypt():
    engine = EnigmaEngine()
    sample_key = Key(key_type=KeyType.NUMBER, data=[1, 15, 6, 0, 7, 19, 0])
    sample_data = Data(data_type=DataType.TEXT, data='example text')

    result = engine.encrypt(sample_data, sample_key)

    assert result.data_type == DataType.TEXT
    assert result.text == 'wcvaacbkwii'

    decrypted_result = engine.decrypt(result, sample_key)

    assert decrypted_result.data_type == DataType.TEXT
    assert decrypted_result.text == 'exampletext'