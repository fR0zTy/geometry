# -*- coding : utf-8 -*-
import math

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


def test_vector_magnitude():
    v1 = Vector([3, 4, 12])
    assert v1.magnitude() == 13


def test_vector_scaling():
    v1 = Vector([1, 1, 1])
    assert v1.scale(2) == Vector([2, 2, 2])


def test_vector_normalize():
    v1 = Vector([4, 5, 6])
    normed = v1.normalize()
    assert math.isclose(normed.magnitude(), 1.0, rel_tol=1e-04)
