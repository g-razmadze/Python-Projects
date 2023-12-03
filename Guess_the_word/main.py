import random
from words import words
import string


def valid_word(word_list):
    # randomly choosing different words from words list
    word = random.choice(word_list)
    while "-" in word or " " in word:
        word = random.choice(word_list)
    return word.upper()


def guess_the_word():
    word = valid_word(words)
    word_letter = set(word)  # characters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what we already guessed

    while len(word_letter) > 0:
        # join(['a', 's', 'b']) -> "a s b"
        print("You have used these letters:", " ".join(used_letters))

        # Current word status
        word_list = [
            letter if letter in used_letters else "-" for letter in word]
        print("Current Word: ", " ".join(word_list))

        user_input = input("Type a letter: ").upper()  # user input
        if user_input in alphabet - used_letters:
            used_letters.add(user_input)

            if user_input in word_letter:
                word_letter.remove(user_input)

        elif user_input in used_letters:
            print("You have already used that character. Try another.")
        else:
            print("Invalid character. Try again")

    if len(word_letter) == 0:
        print("Wow! You guessed the word:", word)


if __name__ == "__main__":
    guess_the_word()
