from typing import Iterator


def is_perfect_divider(current_num: int) -> bool:
    """
    Check if a number is a perfect divider or not.
    :param current_num: Number to check if it is a perfect divider.
    :return: True if it is, otherwise false.
    """
    return sum(filter(lambda num: not current_num % num, range(1, int(current_num/2) + 1))) == current_num


def find_perfect_dividers_generator() -> Iterator[int]:
    """
    Running in infinite and return each time one perfect divider (hows dividers summations
    that different from it equal to the number).
    :return: Perfect divider.
    """
    current_div = 6
    while True:
        if is_perfect_divider(current_div):
            yield current_div
        current_div += 1


def main_perfect_division() -> None:
    """
    Printing all of the perfect dividers (numbers hows divider summation except them are equal to it).
    :return: None.
    """
    for perfect_divider in find_perfect_dividers_generator():
        print(perfect_divider)


if __name__ == "__main__":
    main_perfect_division()
