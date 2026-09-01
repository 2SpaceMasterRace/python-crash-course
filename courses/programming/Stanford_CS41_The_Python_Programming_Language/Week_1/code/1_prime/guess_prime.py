"""
File: guess_prime.py
--------------------

Prompts the user to enter a prime number.
"""
import is_prime as ip


def guess():
    """
    Chatbot which prompts the user to enter a number and tells the user if the
    number is prime or not.
    """
    print("Enter a number and I'll tell you if it's prime! Type 'exit' to exit.")
    while True:
        n = input("> ")
        if n == 'exit':
            break

        # Use the is_prime function from the other file to respond
        n = int(n)
        if ip.is_prime(n):
            print(f"{n} is prime!")
        else:
            print(f"{n} is not prime!")


if __name__ == '__main__':
    guess()
