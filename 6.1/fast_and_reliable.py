from collections.abc import Callable
from time import time
from typing import Any, Iterable


def average_time(number_of_runs: int, function: Callable[[Any], None], *function_parameters: Any) -> float:
    sum_time = 0
    for iterate in range(number_of_runs):
        start = time()
        function(*function_parameters)
        end = time()
        sum_time += (end-start)
    return sum_time if number_of_runs > 0 else number_of_runs


def find_word_inside_iterable(word: str, iterable: Iterable[str]) -> None:
    if word in iterable:
        pass


def main_fast_and_reliable() -> None:
    with open("words.txt", "r") as file:
        file_in_list = file.read()
    file_in_set = set(file_in_list)
    print("list average = ", average_time(1000, find_word_inside_iterable, "zwitterion", file_in_list))
    print("set average = ", average_time(1000, find_word_inside_iterable, "zwitterion", file_in_set))


if __name__ == "__main__":
    main_fast_and_reliable()
