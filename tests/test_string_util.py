from crypto.util.string_util import StringUtil


def test_strip_non_alphabet():
    assert StringUtil.strip_non_alphabet('a1b2c3!@#$%') == 'abc'


def test_remove_space():
    assert StringUtil.remove_space('a b c d') == 'abcd'
    assert StringUtil.remove_space('abcd') == 'abcd'


def test_remove_char():
    assert StringUtil.remove_char('adbdc', 'd') == 'abc'


def test_split_to_group():
    assert StringUtil.split_to_group('12345678910') == '12345 67891 0'
    assert StringUtil.split_to_group('123') == '123'


def test_generate_random_string():
    assert len(StringUtil.generate_random_string(8)) == 8
    assert type(StringUtil.generate_random_string(8)) == str
    assert StringUtil.generate_random_string(8) != StringUtil.generate_random_string(8)


def test_strip_non_ascii():
    assert StringUtil.strip_non_ascii('abc网络😂d\x85') == 'abcd\x85'


def test_get_unique_char():
    assert StringUtil.get_unique_char('aaaaaab') == 'ab'


def test_pad_alphabet():
    assert StringUtil.pad_alphabet('piscolkern') == 'piscolkernabdfghjmqtuvwxyz'