import string
from typing import List, Optional, Callable, Union


class WordPlex:
    def __init__(self):
        self.consonants = [
            "b",
            "c",
            "d",
            "f",
            "g",
            "h",
            "j",
            "k",
            "l",
            "m",
            "n",
            "p",
            "q",
            "r",
            "s",
            "t",
            "v",
            "x",
            "z",
            "w",
        ]
        self.vowels = ["a", "e", "i", "y", "o", "u"]
        self.letters = list(string.ascii_lowercase)
        self.numbers = list(range(10))
        self._format = "VC"
        self._suffix = ""
        self._prefix = ""
        self.alphabet_symbol = "@"

    def reset(self):
        self.set_suffix("")
        self.set_prefix("")
        self.set_format("VC")

    def set_prefix(self, p: str) -> None:
        self._prefix = p

    def set_suffix(self, s: str) -> None:
        self._suffix = s

    def set_format(self, pattern: Optional[str]) -> None:
        if not pattern:
            return
        self._format = str(pattern)

    def set_format_by_word(self, word: Optional[str]) -> None:
        if word is None:
            self.set_format("")
            return

        new_format = ""
        for a in word:
            if self.is_positive_integer(a):
                new_format += "#"
            elif a.lower() == self.alphabet_symbol:
                new_format += self.alphabet_symbol
            elif a.lower() in self.vowels:
                new_format += "V"
            elif a.lower() in self.consonants:
                new_format += "C"
        self.set_format(new_format)

    def get_format(self) -> str:
        return self._format

    def similar(self, word: Optional[str] = None, cb: Optional[Callable[[str], None]] = None) -> List[str]:
        self.set_format_by_word(word)
        return self.go(cb)

    def generate(self, pattern: Optional[str] = None, cb: Optional[Callable[[str], None]] = None) -> List[str]:
        self.set_format(pattern)
        return self.go(cb)

    def go(self, cb: Optional[Callable[[str], None]]) -> List[str]:
        if self._format == "":
            return []

        pattern = self.get_pattern()
        return self.fill_position(pattern, 0, len(pattern), "", [], cb)

    def get_pattern(self) -> List[List[Union[str, int]]]:
        pattern = []
        for letter in self._format:
            if letter == "C":
                pattern.append(self.consonants)
            elif letter == "V":
                pattern.append(self.vowels)
            elif letter == "#":
                pattern.append(self.numbers)
            elif letter == self.alphabet_symbol:
                pattern.append(self.letters)
            else:
                pattern.append([letter])
        return pattern

    def fill_position(self, pattern: List[List[Union[str, int]]], position: int, length: int, partial: str, result: List[str], cb: Optional[Callable[[str], None]] = None) -> List[str]:
        if length == 0:
            return result
        if position == length - 1:
            for character in pattern[position]:
                word = self._prefix + partial + str(character) + self._suffix
                if callable(cb):
                    cb(word)
                else:
                    result.append(word)
        else:
            for character in pattern[position]:
                self.fill_position(
                    pattern, position + 1, length, partial + str(character), result, cb
                )
        return result

    @staticmethod
    def is_positive_integer(n: Union[str, int]) -> bool:
        try:
            return int(n) >= 0
        except ValueError:
            return False
