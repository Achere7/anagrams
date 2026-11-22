# Anagrams

A command-line program that finds the anagrams of a word in a list of English words.

Two words are anagrams if the letters of one, rearranged, spell the other (`tops` and `stop`). The program sorts the letters of both words and compares the results.

## Requirements

- Python 3 (the code uses f-strings, so 3.6 or later)
- `pytest`, only to run the tests

## Usage

```bash
python anagrams.py takes
```

Output:

```
skate
stake
steak
teaks
```

The search ignores upper and lower case, so `Takes` gives the same result.

To use a different word list (one word per line):

```bash
python anagrams.py takes --words my_list.txt
```

For help:

```bash
python anagrams.py --help
```

If no anagram is found, the program says so:

```
No anagrams of 'zzzzz' found in the list.
```

If the word list file does not exist, it shows a usage message and an error instead of a traceback:

```
anagrams.py: error: word list file not found: nope.txt
```

## Tests

```bash
pip install pytest
pytest
```

The tests cover the anagram check (including case and repeated letters), the search function, reading the word list from a file, and the command-line behaviour.

## Project structure

| File | Contents |
|---|---|
| `anagrams.py` | Logic (`is_anagram`, `find_anagrams`, `load_words`) and command-line interface |
| `test_anagrams.py` | Tests with pytest |
| `words.txt` | English word list |

## Design decisions

- **Logic is separate from input and output.** `find_anagrams` receives the word list as an argument instead of relying on a global variable, so it can be tested with small lists.
- **Functions return values, and only `main` prints.** This lets other code reuse `find_anagrams` to count, sort or filter the results.
- **The word itself is excluded from the results**, because it is a trivial anagram of itself.
- **Comparison is case-insensitive.** Both words are converted to lower case before their letters are sorted, and the exclusion of the word itself uses the same rule.
- **The default word list is found relative to the script**, so the program works from any directory.

## Limitations

- Accented letters are treated as different letters (`é` is not `e`).
- Spaces and punctuation count as characters, so the program is meant for single words.

## Data source

`words.txt` comes from the *Think Python* repository by Allen Downey: https://github.com/AllenDowney/ThinkPython
