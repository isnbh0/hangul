from hangul.utils import (
    can_be_chosung,
    can_be_jongsung,
    can_be_jungsung,
    get_chosung,
    get_first_consonants,
    has_batchim,
    has_single_batchim,
)


def test_has_batchim_when_batchim_is_present():
    """
    받침이 있다고 판단되는 경우:
    - "값" 문자에서 받침이 있으므로 true를 반환한다.
    - "공" 문자에서 받침이 있으므로 true를 반환한다.
    - "읊" 문자에서 받침이 있으므로 true를 반환한다.
    """
    assert has_batchim("값")
    assert has_batchim("공")
    assert has_batchim("읊")


def test_has_batchim_when_no_batchim_is_present():
    """
    받침이 없다고 판단되는 경우:
    - "토" 문자에서 받침이 없으므로 false를 반환한다.
    - "서" 문자에서 받침이 없으므로 false를 반환한다.
    """
    assert not has_batchim("토")
    assert not has_batchim("서")


def test_has_single_batchim_when_single_batchim_is_present():
    """
    홑받침을 받으면 true를 반환한다:
    - "공" 문자에서 홑받침이 있으므로 true를 반환한다.
    - "핫" 문자에서 홑받침이 있으므로 true를 반환한다.
    - "양" 문자에서 홑받침이 있으므로 true를 반환한다.
    - "신" 문자에서 홑받침이 있으므로 true를 반환한다.
    """
    assert has_single_batchim("공")
    assert has_single_batchim("핫")
    assert has_single_batchim("양")
    assert has_single_batchim("신")


def test_has_single_batchim_when_not_single_batchim():
    """
    홑받침이 아니라고 판단되는 경우:
    - 겹받침을 받으면 false를 반환한다.
    - 받침이 없는 문자를 받으면 false를 반환한다.
    """
    assert not has_single_batchim("값")
    assert not has_single_batchim("읊")
    assert not has_single_batchim("토")
    assert not has_single_batchim("서")


def test_get_chosung_extract_initials():
    """
    - "사과" 단어에서 초성 "ㅅㄱ"을 추출한다.
    - "프론트엔드" 단어에서 초성 "ㅍㄹㅌㅇㄷ"을 추출한다.
    - "ㄴㅈ" 문자에서 초성 "ㄴㅈ"을 추출한다.
    - "리액트" 단어에서 초성 "ㄹㅇㅌ"을 추출한다.
    - "띄어 쓰기" 문장에서 초성 "ㄸㅇ ㅆㄱ"을 추출한다.
    """
    assert get_chosung("사과") == "ㅅㄱ"
    assert get_chosung("프론트엔드") == "ㅍㄹㅌㅇㄷ"
    assert get_chosung("ㄴㅈ") == "ㄴㅈ"
    assert get_chosung("리액트") == "ㄹㅇㅌ"
    assert get_chosung("띄어 쓰기") == "ㄸㅇ ㅆㄱ"


def test_get_first_consonants_sagwa():
    """'사과' 단어에서 초성 'ㅅㄱ'을 추출한다."""
    assert get_first_consonants("사과") == "ㅅㄱ"


def test_get_first_consonants_frontend():
    """'프론트엔드' 단어에서 초성 'ㅍㄹㅌㅇㄷ'을 추출한다."""
    assert get_first_consonants("프론트엔드") == "ㅍㄹㅌㅇㄷ"


def test_get_first_consonants_double_consonants():
    """'ㄴㅈ' 문자에서 초성 'ㄴㅈ'을 추출한다."""
    assert get_first_consonants("ㄴㅈ") == "ㄴㅈ"


def test_get_first_consonants_react():
    """'리액트' 단어에서 초성 'ㄹㅇㅌ'을 추출한다."""
    assert get_first_consonants("리액트") == "ㄹㅇㅌ"


def test_get_first_consonants_spacing():
    """'띄어 쓰기' 문장에서 초성 'ㄸㅇ ㅆㄱ'을 추출된다."""
    assert get_first_consonants("띄어 쓰기") == "ㄸㅇ ㅆㄱ"


def test_can_be_chosung_valid_cases():
    """초성이 될 수 있다고 판단되는 경우: ㄱ and ㅃ"""
    assert can_be_chosung("ㄱ")
    assert can_be_chosung("ㅃ")


def test_can_be_chosung_invalid_cases():
    """
    초성이 될 수 없다고 판단되는 경우:
    - ㅏ should be false
    - ㅘ should be false
    - ㄱㅅ should be false
    - 가 should be false
    """
    assert not can_be_chosung("ㅏ")
    assert not can_be_chosung("ㅘ")
    assert not can_be_chosung("ㄱㅅ")
    assert not can_be_chosung("가")


def test_can_be_jungsung_valid_cases():
    """중성이 될 수 있다고 판단되는 경우: ㅗㅏ and ㅏ"""
    assert can_be_jungsung("ㅗㅏ")
    assert can_be_jungsung("ㅏ")


def test_can_be_jungsung_invalid_cases():
    """
    중성이 될 수 없다고 판단되는 경우:
    - ㄱ should be false
    - ㄱㅅ should be false
    - 가 should be false
    """
    assert not can_be_jungsung("ㄱ")
    assert not can_be_jungsung("ㄱㅅ")
    assert not can_be_jungsung("가")


def test_can_be_jongsung_valid_cases():
    """종성이 될 수 있다고 판단되는 경우: ㄱ, ㄱㅅ, and ㅂㅅ"""
    assert can_be_jongsung("ㄱ")
    assert can_be_jongsung("ㄱㅅ")
    assert can_be_jongsung("ㅂㅅ")


def test_can_be_jongsung_invalid_cases():
    """
    종성이 될 수 없다고 판단되는 경우:
    - ㅎㄹ should be false
    - ㅗㅏ should be false
    - ㅏ should be false
    - 가 should be false
    """
    assert not can_be_jongsung("ㅎㄹ")
    assert not can_be_jongsung("ㅗㅏ")
    assert not can_be_jongsung("ㅏ")
    assert not can_be_jongsung("가")
