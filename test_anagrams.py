import pytest

from anagrams import find_anagrams, is_anagram, load_words, main


@pytest.mark.parametrize(
    "word1, word2, expected",
    [
        ("tops", "stop", True),
        ("skate", "takes", True),
        ("tops", "takes", False),
        ("skate", "stop", False),
        ("", "", True),
        ("Tops", "stop", True),  # capital first letter
        ("TOPS", "stop", True),  # all caps
        ("aab", "abb", False),  # same letters but different position

    ],
)
def test_is_anagram(word1, word2, expected):
    assert is_anagram(word1, word2) is expected


def test_find_anagrams_returns_list_without_the_word_itself():
    words = ["takes", "skate", "stake", "steak", "stop"]
    assert find_anagrams("takes", words) == ["skate", "stake", "steak"]


def test_find_anagrams_no_matches_returns_empty_list():
    assert find_anagrams("xyz", ["abc", "def"]) == []


def test_load_words(tmp_path):
    file = tmp_path / "words.txt"
    file.write_text("tops\nstop\nskate\n", encoding="utf-8")
    assert load_words(file) == ["tops", "stop", "skate"]


def test_main_prints_anagrams(tmp_path, capsys):
    file = tmp_path / "words.txt"
    file.write_text("tops\nstop\nposts\n", encoding="utf-8")
    main(["tops", "--words", str(file)])
    assert capsys.readouterr().out.strip() == "stop"


def test_main_without_matches(tmp_path, capsys):
    file = tmp_path / "words.txt"
    file.write_text("abc\n", encoding="utf-8")
    main(["xyz", "--words", str(file)])
    assert "No anagrams" in capsys.readouterr().out


def test_main_missing_file_exits_with_error(capsys):
    with pytest.raises(SystemExit):
        main(["tops", "--words", "missing.txt"])
    assert "not found" in capsys.readouterr().err


def test_find_anagrams_ignores_case_and_excludes_the_word_itself():
    words = ["takes", "skate", "Steak"]
    assert find_anagrams("Takes", words) == ["skate", "Steak"]