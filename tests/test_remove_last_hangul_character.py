from hangul.remove_last_hangul_character import remove_last_hangul_character


def test_remove_last_hangul_character_double_to_single_final_consonant():
    """마지막 문자가 겹받침인 경우 홑받침으로 바꾼다."""
    assert remove_last_hangul_character("안녕하세요 값") == "안녕하세요 갑"


def test_remove_last_hangul_character_ending_with_initial_and_vowel():
    """마지막 문자가 초성과 중성의 조합으로 끝날 경우 초성만 남긴다."""
    assert remove_last_hangul_character("프론트엔드") == "프론트엔ㄷ"


def test_remove_last_hangul_character_ending_with_full_syllable():
    """마지막 문자가 초성과 중성과 종성의 조합으로 끝날 경우 초성과 중성이 조합된 문자만 남긴다."""
    assert remove_last_hangul_character("일요일") == "일요이"
    assert remove_last_hangul_character("깎") == "까"


def test_remove_last_hangul_character_empty_string_returns_empty():
    """빈 문자열일 경우 빈 문자열을 반환한다."""
    assert remove_last_hangul_character("") == ""
