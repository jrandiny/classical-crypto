from crypto.engine.base_engine import BaseEngine
from crypto.engine.autokey_vigenere_engine import AutokeyVigenereEngine
from crypto.engine.full_vigenere_cipher import FullVigenereEngine
from crypto.engine.vigenere_engine import VigenereEngine
from crypto.engine.playfair_engine import PlayfairEngine
from enum import Enum


class EngineType(Enum):
    VIGENERE = 'vigenere'
    VIGENERE_AUTOKEY = 'vigenere_autokey'
    VIGENERE_FULL = 'vigenere_full'
    PLAYFAIR = 'playfair'

    @staticmethod
    def list():
        return list(map(lambda engine: engine.value, EngineType))


class EngineFactory():
    @staticmethod
    def create_engine(engine_type: EngineType) -> BaseEngine:
        if engine_type == EngineType.VIGENERE:
            return VigenereEngine()
        elif engine_type == EngineType.VIGENERE_AUTOKEY:
            return AutokeyVigenereEngine()
        elif engine_type == EngineType.VIGENERE_FULL:
            return FullVigenereEngine()
        elif engine_type == EngineType.PLAYFAIR:
            return PlayfairEngine()
        else:
            raise Exception('Unsupported engine')
