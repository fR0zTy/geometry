# -*- coding : utf-8 -*-

from geometry.types import Real
from typing import Iterable


def round_compare(a: Real, b: Real, precision: int = 4) -> bool:
    """
    Utility function for rounded comparision
    """
    return round(a, precision) == round(b, precision)


def is_close(a: Real, b: Real, threshold: int = 0.001) -> bool:
    """
    Utility function for checking if 2 given real numbers are close
    """
    return abs(a - b) < threshold


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
