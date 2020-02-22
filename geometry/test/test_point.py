# -*- coding : utf-8 -*-
import random

import pytest

from geometry import Point


@pytest.fixture
def rand_point():
    return Point(random.random(), random.random(), random.random())


def test_point_generation():
    Point(1, 2, 3)

    with pytest.raises(ValueError):
        Point("1", "2", "3")

    with pytest.raises(ValueError):
        Point(1, 3, complex(3, 4))

    Point(1.1, 2.2, 3.3)

    tup = (4, 3, 12)
    from_tuple = Point.from_tuple(tup)
    assert from_tuple == Point(*tup)


def test_point_add(rand_point):
    other = Point(1, 2, 3)
    added = rand_point + other

    assert added.x == rand_point.x + other.x
    assert added.y == rand_point.y + other.y
    assert added.z == rand_point.z + other.z


def test_point_sub(rand_point):
    other = Point(1, 2, 3)
    subtracted = rand_point - other

    assert subtracted.x == rand_point.x - other.x
    assert subtracted.y == rand_point.y - other.y
    assert subtracted.z == rand_point.z - other.z


def test_point_translate():
    p0 = Point(1, 2, 3)
    p0.translate(1, 2, 3)

    assert p0 == Point(2, 4, 6)


def test_point_translate_uniform():
    p0 = Point(1, 2, 4)
    p0.translate_uniform(5)

    assert p0 == Point(6, 7, 9)


def test_point_at_origin():
    origin_pt = Point.at_origin()
    assert origin_pt == Point(0, 0, 0)


def test_point_distance():
    p0 = Point(1, 2, 3)
    p1 = Point(1, 2, 3)

    assert p0.distance_to(p1) == 0

    p2 = Point(3, 4, 12)
    assert p2.distance_to(Point.at_origin()) == 13


def test_point_vector_magnitude():
    pt = Point(3, 4, 12)
    assert pt.magnitude() == 13

    pt = Point(0, 3, 4)
    assert pt.magnitude() == 5
