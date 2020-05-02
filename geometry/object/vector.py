# -*- coding : utf-8 -*-

from copy import deepcopy
from math import sqrt
from typing import Generator, Iterable, Tuple

import numpy as np

from geometry.error import InvalidSizeError
from geometry.types import Real
from geometry.utilities import round_compare


class Vector:

    ROUND_PRECISION = 4

    __hash__ = None

    def __init__(self, values: Iterable[Real] = []) -> None:
        self.values = [v for v in values]
        if not all(isinstance(v, (int, float)) for v in self.values):
            raise ValueError("values must be of type Real")

    def __iter__(self) -> Generator[Real, None, None]:
        yield from self.values

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise ValueError(f"Cannot add instances of type {type(other)} and {type(self)}")
        if not len(self) == len(other):
            raise InvalidSizeError(f"Cannot add vectors of size {len(self)} and {len(other)}")
        return Vector(i + j for i, j in zip(self, other))

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise ValueError(f"Cannot subtract instances of type {type(other)} and {type(self)}")
        if not len(self) == len(other):
            raise InvalidSizeError(f"Cannot subtract vectors of size {len(self)} and {len(other)}")
        return Vector(i - j for i, j in zip(self, other))

    def __mul__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise ValueError(f"Cannot multiply instances of type {type(other)} and {type(self)}")
        if not len(self) == len(other):
            raise InvalidSizeError(f"Cannot multiply vectors of size {len(self)} and {len(other)}")
        return Vector(i * j for i, j in zip(self, other))

    def __truediv__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise ValueError(f"Cannot divide instances of type {type(other)} and {type(self)}")
        if not len(self) == len(other):
            raise InvalidSizeError(f"Cannot divide vectors of size {len(self)} and {len(other)}")
        return Vector(i / j for i, j in zip(self, other))

    def __eq__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise ValueError(f"Cannot compare instances of type {type(other)} and {type(self)}")
        if not len(self) == len(other):
            raise InvalidSizeError(f"Cannot compare vectors of size {len(self)} and {len(other)}")

        return all(round_compare(i, j, self.ROUND_PRECISION) for i, j in zip(self, other))

    def __str__(self) -> str:
        return f"Vector(values={str(self.values)})"

    def __repr__(self) -> str:
        return str(self)

    def __round__(self, n=None) -> "Vector":
        return Vector(round(i, n) for i in self)

    def __len__(self):
        return len(self.values)

    def copy(self) -> "Vector":
        return deepcopy(self)

    def magnitude(self) -> Real:
        return sqrt(sum(i ** 2 for i in self))

    def normalize(self) -> "Vector":
        mag = self.magnitude()
        return Vector(i / mag for i in self)

    def scale(self, factor: Real) -> "Vector":
        return Vector(i * factor for i in self)

    def as_numpy_array(self) -> np.ndarray:
        return np.array(self.values)

    def as_tuple(self) -> Tuple[Real]:
        return tuple(i for i in self)

    @property
    def is_undefined(self):
        return all(i == 0 for i in self)

    @classmethod
    def from_tuple(cls, tup: Tuple[Real]) -> "Vector":
        return cls(tup)

    @classmethod
    def from_numpy_array(cls, arr: np.ndarray) -> "Vector":
        return cls(arr)
