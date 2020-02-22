# -*- coding : utf-8 -*-

import re
from copy import deepcopy
from math import atan2, sqrt
from typing import Generator, Tuple

import numpy as np

from geometry.types import Real


class Point:

    ROUND_PRECISION = 4

    def __init__(self, x: Real=0.0, y: Real=0.0, z: Real=0.0) -> None:

        if not all(isinstance(i, int) or isinstance(i, float) for i in (x, y, z)):
            raise ValueError("attributes must be of type int or float")

        self.x = x
        self.y = y
        self.z = z

        self.__round_compare = lambda a, b: round(a, self.ROUND_PRECISION) == round(b, self.ROUND_PRECISION)

    def __iter__(self) -> Generator[Real, None, None]:
        return (getattr(self, attr) for attr in ["x", "y", "z"])

    def __add__(self, other: "Point") -> "Point":
        return Point(x=self.x + other.x, y=self.y + other.y, z=self.z + other.z)

    def __sub__(self, other: "Point") -> "Point":
        return Point(x=self.x - other.x, y=self.y - other.y, z=self.z - other.z)

    def __mul__(self, other: "Point") -> "Point":
        if isinstance(other, Point):
            return Point(x=self.x * other.x, y=self.y * other.y, z=self.z * other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Point(x=self.x * other, y=self.y * other, z=self.z * other)
        else:
            raise ValueError("Other must be a point or a scalar")

    def __truediv__(self, other: "Point") -> "Point":
        if isinstance(other, Point):
            return Point(x=self.x / other.x, y=self.y / other.y, z=self.z / other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Point(x=self.x / other, y=self.y / other, z=self.z / other)
        else:
            raise ValueError("Other must be a point or a scalar")

    def __eq__(self, other: "Point") -> bool:
        return (self.__round_compare(self.x, other.x) and
                self.__round_compare(self.y, other.y) and
                self.__round_compare(self.z, other.z))

    def __hash__(self) -> int:
        return int(re.sub(r"\D", "", str(self)))

    def __str__(self) -> str:
        return f"Point(x={self.x:.2f}, y={self.y:.2f}, z={self.z:.2f})"

    def __repr__(self) -> str:
        return str(self)

    def __round__(self, n=None) -> "Point":
        return Point(*[round(i, n) for i in self])

    def translate(self, dx: Real, dy: Real, dz: Real) -> None:
        self.x += dx
        self.y += dy
        self.z += dz

    def translate_uniform(self, d: Real) -> None:
        self.translate(d, d, d)

    def rotate(self, q) -> "Point":
        raise NotImplementedError()

    def rotate_around_axis(self, axis, angle):
        raise NotImplementedError()

    def copy(self) -> "Point":
        return deepcopy(self)

    def distance_to(self, other) -> Real:
        return sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2 + (other.z - self.z) ** 2)

    def near(self, other, threshold=0.01) -> bool:
        return self.distance_to(other) <= threshold

    def as_tuple(self) -> Tuple[Real, Real, Real]:
        return (self.x, self.y, self.z)

    def as_numpy_array(self) -> np.ndarray:
        return np.array(self.as_tuple(), dtype=np.float)

    def angle(self) -> Real:
        return atan2(self.y, self.x)

    def magnitude(self) -> Real:
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    @classmethod
    def from_tuple(cls, tup) -> "Point":
        return cls(*tup)

    @classmethod
    def at_origin(cls) -> "Point":
        return cls()
