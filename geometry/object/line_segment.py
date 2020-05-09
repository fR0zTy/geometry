# -*- coding : utf-8 -*-

from geometry import Point


class LineSegment:

    def __init__(self, a: Point = Point(0, 0, 0), b: Point = Point(1, 0, 0)):
        if not all(isinstance(p, Point) for p in (a, b)):
            raise TypeError("args a and b must be of type Point")
        if a == b:
            raise ValueError("points a and b are same!")
        self.a = a
        self.b = b

    @property
    def direction_vector(self):
        return (self.b - self.a).to_vector()

    def contains_point(self, point: Point):
        return Point.check_collinear(self.a, point, self.b, ordered=True)

    def length(self):
        return self.a.distance_to(self.b)
