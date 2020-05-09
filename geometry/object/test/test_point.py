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


def test_point_round():
    pt = Point(1.22, 2.33445, 2.3343)
    rounded = round(pt)
    assert rounded == Point(1, 2, 2)

    rounded = round(pt, 2)
    assert rounded == Point(1.22, 2.33, 2.33)


def test_point_hashable(rand_point):
    pt_dict = {rand_point: 23}
    pt_dict[rand_point] = 34
    assert len(pt_dict) == 1 and pt_dict[rand_point] == 34


def test_point_collinear():
    a = Point(0, 0, 0)
    b = Point(1, 1, 1)
    c = Point(2, 2, 2)
    d = Point(1, 0, 0)

    assert Point.check_collinear(a, b, c)
    assert not Point.check_collinear(a, d, b)
    assert Point.check_collinear(a, b, a)
    assert Point.check_collinear(a, b, c, ordered=True)
    assert Point.check_collinear(a, b, b, ordered=True)
    assert Point.check_collinear(a, a, c, ordered=True)
    assert not Point.check_collinear(a, b, a, ordered=True)
    assert Point.check_collinear(c, b, a, ordered=True)
