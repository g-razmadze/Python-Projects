def sort_alphanumerically():
    """
    This function prompts the user to enter a string of words, counts the frequency of each word, and prints the words and their frequency in alphabetical order.

    Returns:
        None
    """
    frequency = {}
    user = input("Please type your text: ").split()
    for word in user:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    sorted_frequency = dict(sorted(frequency.items()))
    for word, count in sorted_frequency.items():
        print(f"{word}:{count}")


def main():
    sort_alphanumerically()




if __name__ == "__main__":
    main()