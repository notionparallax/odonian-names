"""Trying to generate all the names that the computer could give an Odonian."""

import itertools

import pronouncing

# from english_words import get_english_words_set
from num2words import num2words
from syllables import estimate

# import cmudict

# ENGLISH_WORDS = get_english_words_set(["web2"], lower=True)


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
    word_length = 5
    the_name_filename = f"possible_names_{word_length}.txt"
    last_name_found = get_last_name(the_name_filename)

    name_generator = generate_combinations(alphabet, word_length)
    combinations_to_check = 700000000
    mark_every_n = 100000
    print(
        f"""
Generating the first {num2words(combinations_to_check)} letter combinations of {num2words(word_length)} letters, 
searching for two syllable words that are pronouncable in english.
The . dots show every {mark_every_n} names checked.
Started from the last name found: {last_name_found}"""
    )
    with open(the_name_filename, "a", encoding="utf-8") as f:
        for i in range(combinations_to_check):
            if i % mark_every_n == 0:
                print(".", end="")
            generated_name = next(name_generator)
            if generated_name > last_name_found:
                if is_two_sylable(generated_name):
                    f.write(
                        # ("📖 " if generated_name in ENGLISH_WORDS else "🔰 ")
                        generated_name
                        + "\n"
                    )


def get_last_name(the_name_filename):
    with open(the_name_filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        last_name_found = lines[-1].strip()
        if last_name_found == "":
            last_name_found = lines[-1].strip()
    return last_name_found


main()
