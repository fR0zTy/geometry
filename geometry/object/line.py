# -*- coding : utf-8 -*-

import math

from geometry import Vector, Point


class Line:

    def __init__(self, direction_vector: Vector = Vector([1, 0, 0]), point: Point = Point(0, 0, 0)):

        if type(direction_vector) != Vector:
            raise TypeError("direction_vector must be of type Vector")
        if not isinstance(point, Point):
            raise TypeError("point must be of type Point")

        if direction_vector.is_undefined:
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
            elif prev is not None and not math.isclose(prev, v / u):
                return False
            else:
                prev = v / u

        return True

    @classmethod
    def from_points(cls, p0: Point, p1: Point) -> "Line":
        direction_vector = (p1 - p0).to_vector()
        return cls(direction_vector, p0)

    def __str__(self):
        return f"{self.__class__.__name__}(direction_vector={self.direction_vector}, point={self.point}"

    def __repr__(self):
        return str(self)
