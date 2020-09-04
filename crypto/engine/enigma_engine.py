from crypto.engine.base_engine import BaseEngine, EngineCapabilities
from crypto.engine.data import *
from crypto.engine.key import *

from crypto.util.string_util import StringUtil

from nptyping import NDArray
from typing import List

import copy
import numpy as np
import random


class EnigmaRotor():
    def __init__(self, wheel_left: str, wheel_right: str, notch: List[str]):
        left_array = list(wheel_left.lower())
        right_array = list(wheel_right.lower())

        self._left_wheel = [0] * 26
        self._right_wheel = [0] * 26

        for index, character in enumerate(left_array):
            found_index = right_array.index(character)
            self._left_wheel[index] = found_index
            self._right_wheel[found_index] = index

        self._wheel_rotation = 0

        self._notch = list(map(lambda x: (ord(x.lower()) - ord('a') + 1) % 26, notch))

    def set_rotation(self, rotation: int):
        if rotation < 0 or rotation > 25:
            raise Exception('Invalid rotation')
        self._wheel_rotation = rotation

    def rotate(self) -> bool:
        self._wheel_rotation += 1
        self._wheel_rotation %= 26

        return self._wheel_rotation in self._notch

    def route(self, alphabet: int, reverse: bool = False) -> int:
        index = (alphabet + self._wheel_rotation) % 26
        if reverse:
            return (self._left_wheel[index] - self._wheel_rotation) % 26
        else:
            return (self._right_wheel[index] - self._wheel_rotation) % 26


class EnigmaEngine(BaseEngine):
    """Enigma machine engine based on Enigma M3"""
    def __init__(self, *args):
        self._standard_rotor = [
            ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ['Q']],
            ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'AJDKSIRUXBLHWTMCQGZNPYFVOE', ['E']],
            ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', ['V']],
            ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ESOVPZJAYQUIRHXLNFTGKDCMWB', ['J']],
            ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'VZBRGITYUPSDNHLXAWMJQOFECK', ['Z']],
            ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'JPGVOUMFYQBENHZRDKASXLICTW', ['Z', 'M']],
            ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'NZJHGRCXMYSWBOUFAIVLPEKQDT', ['Z', 'M']],
            ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'FKQHTLXOCBJSPDZRAMEWNIUYGV', ['Z', 'M']]
        ]

        # UKW-B and UKW-C reflector
        self._standar_reflector = [
            ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'YRUHQSLDPXNGOKMIEBFZCWVJAT', []],
            ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'FVPJIAOYEDRZXWGCTKUQSBNMHL', []]
        ]

        if len(args) == 0:
            super().__init__(
                EngineCapabilities(
                    support_file=False, support_text=True, key_type=KeyType.NUMBER, key_length=6
                )
            )
        else:
            super().__init__(args[0])

    def generate_random_key(self) -> Key:
        return Key(
            KeyType.NUMBER, [
                random.randint(0, 7),
                random.randint(0, 25),
                random.randint(0, 7),
                random.randint(0, 25),
                random.randint(0, 7),
                random.randint(0, 25),
            ]
        )

    def _do_encrypt(self, data: Data, key: Key) -> Data:
        enigma_rotor = self._init_key(key)
        text_array = list(StringUtil.strip_non_alphabet(data.text))

        output_str = ''

        for character in text_array:
            alphabet = ord(character) - ord('a')
            self._rotate_rotor(enigma_rotor)

            target_index = self._pass_rotor(enigma_rotor, alphabet)

            output_str += chr(target_index + ord('a'))

        return Data(data_type=DataType.TEXT, data=output_str)

    def _do_decrypt(self, data: Data, key: Key) -> Data:
        return self._do_encrypt(data, key)

    def _pass_rotor(self, enigma_rotor: List[EnigmaRotor], start_index: int) -> int:
        target_index = enigma_rotor[2].route(start_index)
        target_index = enigma_rotor[1].route(target_index)
        target_index = enigma_rotor[0].route(target_index)
        target_index = enigma_rotor[3].route(target_index)
        target_index = enigma_rotor[0].route(target_index, True)
        target_index = enigma_rotor[1].route(target_index, True)
        return enigma_rotor[2].route(target_index, True)

    def _rotate_rotor(self, enigma_rotor: List[EnigmaRotor]):
        if enigma_rotor[2].rotate():
            if enigma_rotor[1].rotate():
                enigma_rotor[0].rotate()

    def _init_key(self, key: Key) -> List[EnigmaRotor]:
        enigma_rotor = []
        for rotor_index, rotation in zip(key.data[::2], key.data[1::2]):
            config = self._standard_rotor[rotor_index]
            temp_rotor = EnigmaRotor(config[0], config[1], config[2])
            temp_rotor.set_rotation(rotation)
            enigma_rotor.append(temp_rotor)

        enigma_rotor.append(
            EnigmaRotor(self._standar_reflector[0][0], self._standar_reflector[0][1], [])
        )

        return enigma_rotor
