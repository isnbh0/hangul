from hangul.convert_qwerty_to_hangul_alphabet import (
    convert_qwerty_to_hangul,
    convert_qwerty_to_hangul_alphabet,
)


def test_convert_qwerty_to_hangul_alphabet_english_to_hangul_phoneme():
    """영어 알파벳을 한글 음소로 바꾼다."""
    assert convert_qwerty_to_hangul_alphabet("abc") == "ㅁㅠㅊ"


def test_convert_qwerty_to_hangul_alphabet_handle_double_jamo():
    """쌍/자모음에 대응하지 않는 영어 알파벳을 한글 음소로 바꾼다."""
    assert convert_qwerty_to_hangul_alphabet("ABC") == "ㅁㅠㅊ"


def test_convert_qwerty_to_hangul_alphabet_mixed_content():
    """영어 알파벳은 한글 음소로 바꾸고, 한글 음절은 유지한다."""
    assert convert_qwerty_to_hangul_alphabet("vm론트") == "ㅍㅡ론트"


def test_convert_qwerty_to_hangul_alphabet_preserves_decomposed_hangul():
    """분해된 한글 음소는 유지한다."""
    assert convert_qwerty_to_hangul_alphabet("ㅍㅡㄹㅗㄴㅌㅡ") == "ㅍㅡㄹㅗㄴㅌㅡ"


def test_convert_qwerty_to_hangul_alphabet_non_alphabet_characters():
    """영어 알파벳이 아닌 입력은 유지한다."""
    assert convert_qwerty_to_hangul_alphabet("4월/20dlf!") == "4월/20ㅇㅣㄹ!"


def test_convert_qwerty_to_hangul_alphabet_uppercase_to_double_jamo():
    """영문 대문자는 쌍자/모음으로 바꾼다."""
    assert convert_qwerty_to_hangul_alphabet("RㅏㄱEㅜrl") == "ㄲㅏㄱㄸㅜㄱㅣ"
    assert convert_qwerty_to_hangul_alphabet("ㅇPdml") == "ㅇㅖㅇㅡㅣ"


def test_convert_qwerty_to_hangul_alphabet_empty_string():
    """빈 문자열은 빈 문자열을 반환한다."""
    assert convert_qwerty_to_hangul_alphabet("") == ""


def test_convert_qwerty_to_hangul_combines_to_hangul():
    """영어 알파벳을 한글로 합성한다."""
    assert convert_qwerty_to_hangul("abc") == "뮻"
    assert convert_qwerty_to_hangul("vmfhsxmdpsem") == "프론트엔드"


def test_convert_qwerty_to_hangul_handle_uppercase():
    """쌍/자모음에 대응하지 않는 영어 알파벳을 한글로 합성한다."""
    assert convert_qwerty_to_hangul("ABC") == "뮻"
    assert convert_qwerty_to_hangul("VMFHSXM") == "프론트"


def test_convert_qwerty_to_hangul_preserves_hangul():
    """영어 알파벳은 한글로 합성하고, 한글 음절은 유지한다."""
    assert convert_qwerty_to_hangul("vm론트") == "프론트"


def test_convert_qwerty_to_hangul_combines_hangul_phonemes():
    """인자가 한글 음소면 한글로 합성한다."""
    assert convert_qwerty_to_hangul("ㅍㅡㄹㅗㄴㅌㅡ") == "프론트"


def test_convert_qwerty_to_hangul_uppercase_double_jamo():
    """영문 대문자는 쌍자/모음에 대응하며 한글로 합성한다."""
    assert convert_qwerty_to_hangul("RㅏㄱEㅜrl") == "깍뚜기"
    assert convert_qwerty_to_hangul("ㅇPdml") == "예의"


def test_convert_qwerty_to_hangul_returns_empty_for_empty_input():
    """빈 문자열은 빈 문자열을 반환한다."""
    assert convert_qwerty_to_hangul("") == ""
