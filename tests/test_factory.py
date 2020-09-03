from crypto.engine.engine_factory import *
from crypto.engine.vigenere_engine import VigenereEngine


def test_list_engine():
    engine_list = EngineType.list()
    assert len(engine_list) == 4


def test_create_engine():
    vigenere = EngineFactory.create_engine(EngineType.VIGENERE)
    assert type(vigenere) == VigenereEngine