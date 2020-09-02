from crypto.engine.base_engine import BaseEngine
from crypto.engine.vigenere_engine import VigenereEngine
from enum import Enum


class EngineType(Enum):
    VIGENERE = 'vigenere'

    @staticmethod
    def list():
        return list(map(lambda engine: engine.value, EngineType))


class EngineFactory():
    @staticmethod
    def create_engine(engine_type: EngineType) -> BaseEngine:
        if engine_type == EngineType.VIGENERE:
            return VigenereEngine()
        else:
            raise Exception('Unsupported engine')
