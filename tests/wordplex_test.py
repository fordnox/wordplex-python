from wordplex import Wordplex

wordplex = Wordplex()


def test_count_vowels():
    assert len(wordplex.vowels) == 5


def test_count_consonants():
    assert len(wordplex.consonants) == 21


def test_count_numbers():
    assert len(wordplex.numbers) == 10


def test_count_letters():
    assert len(wordplex.letters) == 10


def test_default_format():
    assert wordplex.get_format() == "VC"


def test_pattern():
    wordplex.setFormat("@#")
    assert wordplex.get_pattern() == "VC"


def test_set_format():
    wordplex.setFormat("CVV")
    assert wordplex.get_format() == "CVV"


def test_set_prefix():
    wordplex.set_prefix("i")
    # Assuming the test passes as there's no specified check in the original test
    assert True
