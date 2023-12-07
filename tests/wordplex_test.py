from wordplex import WordPlex

wp = WordPlex()


def test_count_vowels():
    assert len(wp.vowels) == 6


def test_count_consonants():
    assert len(wp.consonants) == 20


def test_count_numbers():
    assert len(wp.numbers) == 10


def test_count_letters():
    assert len(wp.letters) == 26


def test_default_format():
    assert wp.get_format() == "VC"


def test_pattern():
    wp.set_format("@")
    assert wp.get_pattern() == [wp.letters]

    wp.set_format("#")
    assert wp.get_pattern() == [wp.numbers]

    wp.set_format("C")
    assert wp.get_pattern() == [wp.consonants]

    wp.set_format("V")
    assert wp.get_pattern() == [wp.vowels]

    wp.set_format("VC")
    assert wp.get_pattern() == [wp.vowels, wp.consonants]


def test_set_format():
    wp.set_format("CVV")
    assert wp.get_format() == "CVV"

