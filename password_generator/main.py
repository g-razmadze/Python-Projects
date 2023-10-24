"""Password Generator!

   Author: Giorgi Razmadze & 
   Date: October 19, 2023

   This is one of my projects
"""

# importing libraries
import random
import string
import secrets


# defining functions, constans and classes
class SecurePasswordGenerator:
    """
        A class that generates a secure password based on the user's specifications.

        Args:
            length: The length of the password.
            type length: int
            lower: The number of lowercase letters in the password.
            type lower: int
            upper: The number of uppercase letters in the password.
            type upper: int
            digits: The number of digits in the password.
            type digits: int
            special: The number of special characters in the password.
            type special: int 

        Return:
            A secure password that meets the user's requirements.
            rtype: str

    """

    def __init__(self, length, lower, upper, digits, special):
        self.length = length
        self.lower = lower
        self.upper = upper
        self.digits = digits
        self.special = special

    def gen_pass(self):
        lower_letters = string.ascii_lowercase
        upper_letters = string.ascii_uppercase
        num_digits = string.digits
        special_char = string.punctuation

        num_special = self.length - (self.lower + self.upper + self.digits)

        # if num_special < self.special:
        #     print("Warning! Not enough characters for special characters.")
        #     return None

        password_chars = (
            [secrets.choice(lower_letters) for _ in range(self.lower)] +
            [secrets.choice(upper_letters) for _ in range(self.upper)] +
            [secrets.choice(num_digits) for _ in range(self.digits)] +
            [secrets.choice(special_char) for _ in range(num_special)])

        random.shuffle(password_chars)
        password = ''.join(password_chars)

        return password


def password_generator():
    min_length = 8
    while True:
        try:
            rem = False
            up = dig = spec = 0
            while True:
                length = int(input("Enter password length: \n"))
                if length < min_length:
                    print("Warning! Password must be 8+ characters in length.\n")
                else:
                    break

            while True:
                lower = int(
                    input("Enter how many lowercase letters you want: \n"))
                if 0 <= lower <= length:
                    remaining = length - lower
                    if remaining == 0:
                        rem = True
                        up = dig = spec = 0
                        break
                    print(f"You still have {remaining} characters left.\n")
                    break
                else:
                    print(
                        f"Invalid input. Please enter number between 0 to {length}.\n")
            if rem:
                break

            while True:
                upper = int(
                    input("Enter how many uppercase letters you want: \n"))
                up = upper
                if 0 <= upper <= remaining:
                    remaining -= upper
                    if remaining == 0:
                        rem = True
                        dig = spec = 0
                        break
                    print(f"You still have {remaining} characters left.\n")
                    break
                else:
                    print(
                        f"Invalid input. Please enter number between 0 to {remaining}.\n")
            if rem:
                break

            while True:
                digits = int(input("Enter how many digits you want: \n"))
                dig = digits
                if 0 <= digits <= remaining:
                    remaining -= digits
                    if remaining == 0:
                        rem = True
                        spec = 0
                        break
                    break
                else:
                    print(
                        f"Invalid input. Please enter number between 0 to {remaining}.\n")
            if rem:
                break

            special = length - remaining
            spec = special
            break

        except ValueError:
            print("Invalid input. Please enter valid numeric values.\n")

    passw = SecurePasswordGenerator(length, lower, up, dig, spec)
    password = passw.gen_pass()

    if password:
        print(f"Generated Password: {password}")


def main():
    """Main Function"""
    password_generator()


if __name__ == "__main__":
    main()
