from .disassemble_complete_hangul_character import disassemble_complete_hangul_character
from .utils import has_batchim

로_조사 = ["으로/로", "으로서/로서", "으로써/로써", "으로부터/로부터"]


def josa(word, josa_option):
    """
    조사를 올바르게 선택하여 단어에 붙여서 반환합니다.
    예시:
    josa('하늘', '이/가') -> '하늘이'
    josa('바다', '이/가') -> '바다가'
    """
    if len(word) == 0:
        return word

    return word + josa_picker(word, josa_option)


def josa_picker(word, josa_option):
    """
    주어진 단어와 조사 옵션에 따라 올바른 조사를 선택합니다.
    """
    if len(word) == 0:
        return josa_option.split("/")[0]

    has_받침 = has_batchim(word)
    index = 0 if has_받침 else 1

    last_character = word[-1]
    disassembled = disassemble_complete_hangul_character(last_character)
    is_종성_ㄹ = disassembled["last"] == "ㄹ" if disassembled else False

    is_case_of_로 = has_받침 and is_종성_ㄹ and josa_option in 로_조사

    if josa_option == "와/과" or is_case_of_로:
        index = 1 if index == 0 else 0

    is_ends_with_이 = last_character == "이"

    if josa_option == "이에요/예요" and is_ends_with_이:
        index = 1

    return josa_option.split("/")[index]
