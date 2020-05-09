# -*- coding : utf-8 -*-

import pytest

from geometry import Point, LineSegment


def test_line_segment_generation():
    LineSegment()

    with pytest.raises(ValueError):
        LineSegment(Point(0, 0, 0), Point(0, 0, 0))

    LineSegment(Point(1, 1, 1), Point(2, 2, 2))


def test_contains_point():
    ls1 = LineSegment(Point(1, 1, 1), Point(2, 2, 2))

    assert ls1.contains_point(Point(1.2, 1.2, 1.2))
    assert not ls1.contains_point(Point(0.5, 0.5, 0.5))
    assert ls1.contains_point(Point(1, 1, 1))
    assert ls1.contains_point(Point(2, 2, 2))
    assert not ls1.contains_point(Point(0, 1, 0))


def test_length():
    ls1 = LineSegment(Point(1, 0, 0), Point(2, 0, 0))
    ls2 = LineSegment(Point(3, 0, 0), Point(0, 4, 0))
    assert ls1.length() == 1
    assert ls2.length() == 5
