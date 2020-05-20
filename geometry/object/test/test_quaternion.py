# -*- coding : utf-8 -*-

import pytest

from geometry import Quaternion


def test_quaternion_generation():
    q = Quaternion()
    identity = (1, 0, 0, 0)
    assert all(i == j for i, j in zip(q, identity))

    q_id = Quaternion.identity()
    assert all(i == j for i, j in zip(q_id, identity))


def test_quaternion_add():
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(1, 2, 3, 4)
    q3 = Quaternion(2, 4, 6, 8)
    assert q1 + q2 == q3

    q1 += q2
    assert q1 == q3

    with pytest.raises(TypeError):
        q1 + 45


def test_quaternion_neg():
    q1 = Quaternion(1, 2, 3, 4)
    assert -q1 == Quaternion(-1, -2, -3, -4)


def test_quaternion_sub():
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(1, 1, 0, 0)
    q3 = Quaternion(0, 1, 3, 4)

    assert q1 - q2 == q3

    q1 -= q2
    assert q1 == q3

    with pytest.raises(TypeError):
        q1 - 45


def test_quaternion_mul_basis():
    _ = Quaternion.identity()
    i = Quaternion(0, 1, 0, 0)
    j = Quaternion(0, 0, 1, 0)
    k = Quaternion(0, 0, 0, 1)

    # test identity multiplication
    assert _ * i == i
    assert i * _ == i
    assert j * _ == j
    assert _ * j == j
    assert _ * k == k
    assert k * _ == k

    i2 = i * i
    j2 = j * j
    k2 = k * k
    ijk = i * j * k
    assert i2 == j2 == k2 == ijk == -_


def test_quaternion_mul_real():
    q1 = Quaternion(1, 2, 3, 4)
    real = 4
    q2 = Quaternion(*(i * real for i in q1))

    assert q1 * real == q2


def test_quaternion_div():
    q1 = Quaternion(1, 2, 3, 4)

    assert q1 / q1 == Quaternion.identity()


def test_quaternion_div_real():
    q1 = Quaternion(1, 2, 3, 4)
    real = 4
    q2 = Quaternion(*(i / real for i in q1))

    assert q1 / real == q2


def test_quaternion_pow():
    _ = Quaternion.identity()
    i = Quaternion(0, 1, 0, 0)
    j = Quaternion(0, 0, 1, 0)
    k = Quaternion(0, 0, 0, 1)

    i2 = i ** 2
    j2 = j ** 2
    k2 = k ** 2

    assert i2 == j2 == k2


def test_quaternion_normalize():
    q1 = Quaternion(1, 2, 3, 4)
    normalized = q1.normalize()
    assert normalized.is_unit_quaternion()

    with pytest.raises(ValueError):
        zero_q = Quaternion(0, 0, 0, 0)
        zero_q.normalize()


def test_quaternion_inverse():
    q1 = Quaternion(1, 2, 3, 4)
    inv = q1.inverse()
    assert q1 * inv == Quaternion.identity()

    with pytest.raises(ValueError):
        zero_q = Quaternion(0, 0, 0, 0)
        zero_q.inverse()
