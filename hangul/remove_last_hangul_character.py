from hangul.internal.utils import exclude_last_element

from .combine_hangul_character import combine_hangul_character
from .disassemble import disassemble_hangul_to_groups


def remove_last_hangul_character(words):
    """
    인자로 주어진 한글 문자열에서 가장 마지막 문자 하나를 제거하여 반환합니다.
    예시:
    removeLastHangulCharacter('안녕하세요 값') -> '안녕하세요 갑'
    removeLastHangulCharacter('프론트엔드') -> '프론트엔ㄷ'
    removeLastHangulCharacter('일요일') -> '일요이'
    """
    disassembled_groups = disassemble_hangul_to_groups(words)
    if not disassembled_groups:
        return ""

    # Extract all but the last group
    without_last_character = disassembled_groups[:-1]
    last_character = disassembled_groups[-1]

    # Process all groups except the last to recombine them
    def maybe_combine_hangul_character(group):
        if len(group) >= 3:
            first, middle, *last = group
            return combine_hangul_character(first, middle, "".join(last))
        elif len(group) == 2:
            return combine_hangul_character(group[0], group[1])
        return group[0]

    combined_characters = [
        maybe_combine_hangul_character(group) for group in without_last_character
    ]

    # Handle the last character group, removing its last element
    last_character, _ = exclude_last_element(last_character)
    result = maybe_combine_hangul_character(last_character)

    return "".join(combined_characters + [result])
