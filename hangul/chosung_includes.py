import re

from .disassemble import disassemble_hangul_to_groups
from .utils import can_be_chosung, get_chosung


def chosung_includes(x, y):
    trimmed_y = re.sub(r"\s", "", y)

    if not is_only_chosung(trimmed_y):
        return False

    chosung_x = re.sub(r"\s", "", get_chosung(x))
    chosung_y = trimmed_y

    return chosung_y in chosung_x


def is_only_chosung(str):
    """
    문자열이 한글 초성으로만 주어진 경우 True를 반환합니다.
    """
    groups = disassemble_hangul_to_groups(str)
    if not groups:
        return False

    return all(
        len(disassembled) == 1 and can_be_chosung(disassembled[0])
        for disassembled in groups
    )
