import time
import random

def timer(func):
    """
    This function takes a function as input and returns a new function that times the execution of the input function.

    Args:
        func (function): A function to be timed.

    Returns:
        function: A new function that times the execution of the input function.
    """
    def wrapper(*args, **kwargs):
        before = time.monotonic()
        retval = func(*args, **kwargs)
        after = time.monotonic() - before
        print(f"Function {func.__name__}: {after:05f} seconds")
        return retval

    return wrapper


@timer
def bubble(lst):
    """
    This function takes a list as input and returns the number of iterations required to sort the list using bubble sort.

    Args:
        lst (list): A list of integers to be sorted.

    Returns:
        int: The number of iterations required to sort the list.
    """
    loops = 0
    n = len(lst)

    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if lst[j] > lst[j + 1]:
                loops += 1
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return loops


lst = list(range(1, 25 * 507))
random.shuffle(lst)

iterations = bubble(lst)
print("Total iterations:", iterations)