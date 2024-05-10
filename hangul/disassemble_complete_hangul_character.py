from .constants import (
    COMPLETE_HANGUL_END_CHARCODE,
    COMPLETE_HANGUL_START_CHARCODE,
    HANGUL_CHARACTERS_BY_FIRST_INDEX,
    HANGUL_CHARACTERS_BY_LAST_INDEX,
    HANGUL_CHARACTERS_BY_MIDDLE_INDEX,
    NUMBER_OF_JONGSUNG,
    NUMBER_OF_JUNGSUNG,
)


def disassemble_complete_hangul_character(letter):
    char_code = ord(letter)

    is_complete_hangul = (
        COMPLETE_HANGUL_START_CHARCODE <= char_code <= COMPLETE_HANGUL_END_CHARCODE
    )

    if not is_complete_hangul:
        return None

    hangul_code = char_code - COMPLETE_HANGUL_START_CHARCODE

    last_index = hangul_code % NUMBER_OF_JONGSUNG
    middle_index = (
        (hangul_code - last_index) // NUMBER_OF_JONGSUNG
    ) % NUMBER_OF_JUNGSUNG
    first_index = (hangul_code - last_index) // NUMBER_OF_JONGSUNG // NUMBER_OF_JUNGSUNG

    return {
        "first": HANGUL_CHARACTERS_BY_FIRST_INDEX[first_index],
        "middle": HANGUL_CHARACTERS_BY_MIDDLE_INDEX[middle_index],
        "last": HANGUL_CHARACTERS_BY_LAST_INDEX[last_index],
    }
