from .constants import (
    HANGUL_CHARACTERS_BY_FIRST_INDEX,
    HANGUL_CHARACTERS_BY_LAST_INDEX,
    HANGUL_CHARACTERS_BY_MIDDLE_INDEX,
)
from .disassemble import disassemble_hangul, disassemble_hangul_to_groups
from .disassemble_complete_hangul_character import disassemble_complete_hangul_character


def has_batchim(string):
    """
    한글 문자열의 마지막 글자가 받침이 있는지 확인합니다.

    has_batchim('값')  # True
    has_batchim('토')  # False
    """
    if not string:
        return False
    last_char = string[-1]
    disassembled = disassemble_complete_hangul_character(last_char)
    return disassembled is not None and disassembled["last"] != ""


def has_single_batchim(string):
    """
    한글 문자열의 마지막 글자가 홑받침이 있는지 확인합니다.

    has_single_batchim('갑')  # True
    has_single_batchim('값')  # False
    has_single_batchim('토')  # False
    """
    last_char = string[-1] if string else None
    if last_char is None or not has_batchim(last_char):
        return False
    disassembled = disassemble_hangul(last_char)
    return len(disassembled) == 3


def get_chosung(word):
    """
    Extract the initial consonants from a word (e.g., '사과' -> 'ㅅㄱ').
    """
    return "".join([group[0] for group in disassemble_hangul_to_groups(word)])


def get_first_consonants(word):
    """
    Extract the initial consonants from a word; alias to get_chosung. (deprecated)
    """
    return get_chosung(word)


def can_be_chosung(character):
    """
    Check if a character can be an initial consonant in Hangul.
    """
    return character in HANGUL_CHARACTERS_BY_FIRST_INDEX


def can_be_jungsung(character):
    """
    Check if a character can be a vowel in Hangul.
    """
    return character in HANGUL_CHARACTERS_BY_MIDDLE_INDEX


def can_be_jongsung(character):
    """
    Check if a character can be a final consonant in Hangul.
    """
    return character in HANGUL_CHARACTERS_BY_LAST_INDEX
