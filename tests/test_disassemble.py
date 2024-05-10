from hangul.disassemble import disassemble_hangul, disassemble_hangul_to_groups


def test_disassemble_hangul_to_groups_single_syllable():
    """값"""
    assert disassemble_hangul_to_groups("값") == [["ㄱ", "ㅏ", "ㅂ", "ㅅ"]]


def test_disassemble_hangul_to_groups_sentence():
    """값이 비싸다"""
    assert disassemble_hangul_to_groups("값이 비싸다") == [
        ["ㄱ", "ㅏ", "ㅂ", "ㅅ"],
        ["ㅇ", "ㅣ"],
        [" "],
        ["ㅂ", "ㅣ"],
        ["ㅆ", "ㅏ"],
        ["ㄷ", "ㅏ"],
    ]


def test_disassemble_hangul_to_groups_phrase():
    """사과 짱"""
    assert disassemble_hangul_to_groups("사과 짱") == [
        ["ㅅ", "ㅏ"],
        ["ㄱ", "ㅗ", "ㅏ"],
        [" "],
        ["ㅉ", "ㅏ", "ㅇ"],
    ]


def test_disassemble_hangul_to_groups_double_jamo():
    """ㄵ"""
    assert disassemble_hangul_to_groups("ㄵ") == [["ㄴ", "ㅈ"]]


def test_disassemble_hangul_to_groups_complex_vowel():
    """ㅘ"""
    assert disassemble_hangul_to_groups("ㅘ") == [["ㅗ", "ㅏ"]]


def test_disassemble_hangul_single_syllable():
    """값"""
    assert disassemble_hangul("값") == "ㄱㅏㅂㅅ"


def test_disassemble_hangul_sentence():
    """값이 비싸다"""
    assert disassemble_hangul("값이 비싸다") == "ㄱㅏㅂㅅㅇㅣ ㅂㅣㅆㅏㄷㅏ"


def test_disassemble_hangul_phrase():
    """사과 짱"""
    assert disassemble_hangul("사과 짱") == "ㅅㅏㄱㅗㅏ ㅉㅏㅇ"


def test_disassemble_hangul_double_jamo():
    """ㄵ"""
    assert disassemble_hangul("ㄵ") == "ㄴㅈ"


def test_disassemble_hangul_complex_vowel():
    """ㅘ"""
    assert disassemble_hangul("ㅘ") == "ㅗㅏ"
