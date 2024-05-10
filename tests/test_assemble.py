from hangul.assemble import assemble_hangul


def test_assemble_hangul_with_complete_and_incomplete_hangul():
    """
    온전한 한글과 한글 문자 조합
    """
    assert (
        assemble_hangul(["아버지가", " ", "방ㅇ", "ㅔ ", "들ㅇ", "ㅓ갑니다"])
        == "아버지가 방에 들어갑니다"
    )


def test_assemble_hangul_with_complete_hangul_only():
    """
    온전한 한글만 조합
    """
    assert (
        assemble_hangul(["아버지가", " ", "방에 ", "들어갑니다"])
        == "아버지가 방에 들어갑니다"
    )


def test_assemble_hangul_with_incomplete_hangul_only():
    """
    온전하지 않은 한글만 조합
    """
    assert assemble_hangul(["ㅇ", "ㅏ", "ㅂ", "ㅓ", "ㅈ", "ㅣ"]) == "아버지"
