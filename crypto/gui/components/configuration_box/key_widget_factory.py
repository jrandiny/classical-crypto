from enum import Enum

from crypto.engine.engine_factory import EngineType
from crypto.gui.components.configuration_box.base_key import BaseKey
from crypto.gui.components.configuration_box.string_key import StringKey
from crypto.gui.components.configuration_box.string_full_key import StringFullKey
from crypto.gui.components.configuration_box.hill_key import HillKey
from crypto.gui.components.configuration_box.affine_key import AffineKey
from crypto.gui.components.configuration_box.enigma_key import EnigmaKey


class KeyWidgetFactory():
    @staticmethod
    def create_widget(engine: EngineType) -> BaseKey:
        if engine == EngineType.HILL:
            return HillKey()
        elif engine == EngineType.VIGENERE_FULL:
            return StringFullKey()
        elif engine == EngineType.AFFINE:
            return AffineKey()
        elif engine == EngineType.ENIGMA:
            return EnigmaKey()
        else:
            return StringKey()
