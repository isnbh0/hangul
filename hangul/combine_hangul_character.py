from .constants import (
    COMPLETE_HANGUL_START_CHARCODE,
    DISASSEMBLED_VOWELS_BY_VOWEL,
    HANGUL_CHARACTERS_BY_FIRST_INDEX,
    HANGUL_CHARACTERS_BY_LAST_INDEX,
    HANGUL_CHARACTERS_BY_MIDDLE_INDEX,
)
from .utils import can_be_chosung, can_be_jongsung, can_be_jungsung


def combine_hangul_character(first_character, middle_character, last_character=""):
    """
    인자로 초성, 중성, 종성을 받아 하나의 한글 문자를 반환합니다.
    """
    if not (
        can_be_chosung(first_character)
        and can_be_jungsung(middle_character)
        and can_be_jongsung(last_character)
    ):
        raise ValueError(
            f"Invalid hangul Characters: {first_character}, {middle_character}, {last_character}"
        )

    num_of_middle_characters = len(HANGUL_CHARACTERS_BY_MIDDLE_INDEX)
    num_of_last_characters = len(HANGUL_CHARACTERS_BY_LAST_INDEX)

    first_character_index = HANGUL_CHARACTERS_BY_FIRST_INDEX.index(first_character)
    middle_character_index = HANGUL_CHARACTERS_BY_MIDDLE_INDEX.index(middle_character)
    last_character_index = HANGUL_CHARACTERS_BY_LAST_INDEX.index(last_character)

    first_index_of_target_consonant = (
        first_character_index * num_of_middle_characters * num_of_last_characters
    )
    first_index_of_target_vowel = middle_character_index * num_of_last_characters

    unicode = (
        COMPLETE_HANGUL_START_CHARCODE
        + first_index_of_target_consonant
        + first_index_of_target_vowel
        + last_character_index
    )

    return chr(unicode)


def curried_combine_hangul_character(first_character):
    """
    인자로 초성, 중성, 종성을 받아 하나의 한글 문자를 반환하는 `combine_hangul_character` 함수의 커링된 버전입니다.
    """
    return lambda middle_character: lambda last_character="": combine_hangul_character(
        first_character, middle_character, last_character
    )


def combine_vowels(vowel1, vowel2):
    """
    인자로 두 개의 모음을 받아 합성하여 겹모음을 생성합니다. 만약 올바른 한글 규칙으로 합성할 수 없는 모음들이라면 단순 Join합니다.
    """
    for key, value in DISASSEMBLED_VOWELS_BY_VOWEL.items():
        if value == f"{vowel1}{vowel2}":
            return key
    return f"{vowel1}{vowel2}"
