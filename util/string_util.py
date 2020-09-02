import textwrap


class StringUtil:
    @staticmethod
    def remove_space(input: str) -> str:
        return input.replace(' ', '')

    @staticmethod
    def split_to_group(input: str) -> str:
        input_no_space = StringUtil.remove_space(input)
        return ' '.join(textwrap.wrap(input_no_space, width=5))