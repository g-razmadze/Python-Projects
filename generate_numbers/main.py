def generate_list():
    """
    This function prompts the user to enter a series of numbers separated by spaces, underscores, or periods, and returns a list of the numbers.

    Returns:
        tuple: A tuple containing the list of numbers and the length of the list.
    """
    nums_list = []
    while True:
        user = input("Please enter your text: ").replace(" ", "")
        if user == "":
            break
        if user.count(".") == 1:
            if user.count("_") > 0:
                if "._" not in user and user[-1] != "_" and user[0] != "_" and user.replace("_", "").replace(".", "").isdigit():
                    nums_list.append(float(user))
            elif user.replace(".", "").isdigit():
                nums_list.append(float(user))
        elif user.count("_") > 0:
            if user.replace("_", "").isdigit():
                nums_list.append(int(user))
        elif user.isdigit():
            nums_list.append(int(user))
    return nums_list, len(nums_list)

def main():
    """Main Function"""
    generate_list()


if __name__ == "__main__":
    main()
