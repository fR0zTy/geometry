# -*- coding : utf-8 -*-

from geometry.types import Real
from typing import Iterable


def round_compare(a: Real, b: Real, precision: int = 4) -> bool:
    """
    Utility function for rounded comparision
    """
    return round(a, precision) == round(b, precision)


def all_equal(iterable: Iterable):
    """
    Utility function for checking if all the elements in an iterable are equal
    """
    if isinstance(iterable, list):
        return not iterable or iterable.count(iterable[0]) == len(iterable)
    elif isinstance(iterable, tuple):
        return iterable[1:] == iterable[:-1]
    else:
        # This is a generic solution for all iterables, the type checks above are
        # optimized for the respective types.
        it = iter(iterable)
        try:
            first = next(it)
        except StopIteration:
            return True
        return all(first == rest for rest in it)


def all_unique(iterable: Iterable):
    """
    Utility function for checking if all the elements are unique
    """
    try:
        seen = set()
        return not any(i in seen or seen.add(i) for i in iterable)
    except TypeError:
        # Exception handling for unhashable types
        seen = list()
        return not any(i in seen or seen.append(i) for i in iterable)
