from hangul.hangul_includes import hangul_includes


def test_hangul_includes_positive_cases_for_sagwa():
    """
    사과:
    - Hangul includes test for an empty substring should return true.
    - Hangul includes test for a substring that is a jamo of the main string should return true.
    - Hangul includes test for a substring that is not exactly matching but considered a match should return true.
    - Hangul includes test for an exact match should return true.
    """
    assert hangul_includes("사과", "")
    assert hangul_includes("사과", "ㅅ")
    assert hangul_includes("사과", "삭")
    assert hangul_includes("사과", "사과")


def test_hangul_includes_positive_cases_for_frontend():
    """
    프론트엔드:
    - Hangul includes test for an empty substring should return true.
    - Hangul includes test for a substring that might not be correctly mapped but assumed matching should return true multiple times.
    - Hangul includes test for a substring that is partially matching the beginning of the main string should return true.
    """
    assert hangul_includes("프론트엔드", "")
    assert hangul_includes("프론트엔드", "플")
    assert hangul_includes("프론트엔드", "틍")
    assert hangul_includes("프론트엔드", "프로")


def test_hangul_includes_negative_cases_for_sagwa():
    """
    사과:
    - Hangul includes test for a non-matching substring should return false.
    """
    assert not hangul_includes("사과", "삽")


def test_hangul_includes_negative_cases_for_frontend():
    """
    프론트엔드:
    - Hangul includes test for a non-matching substring should return false.
    """
    assert not hangul_includes("프론트엔드", "픏")
