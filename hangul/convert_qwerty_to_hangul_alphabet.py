from .assemble import assemble_hangul
from .constants import QWERTY_KEYBOARD_MAP


def convert_qwerty_to_hangul_alphabet(word):
    """
    영어 알파벳을 qwerty 자판과 매칭되는 한글 음소로 변환합니다.
    param word: 한글 음소로 변환하고자 하는 영문
    returns: 영어 알파벳이 포함되지 않은 한글 음소, 음절, 기타 문자로 이루어진 문자열
    """
    return "".join(
        QWERTY_KEYBOARD_MAP.get(input_text, input_text) for input_text in word
    )


def convert_qwerty_to_hangul(word):
    """
    영어 알파벳을 qwerty 자판과 매칭과는 한글 문자와 문장으로 변환합니다.
    param word: 한글 문장으로 변환하고자 하는 영문
    returns: qwerty 영어 알파벳을 변환하여 한글 규칙에 맞게 합성한 문자열
    """
    if not word:
        return ""
    return assemble_hangul(list(convert_qwerty_to_hangul_alphabet(word)))
