from crypto.engine.engine_factory import *
from crypto.engine.vigenere_engine import VigenereEngine


def test_list_engine():
    engine_list = EngineType.list()
    assert len(engine_list) == 9


def test_create_engine():
    engine_list = EngineType.list()

    for engine in engine_list:
        EngineFactory.create_engine(engine)