# -*- coding : utf-8 -*-

from typing import Iterable

from geometry import Point


class Path:

    def __init__(self, points: Iterable[Point]):
        self.points = points if isinstance(points, list) else [p for p in points]
        assert len(self.points) > 1, "Number of points must be more than 1"

    def append(self, point: Point) -> None:
        self.points.append(point)

    def insert(self, index: int, point: Point) -> None:
        self.points.insert(index, point)

    def remove(self, point) -> None:
        self.points.remove(point)

    def pop(self, index) -> None:
        self.points.pop(index)
