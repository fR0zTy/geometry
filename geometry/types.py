# -*- coding : utf-8 -*-

from enum import Enum
from typing import Union, List

# Type definitions
Real = Union[int, float]
RealList = List[Real]

# Enums


class Axis(Enum):
    X = 1
    Y = 0
    Z = 2
