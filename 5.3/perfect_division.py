from math import isqrt
from typing import Iterator


def is_prime(num: int) -> bool:
    """
    Return answer to the question: is the number prime or not.
    :param num: An integer number to check if it is prime.
    :return: True if it prime, otherwise false.
    """
    # At first, checking if number is even and != 2 or < 2 (the first prime).
    # If it isn't, check if there are dividers to the received number (the number should be odd or = 2).
    return False if num < 2 or (num != 2 and num % 2 == 0) else all(num % div for div in range(3, isqrt(num) + 1, 2))


def all_int_generator() -> Iterator[int]:
    """
    Return all integer numbers one by one. Start from zero.
    :return: Integer number.
    """
    num = 0
    while True:
        yield num
        num += 1


def find_perfect_dividers_generator() -> Iterator[int]:
    """
    Running in an infinite loop and return each time one perfect divider
    (hows dividers summations except it equal to the divider).
    Note: I used Euclid - Euler theorem.
          Link to the theorem: https://en.wikipedia.org/wiki/Euclid%E2%80%93Euler_theorem
    :return: Perfect divider.
    """
    for power in all_int_generator():
        num = 2 ** power
        if is_prime(num - 1):
            yield num//2*(num - 1)


def main_perfect_division() -> None:
    """
    Print all of the perfect dividers (numbers hows divider summation except them are equal to those numbers).
    :return: None.
    """
    for perfect_divider in find_perfect_dividers_generator():
        print(perfect_divider)


if __name__ == "__main__":
    main_perfect_division()
