from functools import reduce

from .disassemble import disassemble_hangul
from .internal.hangul import binary_assemble_hangul


def assemble_hangul(words):
    """
    인자로 받은 배열에 담긴 한글 문장과 문자를 한글 규칙에 맞게 합성합니다.
    예시:
    assemble_hangul(['아버지가', ' ', '방ㅇ', 'ㅔ ', '들ㅇ', 'ㅓ갑니다']) -> '아버지가 방에 들어갑니다'
    assemble_hangul(['아버지가', ' ', '방에 ', '들어갑니다']) -> '아버지가 방에 들어갑니다'
    assemble_hangul(['ㅇ', 'ㅏ', 'ㅂ', 'ㅓ', 'ㅈ', 'ㅣ']) -> '아버지'
    """
    disassembled = disassemble_hangul("".join(words))
    return reduce(binary_assemble_hangul, disassembled)
