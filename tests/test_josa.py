from hangul.josa import josa


def test_josa_nominative_case():
    """주격조사"""
    assert josa("샴푸", "이/가") == "샴푸가"
    assert josa("칫솔", "이/가") == "칫솔이"


def test_josa_accusative_case():
    """목적격조사"""
    assert josa("샴푸", "을/를") == "샴푸를"
    assert josa("칫솔", "을/를") == "칫솔을"


def test_josa_contrastive_particle():
    """대조의 보조사"""
    assert josa("샴푸", "은/는") == "샴푸는"
    assert josa("칫솔", "은/는") == "칫솔은"


def test_josa_directional_particle():
    """방향의 격조사"""
    assert josa("바깥", "으로/로") == "바깥으로"
    assert josa("내부", "으로/로") == "내부로"


def test_josa_directional_particle_with_final_consonant_exception():
    """방향의 격조사 ㄹ 받침 예외 처리"""
    assert josa("지름길", "으로/로") == "지름길로"


def test_josa_comparative_particle():
    """비교의 격조사"""
    assert josa("샴푸", "와/과") == "샴푸와"
    assert josa("칫솔", "와/과") == "칫솔과"


def test_josa_choice_particle():
    """선택의 보조사"""
    assert josa("샴푸", "이나/나") == "샴푸나"
    assert josa("칫솔", "이나/나") == "칫솔이나"


def test_josa_topic_particle():
    """화제의 보조사"""
    assert josa("샴푸", "이란/란") == "샴푸란"
    assert josa("칫솔", "이란/란") == "칫솔이란"


def test_josa_vocative_particle():
    """호격조사"""
    assert josa("철수", "아/야") == "철수야"
    assert josa("길동", "아/야") == "길동아"


def test_josa_connective_particle():
    """접속조사"""
    assert josa("고기", "이랑/랑") == "고기랑"
    assert josa("과일", "이랑/랑") == "과일이랑"


def test_josa_predicative_particle_and_conclusive_suffix():
    """서술격조사와 종결어미"""
    assert josa("사과", "이에요/예요") == "사과예요"
    assert josa("책", "이에요/예요") == "책이에요"


def test_josa_predicative_particle_and_conclusive_suffix_with_ending_e_exception():
    """서술격조사와 종결어미, "이" 로 끝나는 단어 예외 처리"""
    assert josa("때밀이", "이에요/예요") == "때밀이예요"


def test_josa_positional_particle():
    """지위나 신분 또는 자격을 나타내는 위격조사"""
    assert josa("학생", "으로서/로서") == "학생으로서"
    assert josa("부모", "으로서/로서") == "부모로서"


def test_josa_positional_particle_with_final_consonant_exception():
    """지위나 신분 또는 자격을 나타내는 위격조사 ㄹ 받침 예외 처리"""
    assert josa("라이벌", "으로서/로서") == "라이벌로서"


def test_josa_instrumental_particle():
    """수단의 의미를 나타내는 도구격조사"""
    assert josa("토큰", "으로써/로써") == "토큰으로써"
    assert josa("함수", "으로써/로써") == "함수로써"


def test_josa_instrumental_particle_with_final_consonant_exception():
    """수단의 의미를 나타내는 도구격조사 ㄹ 받침 예외 처리"""
    assert josa("건물", "으로써/로써") == "건물로써"


def test_josa_origin_particle():
    """어떤 행동의 출발점이나 비롯되는 대상임을 나타내는 격 조사"""
    assert josa("역삼동", "으로부터/로부터") == "역삼동으로부터"
    assert josa("저기", "으로부터/로부터") == "저기로부터"


def test_josa_origin_particle_with_final_consonant_exception():
    """어떤 행동의 출발점이나 비롯되는 대상임을 나타내는 격 조사 ㄹ 받침 예외 처리"""
    assert josa("동굴", "으로부터/로부터") == "동굴로부터"


def test_josa_returns_empty_for_empty_input():
    """단어가 빈 문자열일 경우 빈 문자열을 반환한다."""
    assert josa("", "이/가") == ""
