def is_isogram(word):
    """
    This function takes a string as input and returns True if the string is an isogram, False otherwise.

    Args:
        word (str): A string to be analyzed.

    Returns:
        bool: True if the input string is an isogram, False otherwise.
    """
    word_text = word.lower()
    lst = []
    for i in word_text:
        if i in lst:
            return False
        lst.append(i)
    return True


def main():
    """Main Function"""
    is_isogram("Hello")


if __name__ == "__main__":
    main()
