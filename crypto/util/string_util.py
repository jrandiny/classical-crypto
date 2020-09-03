import textwrap
import re
import random
import string


class StringUtil:
    @staticmethod
    def strip_non_alphabet(input: str) -> str:
        return re.sub("[^a-zA-Z]+", "", input)

    @staticmethod
    def remove_char(input: str, char: str) -> str:
        return input.replace(char, '')

    @staticmethod
    def split_to_group(input: str) -> str:
        input_no_space = StringUtil.remove_char(input, ' ')
        return ' '.join(textwrap.wrap(input_no_space, width=5))

    @staticmethod
    def generate_random_string(length: int) -> str:
        return ''.join(
            random.choice(string.ascii_lowercase) for _ in range(length))
