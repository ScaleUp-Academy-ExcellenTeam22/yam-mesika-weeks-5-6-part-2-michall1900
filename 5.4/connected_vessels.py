from typing import Any, Iterable
from itertools import chain, zip_longest


def generator_interleave(*iterables: Iterable) -> Any:
    """
    Return items one by one in the order they should be if we will interleave them.
    :param iterables: Iterables item as many as you want.
    :return: Elements in each iterable in the order they should be if we interleave them.
    """
    iterators = list(map(lambda iterable: iter(iterable), iterables))
    counter_finish = 0
    while counter_finish != len(iterators):
        counter_finish = 0
        for it in iterators:
            try:
                yield next(it)
            except StopIteration:
                counter_finish += 1


def interleave(*iterables: Iterable) -> list:
    """
    Return a list of connected vessels (first cell of each iterable obj,
    then second and so on).
    Got help from
    https://stackoverflow.com/questions/48199961/how-to-interleave-two-lists-of-different-length
    :param iterables: Iterables objects.
    :return: List after interleaving elements.
    """
    return [element for element in chain.from_iterable(zip_longest(*iterables)) if element is not None]


def main_connected_vessels() -> None:
    """
    Print the result of the two implementations of interleaving functions.
    :return: None.
    """
    test = 'abc', [1, 2, 3], ('!', '@', '#'), {'hey': 'blue'}, {"func", "hello", 12, 15}
    print(interleave(*test))
    print([element for element in generator_interleave(*test)])


if __name__ == "__main__":
    main_connected_vessels()
