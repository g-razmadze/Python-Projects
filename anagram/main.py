def count_anagrams(input_str):
    """
    This function takes a string as input and returns the number of unique anagrams that can be formed from the characters in the string.

    Args:
        input_str (str): A string to be analyzed.

    Returns:
        int: The number of unique anagrams that can be formed from the characters in the input string.
    """
    stack = [(list(input_str), 0)]
    unique_anagrams = set()
    while stack:
        chars, i = stack.pop()
        if i == len(chars) - 1:
            unique_anagrams.add("".join(chars))
        else:
            for j in range(i, len(chars)):
                chars[i], chars[j] = chars[j], chars[i]
                stack.append((chars.copy(), i + 1))
                chars[i], chars[j] = chars[j], chars[i]
    return len(unique_anagrams)


def main():
    """Main Function"""
    count_anagrams("abc")


if __name__ == "__main__":
    main()
