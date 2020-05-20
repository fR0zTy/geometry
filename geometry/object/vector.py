# -*- coding : utf-8 -*-

from math import sqrt, acos, isclose
from typing import Generator, Iterable, Tuple

from geometry.error import InvalidSizeError
from geometry.types import Real
from geometry.utilities.copyable import CopyableMixin


class Vector(CopyableMixin):

    def __init__(self, values: Iterable[Real] = []) -> None:
        self.values = [v for v in values]
        if not all(isinstance(v, (int, float)) for v in self.values):
            raise ValueError("values must be of type Real")

    def __iter__(self) -> Generator[Real, None, None]:
        yield from self.values

    def __neg__(self) -> "Vector":
        return Vector(-i for i in self)

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError(f"Cannot add instances of type {type(other)} and {type(self)}")
        if not len(self) == len(other):
            raise InvalidSizeError(f"Cannot add vectors of size {len(self)} and {len(other)}")
        return Vector(i + j for i, j in zip(self, other))

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError(f"Cannot subtract instances of type {type(other)} and {type(self)}")
        if not len(self) == len(other):
            raise InvalidSizeError(f"Cannot subtract vectors of size {len(self)} and {len(other)}")
        return Vector(i - j for i, j in zip(self, other))

    def __mul__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError(f"Cannot multiply instances of type {type(other)} and {type(self)}")
        if not len(self) == len(other):
            raise InvalidSizeError(f"Cannot multiply vectors of size {len(self)} and {len(other)}")
        return Vector(i * j for i, j in zip(self, other))

    def __truediv__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError(f"Cannot divide instances of type {type(other)} and {type(self)}")
        if not len(self) == len(other):
            raise InvalidSizeError(f"Cannot divide vectors of size {len(self)} and {len(other)}")
        return Vector(i / j for i, j in zip(self, other))

    def __eq__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError(f"Cannot compare instances of type {type(other)} and {type(self)}")
        if not len(self) == len(other):
            raise InvalidSizeError(f"Cannot compare vectors of size {len(self)} and {len(other)}")

        return all(isclose(i, j, rel_tol=1e-09, abs_tol=1e-04) for i, j in zip(self, other))

    def __getitem__(self, idx) -> Real:
        if idx >= len(self.values):
            raise IndexError(f"index {idx} is out of range for a Vector of size {len(self.values)}")
        return self.values[idx]

    def __setitem__(self, idx, value) -> None:
        if idx >= len(self.values):
            raise IndexError(f"index {idx} is out of range for a Vector of size {len(self.values)}")
        self.values[idx] = value

    def __hash__(self) -> int:
        return hash(self.as_tuple())

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(" + ", ".join([f"{i:.4f}" for i in self.values]) + ")"

    def __repr__(self) -> str:
        return str(self)

    def __round__(self, n=None) -> "Vector":
        return Vector(round(i, n) for i in self)

    def __len__(self) -> int:
        return len(self.values)

    def append(self, value: Real) -> None:
        self.values.append(value)

    def extend(self, values: Iterable[Real]) -> None:
        for v in values:
            self.values.append(v)

    def is_zero_vector(self) -> bool:
        return all(isclose(i, 0.0, abs_tol=1e-04) for i in self)

    def magnitude(self) -> Real:
        return sqrt(sum(i ** 2 for i in self))

    def normalize(self) -> "Vector":
        mag = self.magnitude()
        return Vector(i / mag for i in self)

    def scale(self, factor: Real) -> "Vector":
        return Vector(i * factor for i in self)

    def angle(self, other: "Vector") -> Real:
        return acos(self.dot(other) / self.magnitude() * other.magnitude())

    def dot(self, other: "Vector") -> Real:
        return sum(self * other)

    def cross(self, other: "Vector") -> "Vector":
        size_self, size_other = len(self), len(other)
        if not 1 < size_self < 4 or not 1 < size_other < 4:
            raise InvalidSizeError(f"Cross product of vector with size {len(self)} and {len(other)} is undefined!")

        u = self.copy()
        v = other.copy()
        if size_self < size_other:
            u.append(0)
        elif size_self > size_other:
            v.append(0)

        if len(u) == 2:
            u0, u1 = u
            v0, v1 = v
            return Vector([u0 * v1 - u1 * v0])
        else:
            u0, u1, u2 = u
            v0, v1, v2 = v
            return Vector([u1 * v2 - u2 * v1, u2 * v0 - u0 * v2, u0 * v1 - u1 * v0])

    def is_parallel(self, other: "Vector") -> bool:
        v1 = self.normalize()
        v2 = other.normalize()
        return isclose(v1.dot(v2), 1.0)

    def is_antiparallel(self, other: "Vector") -> bool:
        v1 = self.normalize()
        v2 = other.normalize()
        return isclose(v1.dot(v2), -1.0)

    def is_orthogonal(self, other: "Vector") -> Real:
        v1 = self.normalize()
        v2 = other.normalize()
        return isclose(abs(v1.dot(v2)), 0.0, abs_tol=1e-04)

    def as_tuple(self) -> Tuple[Real]:
        return tuple(i for i in self)

    @classmethod
    def from_tuple(cls, tup: Tuple[Real]) -> "Vector":
        return cls(tup)
