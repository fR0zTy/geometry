# -*- coding : utf-8 -*-
from math import sqrt, isclose, acos, cos, sin
from typing import Generator, Tuple

from geometry.types import Real
from geometry import Vector
from geometry.utilities.copyable import CopyableMixin


class Quaternion(CopyableMixin):

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
            other = Quaternion.from_scalar(other)

        _scalar = self.scalar * other.scalar - self.vector.dot(other.vector)
        _vector = other.vector.scale(self.scalar) + self.vector.scale(other.scalar) + self.vector.cross(other.vector)
        return Quaternion(_scalar, *_vector)

    def __imul__(self, other: "Quaternion") -> "Quaternion":
        return self * other

    def __rmul__(self, other: "Quaternion") -> "Quaternion":
        if not isinstance(other, Quaternion):
            other = Quaternion.from_scalar(other)
        return other * self

    def __div__(self, other: "Quaternion") -> "Quaternion":
        if not isinstance(other, Quaternion):
            other = Quaternion.from_scalar(other)
        if other.is_zero_quaternion():
            raise ZeroDivisionError("other is a zero quaternion!")
        return other * self.inverse()

    def __truediv__(self, other: "Quaternion") -> "Quaternion":
        return self.__div__(other)

    def __pow__(self, exponent: Real) -> "Quaternion":
        norm = self.norm()
        if norm > 0:
            vector_mag = self.vector.magnitude()
            if vector_mag <= 0:
                return Quaternion.from_scalar(self.scalar ** exponent)
            unit_vector = self.vector.scale(1 / vector_mag)
            phi = acos(self.scalar / norm)
            _scalar = cos(exponent * phi)
            _vector = unit_vector.scale(sin(exponent * phi))
            return (norm ** exponent) * Quaternion(_scalar, *_vector)
        return self.copy()

    def __eq__(self, other: "Quaternion") -> "Quaternion":
        return all(isclose(i, j, rel_tol=1e-09, abs_tol=1e-09) for i, j in zip(self, other))

    def __hash__(self) -> int:
        return hash(self.as_tuple())

    def is_zero_quaternion(self) -> bool:
        return self == Quaternion(0, 0, 0, 0)

    def is_unit_quaternion(self) -> bool:
        return isclose(self._squared_sum(), 1.0, rel_tol=1e-09)

    def magnitude(self) -> Real:
        return self.norm()

    def _squared_sum(self) -> Real:
        return self.scalar ** 2 + self.vector.dot(self.vector)

    def norm(self) -> Real:
        return sqrt(self._squared_sum())

    def normalize(self) -> "Quaternion":
        if self.is_zero_quaternion():
            raise ValueError("Cannot normalize a zero quaternion!")
        n = self.norm()
        return Quaternion(*(i / n for i in self))

    def inverse(self) -> "Quaternion":
        if self.is_zero_quaternion():
            raise ValueError("Cannot invert a zero quaternion!")
        square_sum = self._squared_sum()
        return Quaternion(self.scalar / square_sum, *-self.vector.scale(1 / square_sum))

    def conjugate(self) -> "Quaternion":
        return Quaternion(self.scalar, -self.vector)

    def as_tuple(self) -> Tuple[Real]:
        return tuple(i for i in self)

    @classmethod
    def from_tuple(cls, tup: Tuple[Real]) -> "Quaternion":
        assert len(tup) == 4
        return cls(*tup)

    @classmethod
    def identity(cls) -> "Quaternion":
        return cls(1, 0, 0, 0)

    @classmethod
    def i(cls) -> "Quaternion":
        return cls(0, 1, 0, 0)

    @classmethod
    def j(cls) -> "Quaternion":
        return cls(0, 0, 1, 0)

    @classmethod
    def k(cls) -> "Quaternion":
        return cls(0, 0, 0, 1)

    @classmethod
    def from_scalar(cls, scalar: Real) -> "Quaternion":
        return cls(scalar, 0, 0, 0)
