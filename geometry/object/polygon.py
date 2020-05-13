# -*- coding : utf-8 -*-

from typing import Iterable

from geometry import Point
from geometry.types import Real


class Polygon:

    def __init__(self, vertices: Iterable[Point]):
        self.vertices = vertices if isinstance(vertices, list) else [v for v in vertices]

    def translate(self, dx: Real, dy: Real, dz: Real) -> None:
        for vertex in self.vertices:
            vertex.translate(dx, dy, dz)
