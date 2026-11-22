"""Search for anagrams of a word in a word list.

By default, it uses a complete English word list (words.txt).

Usage:
    python anagrams.py takes
    python anagrams.py takes --words my_list.txt
"""



# Standard library: argparse reads command-line arguments,
# Path builds file paths that work on any operating system.
import argparse
from pathlib import Path

# Path to words.txt, located in the same folder as this script, so the
# program finds it no matter which directory it is run from.
DEFAULT_WORDS_FILE = Path(__file__).with_name("words.txt")


def is_anagram(word1, word2):
    """Check if two words are anagrams, ignoring case.

    >>> is_anagram('tops', 'stop')
    True
    >>> is_anagram('Tops', 'stop')
    True
    >>> is_anagram('tops', 'takes')
    False
    """
    return sorted(word1.lower()) == sorted(word2.lower())


def load_words(path):
    """Read a text file (one word per line) and return a list of words."""
    file = open(path, encoding="utf-8")
    content = file.read()
    file.close()
    return content.split()


def find_anagrams(word1, word_list):
    """Return the words in word_list that are anagrams of word1.

    The word itself is excluded.
    """
    anagrams = []
    for word in word_list:
        if word.lower() != word1.lower() and is_anagram(word1, word):
            anagrams.append(word)
    return anagrams


def main(argv=None):
    """Parse command-line arguments and print the anagrams found."""
    parser = argparse.ArgumentParser(description="Find anagrams of a word.")
    parser.add_argument("word", help="word to find anagrams of")
    parser.add_argument(
        "--words",
        default=DEFAULT_WORDS_FILE,
        help="file with one word per line (default: words.txt)",
    )
    args = parser.parse_args(argv)

    try:
        word_list = load_words(args.words)
    except FileNotFoundError:
        parser.error(f"word list file not found: {args.words}")

    anagrams = find_anagrams(args.word, word_list)
    if anagrams:
        print("\n".join(anagrams))
    else:
        print(f"No anagrams of '{args.word}' found in the list.")


if __name__ == "__main__":
    main()
