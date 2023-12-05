def letter_percentages(input_string):
    """
    This function takes a string as input and returns a dictionary of letter frequencies as percentages.

    Args:
        input_string (str): A string to be analyzed.

    Returns:
        dict: A dictionary of letter frequencies as percentages.
    """
    letter_count = {}
    total_letters = sum([i.isalpha() for i in input_string])
    for i in input_string:
        if i.isalpha():
            if i in letter_count:
                letter_count[i] += 1
            else:
                letter_count[i] = 1
    for k, v in letter_count.items():
        letter_count[k] = round(v * 100 / total_letters, 2)
    return letter_count


def main():
    """Main Function"""
    letter_percentages("Hello world")


if __name__ == "__main__":
    main()
