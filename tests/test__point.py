"""
Tests for the ``geometry/point.py`` module.
"""

from __future__ import annotations

import math

import pytest

from geometry.point import Number, Point


@pytest.mark.parametrize(
    "point, other, expected",
    [
        (Point(1, 2), Point(1, 2), True),
        (Point(1, 2), Point(1.0, 2.0), True),
        (Point(1, 2), Point(1, 3), False),
    ],
)
def test__point__equal(point: Point, other: Point, expected: Point):
    """
    Test that points can be compared for equality.
    """
    assert (point == other) is expected


def test__point__not_equal():
    """
    Test that points are not equal to other types.
    """
    assert (Point(1, 2) == 3) is False
    assert (Point(1, 2) == "3") is False


@pytest.mark.parametrize(
    "point, other, expected",
    [
        (Point(1, 2), 3, Point(4, 5)),
        (Point(1.0, 2.0), 3.0, Point(4.0, 5.0)),
        (Point(1, 2), Point(3, 4), Point(4, 6)),
    ],
)
def test__point__addition(point: Point, other: Number | Point, expected: Point):
    """
    Test that points can be added together and to numbers.
    """
    assert (point + other) == expected
    assert (other + point) == expected


def test__point__addition__not_implemented():
    """
    Test that points cannot be added to non-numerics.
    """
    with pytest.raises(TypeError):
        Point(1, 2) + "3"


@pytest.mark.parametrize(
    "points, expected",
    [
        ([Point(1, 2), 3], Point(4, 5)),
        ([Point(1, 2), Point(3, 4)], Point(4, 6)),
    ],
)
def test__point__addition_inplace(
    points: list[Number | Point],
    expected: Point,
):
    """
    Test that points can be added together and to numbers in place.
    """
    actual = Point(0, 0)
    for point in points:
        actual += point

    assert actual == expected


@pytest.mark.parametrize(
    "point, other, expected",
    [
        (Point(4, 5), 3, Point(1, 2)),
        (Point(4.0, 5.0), 3.0, Point(1.0, 2.0)),
        (Point(4, 6), Point(3, 4), Point(1, 2)),
        (3.0, Point(1.0, 2.0), Point(2.0, 1.0)),
    ],
)
def test__point__subtraction(
    point: Number | Point,
    other: Number | Point,
    expected: Point,
):
    """
    Test that points can be subtracted from each other and from numbers.
    """
    assert (point - other) == expected


def test__point__subtraction__not_implemented():
    """
    Test that points cannot be subtracted from non-numerics.
    """
    with pytest.raises(TypeError):
        Point(1, 2) - "3"


@pytest.mark.parametrize(
    "points, expected",
    [
        ([Point(4, 5), 3], Point(-7, -8)),
        ([Point(4, 6), Point(3, 4)], Point(-7, -10)),
    ],
)
def test__point__subtraction_inplace(
    points: list[Number | Point],
    expected: Point,
):
    """
    Test that points can be subtracted from each other and from numbers in
    place.
    """
    actual = Point(0, 0)
    for point in points:
        actual -= point

    assert actual == expected


@pytest.mark.parametrize(
    "point, expected",
    [
        (Point(1, 2), Point(-1, -2)),
        (Point(0, 0), Point(0, 0)),
        (Point(-3, 4), Point(3, -4)),
    ],
)
def test__point__negation(point: Point, expected: Point):
    """
    Test that points can be negated.
    """
    assert -point == expected


@pytest.mark.parametrize(
    "point, other, expected",
    [
        (Point(1, 2), 3, Point(3, 6)),
        (Point(1.0, 2.0), 3.0, Point(3.0, 6.0)),
        (Point(1, 2), Point(3, 4), Point(3, 8)),
    ],
)
def test__point__multiplication(
    point: Point,
    other: Number | Point,
    expected: Point,
):
    """
    Test that points can be multiplied by each other and by numbers.
    """
    assert (point * other) == expected
    assert point.__rmul__(other) == expected


def test__point__multiplication__not_implemented():
    """
    Test that points cannot be multiplied by non-numerics.
    """
    with pytest.raises(TypeError):
        Point(1, 2) * "3"


@pytest.mark.parametrize(
    "points, expected",
    [
        ([Point(1, 2), 3], Point(3, 6)),
        ([Point(1, 2), Point(3, 4)], Point(3, 8)),
    ],
)
def test__point__multiplication_inplace(
    points: list[Number | Point],
    expected: Point,
):
    """
    Test that points can be multiplied by each other and by numbers in
    place.
    """
    actual = Point(1, 1)
    for point in points:
        actual *= point

    assert actual == expected


@pytest.mark.parametrize(
    "point, angle, expected",
    [
        (Point(1, 2), math.radians(0), Point(1, 2)),
        (Point(1, 2), math.radians(90), Point(-2, 1)),
        (Point(1, 2), math.radians(180), Point(-1, -2)),
        (Point(1, 2), math.radians(270), Point(2, -1)),
        (Point(1, 2), math.radians(360), Point(1, 2)),
    ],
)
def test__point__rotate(point: Point, angle: Number, expected: Point):
    """
    Test that points can be rotated.
    """
    assert point.rotate(angle) == expected
