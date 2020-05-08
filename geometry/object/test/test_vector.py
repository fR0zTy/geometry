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


def test_vector_dot():
    v1 = Vector([1, 2, 3])
    v2 = Vector([1, 2, 3])
    assert v1.dot(v2) == 14


def test_vector_angle():
    v1 = Vector([1, 0, 0])
    v2 = Vector([0, 1, 0])
    assert math.isclose(v1.angle(v2), math.pi / 2, rel_tol=1e-04)


def test_vector_parallel():
    v1 = Vector([1, 1, 1])
    v2 = Vector([3, 3, 3])
    v3 = Vector([0, 1, 0])

    assert v1.is_parallel(v2)
    assert not v2.is_parallel(v3)
    assert not v3.is_parallel(v1)


def test_vector_antiparallel():
    v1 = Vector([1, 1, 1])
    v2 = Vector([-1, -1, -1])
    v3 = Vector([0, 0, 1])

    assert v1.is_antiparallel(v2)
    assert not v2.is_antiparallel(v3)
    assert not v3.is_antiparallel(v1)


def test_vector_orthogonal():
    v1 = Vector([1, 0, 0])
    v2 = Vector([0, 1, 0])
    v3 = Vector([0, 0, 1])
    v4 = Vector([1, 1, 1])

    assert v1.is_orthogonal(v2)
    assert v2.is_orthogonal(v3)
    assert v3.is_orthogonal(v1)
    assert not v1.is_orthogonal(v4)
