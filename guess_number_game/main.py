"""Guess the Number!

   Author: Giorgi Razmadze
   Date: October 12, 2023

   This is one of my projects which I finished during my Python course by Reza Ghazi
"""

import random


# defining functions, constans and classes
def splash_screen(name_of_game):
    """
      Giving game a title

    """
    title = "\nWelcome to " + name_of_game
    print(f"{title}")
    print(f"{'─' * len(title)}")
    print()


def guessing_game(left_bound=1, right_bound=100, max_attempts=5):
    """
      Guessing a number.

      Args:
          left_bound=1: default integer of starting number.
          right_bound=100: default integer of ending number.
          max_attempts=5: number of tries.

      Return:
          None.


    """
    num_of_guess = random.randint(left_bound, right_bound)
    attempts = 0
    guess = None
    print(f"Guess a Number Between {left_bound} and {right_bound}.")
    print(f"You have {max_attempts} attempts.\n")
    while guess != num_of_guess:
        if attempts < max_attempts:
            try:
                guess = int(input("Enter your number: "))
                print()
                if guess < num_of_guess:
                    print(f"Too low!\n")
                elif guess > num_of_guess:
                    print(f"Too high!\n")
                attempts += 1
                print(f"{max_attempts - attempts} Attempts Left.\n")

            except ValueError:
                print(f"Invalid input please enter a number.")
        else:
            print(f"Sorry you have reached to the maximum number of attempt.\n")
            print(f"The chosen number was {num_of_guess}.\n")

            break
    if guess == num_of_guess:
        print(f"Congradulations! You won.\n")


def main():
    """Main Function"""
    splash_screen("Guess a Number Game")
    guessing_game()


if __name__ == "__main__":
    main()
