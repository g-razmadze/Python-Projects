"""Countdown timer!

   Author: Giorgi Razmadze
   Date: October 24, 2023

   This is one of my projects
"""

# importing libraries
import time


# defining functions, constans and classes
def countdown(user: int) -> None:
    """Count down from a given number of seconds and print "Time completed" when done.

    Args:
        user (int): The number of seconds to count down from.

    Raises:
        ValueError: If user is not a positive integer.

    Return:
        None
    """
    while user:
            min , sec = divmod(user , 60)
            timer = f"{min:02d}:{sec:02d}"
            print(timer, end="\r")
            time.sleep(1)
            user -= 1 
    print("Time completed")
    
try:
    user = int(input("Enter the time in seconds: \n"))
    countdown(user)
except ValueError:
    print("Invalid input. Please enter a valid number of seconds.\n")
