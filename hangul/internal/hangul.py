import re

from ..combine_hangul_character import (
    combine_hangul_character,
    combine_vowels,
    curried_combine_hangul_character,
)
from ..disassemble import disassemble_hangul_to_groups
from ..remove_last_hangul_character import remove_last_hangul_character
from ..utils import can_be_chosung, can_be_jongsung, can_be_jungsung, has_single_batchim
from .utils import exclude_last_element, is_blank, join_string


def is_hangul_character(character):
    """
    Returns True if the character is a Hangul syllable.
    """
    return re.match(r"^[가-힣]$", character) is not None


def is_hangul_alphabet(character):
    """
    Returns True if the character is a Hangul Jamo.
    """
    return re.match(r"^[ㄱ-ㅣ]$", character) is not None


def binary_assemble_hangul_alphabets(source, next_character):
    """
    두 개의 한글 자모를 합칩니다. 완성된 한글 문자는 취급하지 않습니다.
    예시:
    binary_assemble_hangul_alphabets('ㄱ', 'ㅏ') -> '가'
    binary_assemble_hangul_alphabets('ㅗ', 'ㅏ') -> 'ㅘ'
    """
    if can_be_jungsung(f"{source}{next_character}"):
        return combine_vowels(source, next_character)

    is_consonant_source = not can_be_jungsung(source)
    if is_consonant_source and can_be_jungsung(next_character):
        return combine_hangul_character(source, next_character)

    return join_string(source, next_character)


def link_hangul_characters(source, next_character):
    """
    연음 법칙을 적용하여 두 개의 한글 문자를 연결합니다.
    """
    source_jamo = disassemble_hangul_to_groups(source)[0]
    _, last_jamo = exclude_last_element(source_jamo)

    return join_string(
        remove_last_hangul_character(source),
        combine_hangul_character(last_jamo, next_character),
    )


def binary_assemble_hangul_characters(source, next_character):
    """
    인자로 받은 한글 문자 2개를 합성합니다.
    예시:
    binary_assemble_hangul_characters('ㄱ', 'ㅏ') -> '가'
    binary_assemble_hangul_characters('가', 'ㅇ') -> '강'
    binary_assemble_hangul_characters('갑', 'ㅅ') -> '값'
    binary_assemble_hangul_characters('깎', 'ㅏ') -> '까까'
    """
    assert is_hangul_character(source) or is_hangul_alphabet(
        source
    ), f"Invalid source character: {source}. Source must be one character."

    assert is_hangul_alphabet(
        next_character
    ), f"Invalid next character: {next_character}. Next character must be one of the chosung, jungsung, or jongsung."

    source_jamos = disassemble_hangul_to_groups(source)[0]
    is_single_character = len(source_jamos) == 1
    if is_single_character:
        source_character = source_jamos[0]
        return binary_assemble_hangul_alphabets(source_character, next_character)

    rest_jamos, last_jamo = exclude_last_element(source_jamos)

    need_linking = can_be_chosung(last_jamo) and can_be_jungsung(next_character)
    if need_linking:
        return link_hangul_characters(source, next_character)

    fix_consonant = curried_combine_hangul_character
    combine_jungsung = fix_consonant(rest_jamos[0])

    if can_be_jungsung(f"{last_jamo}{next_character}"):
        return combine_jungsung(f"{last_jamo}{next_character}")()

    if can_be_jungsung(last_jamo) and can_be_jongsung(next_character):
        return combine_jungsung(last_jamo)(next_character)

    fix_vowel = combine_jungsung
    if len(rest_jamos) >= 2:
        combine_jongsung = fix_vowel(rest_jamos[1])

        last_consonant = last_jamo

        if has_single_batchim(source) and can_be_jongsung(
            f"{last_consonant}{next_character}"
        ):
            return combine_jongsung(f"{last_consonant}{next_character}")

    return join_string(source, next_character)


def binary_assemble_hangul(source, next_character):
    """
    인자로 받은 한글 문장과 한글 문자 하나를 합성합니다.
    예시:
    binary_assemble_hangul('저는 고양이를 좋아합닏', 'ㅏ') -> '저는 고양이를 좋아합니다'
    binary_assemble_hangul('저는 고양이를 좋아합', 'ㅅ') -> '저는 고양이를 좋아핪'
    binary_assemble_hangul('저는 고양이를 좋아하', 'ㅏ') -> '저는 고양이를 좋아하ㅏ'
    """
    rest, last_character = exclude_last_element(list(source))
    need_join_string = is_blank(last_character) or is_blank(next_character)

    return join_string(
        *rest,
        join_string(last_character, next_character)
        if need_join_string
        else binary_assemble_hangul_characters(last_character, next_character),
    )
