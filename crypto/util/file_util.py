from typing import BinaryIO

import os
import tempfile


class FileUtil:
    @staticmethod
    def generate_temp_file() -> BinaryIO:
        return tempfile.NamedTemporaryFile(delete=False)
