def list_of_primes(n: list[int]) -> list[int]:
    """
    Returns a list of prime numbers from a given list.

    Parameters:
    n (list[int]): A list of integers.

    Returns:
    list[int]: A list of prime numbers from the given list.
    """
    def is_prime(num: int) -> bool:
        """
        Returns True if the given number is prime, False otherwise.

        Parameters:
        num (int): An integer.

        Returns:
        bool: True if the given number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in n if is_prime(num)]

def main():
      list_of_primes([0, 1, 2, 3, 4, 5, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32])

if __name__ == "__main__":
    main()
