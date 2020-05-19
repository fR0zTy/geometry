# -*- coding : utf-8 -*-

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


def test_quaternion_neg():
    q1 = Quaternion(1, 2, 3, 4)
    assert -q1 == Quaternion(-1, -2, -3, -4)
