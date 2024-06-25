"""Trying to generate all the names that the computer could give an Odonian."""

import itertools

# import cmudict
import pronouncing
from syllables import estimate


def generate_combinations(letters, word_length):
    """Generate all possible combinations of letters of a given word length."""
    for p in itertools.product(letters, repeat=word_length):
        yield "".join(p)


def is_two_sylable(word):
    """Check if a word is two syllables."""
    rough = estimate(word)
    if 1 <= rough <= 3:
        pronunciation_list = pronouncing.phones_for_word(word)
        if not pronunciation_list:
            return False
        accurate_count = pronouncing.syllable_count(pronunciation_list[0])
        if accurate_count == 2:
            return True
    return False


def main():
    """Generate all possible combinations of letters of a given word length."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    word_length = 6
    name_generator = generate_combinations(alphabet, word_length)
    for i in range(100000):
        generated_name = next(name_generator)
        if is_two_sylable(generated_name):
            print(generated_name)


main()
