# -*- coding : utf-8 -*-

from geometry.types import Real


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
