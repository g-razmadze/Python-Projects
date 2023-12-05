def all_perms(elements):
    """
    This function takes a list as input and returns a list of all possible permutations of the elements in the list.

    Args:
        elements (list): A list of elements to be permuted.

    Returns:
        list: A list of all possible permutations of the elements in the input list.
    """
    if len(elements) <= 1:
        return elements
    else:
        tmp = []
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                tmp.append(perm[:i] + elements[0:1] + perm[i:])
        return tmp

def main():
    all_perms("abcde")



if __name__ == "__main__":
    main()
