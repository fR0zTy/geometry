# -*- coding : utf-8 -*-

import pytest

from geometry import Vector


def test_vector_generation():
    Vector([1, 2, 3])
    Vector(i for i in range(10))

    with pytest.raises(ValueError):
        Vector(["1", "2", "3"])


def test_vector_add():
    v1 = Vector([1, 2, 3])
    v2 = Vector([1, 2, 3])

    v3 = v1 + v2
    assert v3 == Vector([2, 4, 6])


def test_vector_sub():
    v1 = Vector([1, 2, 3])
    v2 = Vector([1, 2, 3])

    v3 = v1 - v2
    assert v3 == Vector([0, 0, 0])


def test_vector_mul():
    v1 = Vector([1, 2, 3])
    v2 = Vector([1, 2, 3])

    v3 = v1 * v2
    assert v3 == Vector([1, 4, 9])


def test_vector_div():
    v1 = Vector([1, 2, 3])
    v2 = Vector([1, 2, 3])

    v3 = v1 / v2
    assert v3 == Vector([1, 1, 1])
