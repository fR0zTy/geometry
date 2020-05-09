# -*- coding : utf-8 -*-

from math import isclose
from typing import Optional

from geometry import Vector, Point


class Line:

    def __init__(self, direction_vector: Vector = Vector([1, 0, 0]), point: Point = Point(0, 0, 0)):

        if type(direction_vector) != Vector:
            raise TypeError("direction_vector must be of type Vector")
        if not isinstance(point, Point):
            raise TypeError("point must be of type Point")

        if direction_vector.is_zero_vector():
            raise ValueError(f"direction_vector: {direction_vector} is an undefined vector")
        self.direction_vector = direction_vector
        self.point = point

    def contains_point(self, point: Point) -> bool:
        dv = point - self.point
        prev = None

        for u, v in zip(self.direction_vector, dv):
            if u == 0:
                if v == 0:
                    continue
                else:
                    return False
            elif prev is not None and not isclose(prev, v / u):
                return False
            else:
                prev = v / u

        return True

    def is_parallel(self, other: "Line") -> bool:
        return (self.direction_vector.is_parallel(other.direction_vector) or
                self.direction_vector.is_antiparallel(other.direction_vector))

    def is_orthogonal(self, other: "Line") -> bool:
        return self.direction_vector.is_orthogonal(other.direction_vector)

    def intersection(self, other: "Line") -> Optional[Point]:
        if self.is_parallel(other):
            return None
        if self.contains_point(other.point):
            return other.point.copy()
        elif other.contains_point(self.point):
            return self.point.copy()

        connector_line = Line.from_points(self.point, other.point)
        otherXconnector = other.direction_vector.cross(connector_line.direction_vector)
        otherXself = other.direction_vector.cross(self.direction_vector)

        otherXconnector_mag = otherXconnector.magnitude()
        otherXself_mag = otherXself.magnitude()

        if any(isclose(i, 0.0, abs_tol=1e-04) for i in (otherXconnector_mag, otherXself_mag)):
            return None

        quotient = otherXconnector_mag / otherXself_mag
        interm = self.direction_vector.scale(quotient)
        if otherXconnector.is_parallel(otherXself):
            return self.point + interm
        elif otherXconnector.is_antiparallel(otherXself):
            return self.point - interm
        else:
            raise Exception("Something is wrong with the intersection calculation, please notify the author!")

    @classmethod
    def from_points(cls, p0: Point, p1: Point) -> "Line":
        direction_vector = (p1 - p0).to_vector()
        return cls(direction_vector, p0)

    def __str__(self):
        return f"{self.__class__.__name__}(direction_vector={self.direction_vector}, point={self.point}"

    def __repr__(self):
        return str(self)
