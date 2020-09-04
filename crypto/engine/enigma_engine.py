from crypto.engine.base_engine import BaseEngine, EngineCapabilities
from crypto.engine.data import *
from crypto.engine.key import *

from crypto.util.string_util import StringUtil

from nptyping import NDArray
from typing import List

import random
import numpy as np


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

        self._wheel_rotate = 0

        self._notch = list(map(lambda x: (ord(x.lower()) - ord('a') + 1) % 26, notch))

        print(self._left_wheel)

    def set_rotation(self, rotation: int):
        if rotation < 0 or rotation > 25:
            raise Exception('Invalid rottion')
        self._wheel_rotate = rotation

    def rotate(self) -> bool:
        self._wheel_rotate += 1
        self._wheel_rotate %= 26

        return self._wheel_rotate in self._notch

    def route(self, alphabet: int, reverse: bool = False) -> int:
        index = (alphabet + self._wheel_rotate) % 26

        if reverse:
            return self._left_wheel[index]
        else:
            return self._right_wheel[index]


class EnigmaEngine(BaseEngine):
    def __init__(self, *args):
        self._standard_rotor = []
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
        return data

    def _do_decrypt(self, data: Data, key: Key) -> Data:
        return data