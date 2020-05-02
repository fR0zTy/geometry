# -*- coding : utf-8 -*-

import pytest

from geometry import Line, Point, Vector


def test_line_generation():
    Line()

    Line(direction_vector=Vector([1, 1, 1]), point=Point(2, 2, 2))

    with pytest.raises(TypeError):
        Line(direction_vector=Point(1, 1, 1))

    with pytest.raises(ValueError):
        Line(direction_vector=Vector([0, 0, 0]))

    Line.from_points(Point(1, 1, 1), Point(2, 2, 2))


def test_contains_point():
    l1 = Line.from_points(Point(1, 1, 1), Point(2, 2, 2))
    assert l1.contains_point(Point(3, 3, 3))
    assert l1.contains_point(Point(0, 0, 0))
    assert not l1.contains_point(Point(2, 3, 4))

    l2 = Line.from_points(Point(0, 0, 0), Point(2, 0, 0))
    assert l2.contains_point(Point(4, 0, 0))
    assert l2.contains_point(Point(-3, 0, 0))
    assert not l2.contains_point(Point(0, 1, 0))
