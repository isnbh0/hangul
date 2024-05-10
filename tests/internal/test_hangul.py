import pytest

from hangul.internal.hangul import (
    binary_assemble_hangul,
    binary_assemble_hangul_characters,
    is_hangul_alphabet,
    is_hangul_character,
)


def test_is_hangul_character_returns_true_for_complete_hangul_characters():
    """isHangulCharacter는 완성된 한글 문자를 받으면 true를 반환한다."""
    assert is_hangul_character("가")
    assert is_hangul_character("값")
    assert not is_hangul_character("ㄱ")
    assert not is_hangul_character("ㅏ")
    assert not is_hangul_character("a")


def test_is_hangul_alphabet_returns_true_for_uncombined_hangul_characters():
    """isHangulAlphabet은 조합되지않은 한글 문자를 받으면 true를 반환한다."""
    assert not is_hangul_alphabet("가")
    assert not is_hangul_alphabet("값")
    assert is_hangul_alphabet("ㄱ")
    assert is_hangul_alphabet("ㅏ")
    assert not is_hangul_alphabet("a")


def test_binary_assemble_hangul_characters_combines_characters_correctly():
    """초성과 중성만 조합"""
    assert binary_assemble_hangul_characters("ㄱ", "ㅏ") == "가"
    assert binary_assemble_hangul_characters("가", "ㅇ") == "강"
    assert binary_assemble_hangul_characters("갑", "ㅅ") == "값"
    assert binary_assemble_hangul_characters("고", "ㅏ") == "과"
    assert binary_assemble_hangul_characters("ㅗ", "ㅏ") == "ㅘ"
    assert binary_assemble_hangul_characters("톳", "ㅡ") == "토스"
    assert binary_assemble_hangul_characters("닭", "ㅏ") == "달가"
    assert binary_assemble_hangul_characters("깎", "ㅏ") == "까까"
    assert binary_assemble_hangul_characters("ㅏ", "ㄱ") == "ㅏㄱ"
    assert binary_assemble_hangul_characters("까", "ㅃ") == "까ㅃ"
    assert binary_assemble_hangul_characters("ㅘ", "ㅏ") == "ㅘㅏ"
    assert binary_assemble_hangul_characters("뼈", "ㅣ") == "뼈ㅣ"


def test_binary_assemble_hangul_combines_sentences_with_characters():
    """문장과 모음을 조합하여 다음 글자를 생성한다."""
    assert (
        binary_assemble_hangul("저는 고양이를 좋아합닏", "ㅏ")
        == "저는 고양이를 좋아합니다"
    )
    assert (
        binary_assemble_hangul("저는 고양이를 좋아하", "ㅂ") == "저는 고양이를 좋아합"
    )
    assert (
        binary_assemble_hangul("저는 고양이를 좋아합", "ㅅ") == "저는 고양이를 좋아핪"
    )
    assert (
        binary_assemble_hangul("저는 고양이를 좋아합", "ㄲ") == "저는 고양이를 좋아합ㄲ"
    )
    assert (
        binary_assemble_hangul("저는 고양이를 좋아합", "ㅂ") == "저는 고양이를 좋아합ㅂ"
    )
    assert (
        binary_assemble_hangul("저는 고양이를 좋아하", "ㅏ") == "저는 고양이를 좋아하ㅏ"
    )
    assert (
        binary_assemble_hangul("저는 고양이를 좋아합니다", "ㅜ")
        == "저는 고양이를 좋아합니다ㅜ"
    )


def test_binary_assemble_hangul_raises_error_on_invalid_input():
    """소스가 두 글자 이상이라면 Invalid source 에러를 발생시킨다."""
    with pytest.raises(Exception) as excinfo:
        binary_assemble_hangul_characters("가나", "ㄴ")
    assert "Invalid source character: 가나. Source must be one character." in str(
        excinfo.value
    )

    with pytest.raises(Exception) as excinfo:
        binary_assemble_hangul_characters("ㄱㄴ", "ㅏ")
    assert "Invalid source character: ㄱㄴ. Source must be one character." in str(
        excinfo.value
    )

    with pytest.raises(Exception) as excinfo:
        binary_assemble_hangul_characters("ㄱ", "a")
    assert (
        "Invalid next character: a. Next character must be one of the chosung, jungsung, or jongsung."
        in str(excinfo.value)
    )

    with pytest.raises(Exception) as excinfo:
        binary_assemble_hangul_characters("ㄱ", "ㅡㅏ")
    assert (
        "Invalid next character: ㅡㅏ. Next character must be one of the chosung, jungsung, or jongsung."
        in str(excinfo.value)
    )
