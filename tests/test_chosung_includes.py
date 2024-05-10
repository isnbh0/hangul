import pytest

from hangul.chosung_includes import chosung_includes


@pytest.mark.parametrize(
    "word, chosung, expected",
    [
        ("프론트엔드", "ㅍㄹㅌ", True),
        ("00프론트엔드", "ㅍㄹㅌ", True),
        ("프론트엔드 개발자", "ㅍㄹㅌㅇㄷㄱㅂㅈ", True),
        ("프론트엔드 개발자", "ㅍㄹㅌㅇㄷ ㄱㅂㅈ", True),
    ],
)
def test_chosung_includes_positive(word, chosung, expected):
    """
    초성이 포함되어있다고 판단되는 경우:
    - "ㅍㄹㅌ" 문자열로 "프론트엔드"를 검색하면 true를 반환한다.
    - "ㅍㄹㅌ" 문자열로 "00프론트엔드"를 검색하면 true를 반환한다.
    - "ㅍㄹㅌㅇㄷㄱㅂㅈ" 문자열로 "프론트엔드 개발자"를 검색하면 true를 반환한다.
    - "ㅍㄹㅌㅇㄷ ㄱㅂㅈ" 문자열로 "프론트엔드 개발자"를 검색하면 true를 반환한다.
    """
    assert chosung_includes(word, chosung) == expected


@pytest.mark.parametrize(
    "word, chosung, expected",
    [
        ("프론트엔드", "ㅍㅌ", False),
        ("프론트엔드 개발자", " ", False),
        ("프론트엔드", "푸롴트", False),
    ],
)
def test_chosung_includes_negative(word, chosung, expected):
    """
    초성이 포함되어있다고 판단되지 않는 경우:
    - "ㅍㅌ" 문자열로 "프론트엔드"를 검색하면 false를 반환한다.
    - 빈 문자열로 "프론트엔드 개발자"를 검색하면 false를 반환한다.
    - "푸롴트" 문자열로 "프론트엔드"를 검색하면 초성으로만 구성되어 있지 않아 false를 반환한다.
    """
    assert chosung_includes(word, chosung) == expected
