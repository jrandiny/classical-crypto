from crypto.engine.base_engine import BaseEngine
from crypto.engine.autokey_vigenere_engine import AutokeyVigenereEngine
from crypto.engine.full_vigenere_cipher import FullVigenereEngine
from crypto.engine.vigenere_engine import VigenereEngine
from crypto.engine.playfair_engine import PlayfairEngine
from crypto.engine.hill_engine import HillEngine
from crypto.engine.affine_engine import AffineEngine
from enum import Enum


class EngineType(Enum):
    VIGENERE = 'Vigenere Cipher Standard'
    VIGENERE_AUTOKEY = 'Auto-key Vigenere Cipher'
    VIGENERE_FULL = 'Full Vigenere Cipher'
    PLAYFAIR = 'Playfair Cipher'
    HILL = 'Hill Cipher'
    AFFINE = 'Affine Cipher'
    VIGENERE_EXTENDED = 'Extended Vigenere Cipher'
    SUPER_ENCRYPTION = 'Super Encryption'
    ENIGMA = 'Enigma Cipher (M3)'

    @staticmethod
    def list():
        return list(map(lambda engine: engine, EngineType))


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
        elif engine_type == EngineType.HILL:
            return HillEngine()
        elif engine_type == EngineType.AFFINE:
            return AffineEngine()
        else:
            raise Exception('Unsupported engine')
