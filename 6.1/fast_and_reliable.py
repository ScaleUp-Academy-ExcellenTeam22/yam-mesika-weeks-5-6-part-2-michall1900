from collections.abc import Callable
from functools import partial
from time import time
from typing import Any


def average_runtime(*function_parameters: Any, number_of_runs: int, function: Callable[[Any], Any]) -> float:
    """
    Return the average running time while running function "number of runs" times.
    :param function_parameters: Parameters that function should receive.
    :param number_of_runs: Time's number you want to run the function.
    :param function: Function to check. It's return value will not return from this function.
    :return: Average time if number of runs > 0, otherwise, -1.
    """
    sum_time = 0
    for iterate in range(number_of_runs):
        start = time()
        function(*function_parameters)
        end = time()
        sum_time += (end-start)
    return sum_time if number_of_runs > 0 else -1


def is_inside_object(item: Any, an_object: Any) -> bool:
    """
    Check if an item appeared inside an object.
    :param item: Any item that could appear inside the object.
    :param an_object: Any kind of an object.
    :return: True if it is, otherwise, false.
    """
    if item in an_object:
        return True
    return False


def main_fast_and_reliable() -> None:
    """
    Read the "words.txt" file into a list and a set.
    Then, check the average time for searching the word "zwitterion" 1000 times for each iterable.
    :return: None.
    """
    with open("words.txt", "r") as file:
        file_in_list = file.read().split("\n")
    file_in_set = set(file_in_list)
    compare_average_time = partial(average_runtime, "zwitterion", number_of_runs=1000,
                                   function=is_inside_object)
    print_result = lambda start_message_word, iterable: print(f"{start_message_word} average = ",
                                                              compare_average_time(iterable))
    print_result("list", file_in_list)
    print_result("set", file_in_set)


if __name__ == "__main__":
    main_fast_and_reliable()
