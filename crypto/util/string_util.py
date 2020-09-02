import textwrap
import re
import random
import string


class StringUtil:
    @staticmethod
    def strip_non_alphabet(input: str) -> str:
        return re.sub("[^a-zA-Z]+", "", input)

    @staticmethod
    def remove_space(input: str) -> str:
        return input.replace(' ', '')

    @staticmethod
    def split_to_group(input: str) -> str:
        input_no_space = StringUtil.remove_space(input)
        return ' '.join(textwrap.wrap(input_no_space, width=5))

    @staticmethod
    def generate_random_string(length: int) -> str:
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))