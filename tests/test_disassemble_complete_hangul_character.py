from hangul.disassemble_complete_hangul_character import (
    disassemble_complete_hangul_character,
)


def test_disassemble_complete_hangul_character_gabs():
    """값"""
    assert disassemble_complete_hangul_character("값") == {
        "first": "ㄱ",
        "middle": "ㅏ",
        "last": "ㅂㅅ",
    }


def test_disassemble_complete_hangul_character_ri():
    """리"""
    assert disassemble_complete_hangul_character("리") == {
        "first": "ㄹ",
        "middle": "ㅣ",
        "last": "",
    }


def test_disassemble_complete_hangul_character_bit():
    """빚"""
    assert disassemble_complete_hangul_character("빚") == {
        "first": "ㅂ",
        "middle": "ㅣ",
        "last": "ㅈ",
    }


def test_disassemble_complete_hangul_character_park():
    """박"""
    assert disassemble_complete_hangul_character("박") == {
        "first": "ㅂ",
        "middle": "ㅏ",
        "last": "ㄱ",
    }
