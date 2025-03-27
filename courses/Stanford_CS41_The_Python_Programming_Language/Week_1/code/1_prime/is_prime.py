"""
File: is_prime.py
-----------------

Review of CS 41 Lecture 1. Implements a function that returns whether a number
is prime or not.
"""


def is_prime(n):
    """
    Returns True if n is prime and False otherwise.
    """
    n_root = int(n ** (1/2)) + 1

    for i in range(2, n_root):
        if n % i == 0:
            return False

    return True


if __name__ == '__main__':
    print(is_prime(41))
    print(is_prime(119))
    print(is_prime(203))
