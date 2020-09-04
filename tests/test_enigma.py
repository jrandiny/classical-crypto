from crypto.engine.enigma_engine import *


def test_init():
    pass


def test_rotor_init():
    rotor_1 = EnigmaRotor('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ['B'])

    # A -> E
    assert rotor_1.route(0) == 4

    # Y -> C
    assert rotor_1.route(24) == 2

    # J -> Z
    assert rotor_1.route(9) == 25

    assert not rotor_1.rotate()

    # A -> K
    assert rotor_1.route(0) == 10

    assert rotor_1.rotate()
