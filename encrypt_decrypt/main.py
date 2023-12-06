alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    """
    This function takes a string and an integer as input and returns the encoded text by shifting each letter in the string by the specified amount.

    Args:
        plain_text (str): A string to be encoded.
        shift_amount (int): An integer specifying the amount of shift.

    Returns:
        None
    """
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position > 25:
            new_position2 = new_position - 26
            new_letter2 = alphabet[new_position2]
            cipher_text += new_letter2
        else:
            new_letter1 = alphabet[new_position]
            cipher_text += new_letter1
    print(f"The encoded text is {cipher_text}.")



def decrypt(cipher_text, shift_amount):
    """
    This function takes a string and an integer as input and returns the decoded text by shifting each letter in the string by the specified amount.

    Args:
        cipher_text (str): A string to be decoded.
        shift_amount (int): An integer specifying the amount of shift.

    Returns:
        None
    """
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")



def main():
    encrypt(plain_text=text, shift_amount=shift)

    decrypt("mjqqt", 5)




if __name__ == "__main__":
    main()
