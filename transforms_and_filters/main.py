from typing import List, Tuple

def transform_filter_tuples(input_list: List[Tuple[int, ...]]) -> List[Tuple[int, ...]]:
    """
    Transforms and filters a list of tuples based on specified criteria.

    Each integer in the tuples is squared if it is odd, and halved if it is even.
    Only tuples whose transformed elements sum to more than 50 are returned.

    Args:
        input_list: A list of tuples containing integers.

    Returns:
        A filtered list of tuples after applying the transformations.
    """
    # Apply the correct transformation to each element in each tuple
    transformed = [(tuple(x**2 if x % 2 else int(x / 2) for x in t)) for t in input_list]

    # Filter out the tuples where the sum of their elements is greater than 50
    filtered = [t for t in transformed if sum(t) > 50]

    return filtered

# Example usage
if __name__ == "__main__":
    input_list = [(1, 2, 3), (4, 5, 6, 7), (8, 9), (10,)]
    result = transform_filter_tuples(input_list)
    print(result)  # Expected output: [(2, 25, 3, 49), (4, 81)]

