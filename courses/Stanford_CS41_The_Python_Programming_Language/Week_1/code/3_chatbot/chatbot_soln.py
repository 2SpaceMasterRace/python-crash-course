"""
File: dictionary_chatbot.py
---------------------------

Checks if words are in the dictionary.
"""

WORDS_FILE = 'words.txt'
DEFINITIONS_FILE = 'definitions.txt'


def is_word(guess):
    with open(WORDS_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if line == guess:
                return True
    return False


def get_definition(guess):
    with open(DEFINITIONS_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            colon_idx = line.find(':')

            word = line[:colon_idx]
            meaning = line[colon_idx + 1:]

            if guess == word:
                return meaning


def main():
    """
    A chatbot which repeatedly prompts the user for a word and checks if it's in
    the dictionary.
    """
    print("Hi! My name is Parth, your friendly dictionary chatbot.")
    print("Enter a word and I'll tell you if it's in the dictionary.")

    while True:
        word = input("> ")
        word = word.lower()
        word = word.strip(' ?!')

        # conditionally, breaking out of the loop
        if word == '':
            break

        # doing something with that input
        if is_word(word):
            definition = get_definition(word)
            print(f"Yes! {word} is a word! The definition is: {definition}.")
        else:
            print(f"No! {word} is not a word.")


if __name__ == '__main__':
    main()
