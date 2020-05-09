# -*- coding : utf-8 -*-

import re
from math import atan2, sqrt, isnan
from typing import Tuple

import numpy as np

from geometry import Vector
from geometry.error import InvalidSizeError
from geometry.types import Real, Axis
from geometry.utilities import round_compare


class Point(Vector):

    ROUND_PRECISION = 4

    def __init__(self, x: Real = 0.0, y: Real = 0.0, z: Real = 0.0) -> None:
        super().__init__([x, y, z])

    @property
    def x(self) -> Real:
        return self.values[0]

    @x.setter
    def x(self, value: Real) -> None:
        assert isinstance(value, (int, float))
        self.values[0] = value

    @property
    def y(self) -> Real:
        return self.values[1]

    @y.setter
    def y(self, value: Real) -> None:
        assert isinstance(value, (int, float))
        self.values[1] = value

    @property
    def z(self) -> Real:
        return self.values[2]

    @z.setter
    def z(self, value) -> None:
        assert isinstance(value, (int, float))
        self.values[2] = value

    def __add__(self, other: "Point") -> "Point":
        if not isinstance(other, Vector):
            raise ValueError(f"Cannot add instances of type {type(other)} and {type(self)}")

        return Point(*super().__add__(other))

    def __sub__(self, other: "Point") -> "Point":
        if not isinstance(other, Vector):
            raise ValueError(f"Cannot subtract instances of type {type(other)} and {type(self)}")

        return Point(*super().__sub__(other))

    def __mul__(self, other: "Point") -> "Point":
        if not isinstance(other, Vector):
            raise ValueError(f"Cannot multiply instances of type {type(other)} and {type(self)}")

        return Point(*super().__mul__(other))

    def __truediv__(self, other: "Point") -> "Point":
        if not isinstance(other, Vector):
            raise ValueError(f"Cannot divide instances of type {type(other)} and {type(self)}")

        return Point(*super().__truediv__(other))

    def __eq__(self, other: "Point") -> bool:
        return (round_compare(self.x, other.x, self.ROUND_PRECISION) and
                round_compare(self.y, other.y, self.ROUND_PRECISION) and
                round_compare(self.z, other.z, self.ROUND_PRECISION))

    def __hash__(self) -> int:
        return int(re.sub(r"\D", "", str(self)))

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(x={self.x:.4f}, y={self.y:.4f}, z={self.z:.4f})"

    def __round__(self, n=None) -> "Point":
        return Point(*(round(i, n) for i in self))

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

    def distance_to(self, other) -> Real:
        return sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2 + (other.z - self.z) ** 2)

    def near(self, other, threshold=0.01) -> bool:
        return self.distance_to(other) <= threshold

    def angle(self, axis: Axis) -> Real:
        if axis == Axis.X:
            return atan2(sqrt(self.y ** 2 + self.z ** 2), self.x)
        elif axis == Axis.Y:
            return atan2(sqrt(self.z ** 2 + self.x ** 2), self.y)
        elif axis == Axis.Z:
            return atan2(sqrt(self.x ** 2 + self.y ** 2), self.z)
        else:
            raise ValueError("Invalid value for axis")

    def to_vector(self):
        return Vector(self)

    @property
    def is_undefined(self):
        return any(isnan(i) for i in self)

    @property
    def is_origin(self):
        return all(i == 0 for i in self)

    @classmethod
    def at_origin(cls) -> "Point":
        return cls()

    @classmethod
    def from_tuple(cls, tup: Tuple[Real, Real, Real]) -> "Point":
        if len(tup) != 3:
            raise InvalidSizeError("length of tuple must be 3")
        return cls(*tup)

    @classmethod
    def from_numpy_array(cls, arr: np.ndarray) -> "Point":
        if len(arr) != 3:
            raise InvalidSizeError("array must be of size 3")
        return cls(*arr)

    @staticmethod
    def check_collinear(a: "Point", b: "Point", c: "Point") -> bool:
        u = (b - a).to_vector()
        v = (c - a).to_vector()

        uXv = u.cross(v)
        if uXv.is_zero_vector():
            return True
        return False
