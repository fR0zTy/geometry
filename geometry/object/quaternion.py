# -*- coding : utf-8 -*-
from math import sqrt, isclose
from typing import Generator, Tuple

from geometry.types import Real
from geometry import Vector


class Quaternion:

    def __init__(self, w: Real = 1, x: Real = 0, y: Real = 0, z: Real = 0):
        self.scalar = w
        self.vector = Vector([x, y, z])

    @property
    def w(self) -> Real:
        return self.scalar

    @w.setter
    def w(self, value: Real) -> None:
        self.scalar = value

    @property
    def x(self) -> Real:
        return self.vector[0]

    @x.setter
    def x(self, value: Real) -> None:
        self.vector[0] = value

    @property
    def y(self) -> Real:
        return self.vector[1]

    @y.setter
    def y(self, value: Real) -> None:
        self.vector[1] = value

    @property
    def z(self) -> Real:
        return self.vector[2]

    @z.setter
    def z(self, value: Real) -> None:
        self.vector[2] = value

    def __iter__(self) -> Generator[Real, None, None]:
        yield self.scalar
        yield from self.vector

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(w={self.w:.4f}, x={self.x:.4f}, y={self.y:.4f}, z={self.z:.4f})"

    def __repr__(self) -> str:
        return self.__str__()

    def __neg__(self) -> "Quaternion":
        return Quaternion(*(-i for i in self))

    def __add__(self, other: "Quaternion") -> "Quaternion":
        if not isinstance(other, Quaternion):
            raise TypeError(f"Cannot add instances of type {type(other)} and {type(self)}")
        return Quaternion(self.scalar + other.scalar, *(self.vector + other.vector))

    def __sub__(self, other: "Quaternion") -> "Quaternion":
        if not isinstance(other, Quaternion):
            raise TypeError(f"Cannot subtract instances of type {type(other)} and {type(self)}")
        return Quaternion(self.scalar - other.scalar, *(self.vector - other.vector))

    def __mul__(self, other: "Quaternion") -> "Quaternion":
        if not isinstance(other, Quaternion):
            raise TypeError(f"Cannot multiply instances of type {type(other)} and {type(self)}")
        _scalar = self.scalar * other.scalar - self.vector.dot(other.vector)
        _vector = other.vector.scale(self.scalar) + self.vector.scale(other.scalar) + self.vector.cross(other.vector)
        return Quaternion(_scalar, *_vector)

    def __eq__(self, other: "Quaternion") -> "Quaternion":
        return all(isclose(i, j, rel_tol=1e-09, abs_tol=1e-09) for i, j in zip(self, other))

    def __hash__(self) -> int:
        return hash(self.as_tuple())

    def norm(self) -> "Quaternion":
        return sqrt(self.scalar ** 2 + self.vector.dot(self.vector))

    def inverse(self) -> "Quaternion":
        pass

    def conjugate(self) -> "Quaternion":
        return Quaternion(self.scalar, self.vector.scale(-1))

    def as_tuple(self) -> Tuple[Real]:
        return tuple(i for i in self)

    @classmethod
    def from_tuple(cls, tup: Tuple[Real]) -> "Quaternion":
        assert len(tup) == 4
        return cls(*tup)

    @classmethod
    def identity(cls) -> "Quaternion":
        return cls()
