import pytest

from hangul.combine_hangul_character import combine_hangul_character, combine_vowels


def test_combines_two_characters_into_double_final_consonant():
    """종성으로 겹받침으로 구성될 수 있는 문자 두 개를 받으면 겹받침을 생성한다. (ㄱ, ㅏ, ㅂㅅ)"""
    assert combine_hangul_character("ㄱ", "ㅏ", "ㅂㅅ") == "값"


def test_combines_without_final_if_no_final_given():
    """종성이 입력되지 않았다면 받침이 없는 문자로 합성한다. (ㅌ, ㅗ)"""
    assert combine_hangul_character("ㅌ", "ㅗ") == "토"


def test_adds_final_consonant_when_given():
    """종성이 입력되었다면 받침을 추가한다. (ㅌ, ㅗ, ㅅ)"""
    assert combine_hangul_character("ㅌ", "ㅗ", "ㅅ") == "톳"


def test_raises_error_for_invalid_initial():
    """초성이 될 수 없는 문자가 초성으로 입력되면 에러를 반환한다. (ㅏ, ㅏ, ㄱ)"""
    with pytest.raises(ValueError):
        combine_hangul_character("ㅏ", "ㅏ", "ㄱ")


def test_raises_error_for_invalid_vowel():
    """중성이 될 수 없는 문자가 중성으로 입력되면 에러를 반환한다. (ㄱ, ㄴ, ㅃ)"""
    with pytest.raises(ValueError):
        combine_hangul_character("ㄱ", "ㄴ", "ㅃ")


def test_raises_error_for_invalid_final():
    """종성이 될 수 없는 문자가 종성으로 입력되면 에러를 반환한다. (ㄱ, ㅏ, ㅃ)"""
    with pytest.raises(ValueError):
        combine_hangul_character("ㄱ", "ㅏ", "ㅃ")


def test_raises_error_if_full_hangul_character_given():
    """온전한 한글 문자가 하나라도 입력되면 에러를 반환한다. (가, ㅏ, ㄱ)"""
    with pytest.raises(ValueError):
        combine_hangul_character("가", "ㅏ", "ㄱ")


def test_creates_diphthong_if_possible():
    """겹모음이 될 수 있는 모음이 순서대로 입력되면 겹모음으로 합성한다."""
    assert combine_vowels("ㅗ", "ㅏ") == "ㅘ"
    assert combine_vowels("ㅜ", "ㅔ") == "ㅞ"
    assert combine_vowels("ㅡ", "ㅣ") == "ㅢ"


def test_joins_if_wrong_order():
    """겹모음이 될 수 있는 모음이라고 해도 틀린 순서로 입력되면 Join한다."""
    assert combine_vowels("ㅏ", "ㅗ") == "ㅏㅗ"
    assert combine_vowels("ㅣ", "ㅡ") == "ㅣㅡ"


def test_joins_if_already_a_diphthong():
    """이미 겹모음인 문자와 모음을 합성하려고 시도하면 Join한다."""
    assert combine_vowels("ㅘ", "ㅏ") == "ㅘㅏ"
    assert combine_vowels("ㅝ", "ㅣ") == "ㅝㅣ"
