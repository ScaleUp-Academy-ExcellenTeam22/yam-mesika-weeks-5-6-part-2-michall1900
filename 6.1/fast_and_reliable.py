from collections.abc import Callable
from functools import partial, wraps
import timeit
from typing import Any, Iterable


def average_run_time(runs_time: int) -> Callable[[Any], Any]:
    """
    Return the average running time while running function "runs_time" times.
    I used this site:
    https://www.pythontutorial.net/advanced-python/python-decorator-arguments/
    :param runs_time: Time's number you want to run the function.
    :return: Average time if number of runs > 0, otherwise, -1.
    """
    def decorator(function: Callable[[Any], Any]) -> Callable[[Any], Any]:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> float:
            sum_time = 0
            for iterate in range(runs_time):
                starting_time = timeit.default_timer()
                function(*args, **kwargs)
                sum_time += timeit.default_timer() - starting_time
            return sum_time if runs_time > 0 else -1
        return wrapper
    return decorator


@average_run_time(1000)
def is_inside_iterable(item: Any, iterable: Iterable[Any]) -> bool:
    """
    Check if an item appeared inside an iterable.
    :param item: Any item that could appear inside the iterable.
    :param iterable: Any kind of an iterable.
    :return: True if it is, otherwise, false.
    """
    return item in iterable


def main_fast_and_reliable() -> None:
    """
    Read the "words.txt" file into a list and a set.
    Then, check the average time for searching the word "zwitterion" 1000 times for each iterable.
    :return: None.
    """
    with open("words.txt", "r") as file:
        file_in_list = file.read().split("\n")
    file_in_set = set(file_in_list)
    compare_average_time = partial(is_inside_iterable, "zwitterion")
    print_result = lambda start_message_word, iterable: print(f"{start_message_word} average = ",
                                                              compare_average_time(iterable))
    print_result("list", file_in_list)
    print_result("set", file_in_set)


if __name__ == "__main__":
    main_fast_and_reliable()
