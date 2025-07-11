"""
Tests for the ``geometry/point.py`` module.
"""

from __future__ import annotations

import math

import pytest

from geometry.point import Number, Point


def test__point_can_be_used_as_a_key_in_a_dict():
    """
    Points can be used as keys in a dictionary.
    """

    assert {Point(1, 2): "value"}[Point(1, 2)] == "value"


@pytest.mark.parametrize(
    "point, other, expected",
    [
        (Point(1, 2), Point(1, 2), True),
        (Point(1, 2), Point(1.0, 2.0), True),
        (Point(1, 2), Point(1, 3), False),
        (Point(1, 2), 3, False),
        (Point(1, 2), "3", False),
    ],
)
def test__point_can_be_compared_for_equality(
    point: Point,
    other: Point,
    expected: Point,
):
    """
    Points can be compared for equality.
    """
    assert (point == other) is expected


@pytest.mark.parametrize(
    "point, other, expected",
    [
        (Point(1, 2), 3, Point(4, 5)),
        (Point(1.0, 2.0), 3.0, Point(4.0, 5.0)),
        (Point(1, 2), Point(3, 4), Point(4, 6)),
    ],
)
def test__point_can_be_added_to_points_and_numbers(
    point: Point,
    other: Number | Point,
    expected: Point,
):
    """
    Points can be added together and to numbers.
    """
    assert (point + other) == expected
    assert (other + point) == expected


def test__point_addition_is_not_implemented_with_non_numbers():
    """
    Points cannot be added to non-numerics.
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
def test__point_can_be_added_inplace(
    points: list[Number | Point],
    expected: Point,
):
    """
    Points can be added together and to numbers in place.
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
def test__point_can_subtract_points_and_numbers(
    point: Number | Point,
    other: Number | Point,
    expected: Point,
):
    """
    Points can be subtracted from each other and from numbers.
    """
    assert (point - other) == expected


def test__point_subtraction_is_not_implemented_with_non_numerics():
    """
    Points cannot be subtracted from non-numerics.
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
def test__point_can_subtract_inplace(
    points: list[Number | Point],
    expected: Point,
):
    """
    Points can be subtracted from each other and from numbers in place.
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
def test__point_has_negation(point: Point, expected: Point):
    """
    Points can be negated.
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
def test__point_can_be_multiplied_to_points_and_numbers(
    point: Point,
    other: Number | Point,
    expected: Point,
):
    """
    Points can be multiplied by each other and by numbers.
    """
    assert point * other == expected
    assert other * point == expected


def test__point_multiplication_is_not_implemented_for_non_numerics():
    """
    Points cannot be multiplied by non-numerics.
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
def test__point_can_be_multiplied_inplace(
    points: list[Number | Point],
    expected: Point,
):
    """
    Points can be multiplied by each other and by numbers in place.
    """
    actual = Point(1, 1)
    for point in points:
        actual *= point

    assert actual == expected


@pytest.mark.parametrize(
    "point_to_rotate, point_of_rotation, angle, expected",
    [
        # Rotate a point around the origin
        (Point(1, 2), Point(0, 0), math.radians(0), Point(1, 2)),
        (Point(1, 2), Point(0, 0), math.radians(90), Point(-2, 1)),
        (Point(1, 2), Point(0, 0), math.radians(180), Point(-1, -2)),
        (Point(1, 2), Point(0, 0), math.radians(270), Point(2, -1)),
        (Point(1, 2), Point(0, 0), math.radians(360), Point(1, 2)),
        # Rotate a point around another point
        (Point(1, 2), Point(1, 1), math.radians(0), Point(1, 2)),
        (Point(1, 2), Point(1, 1), math.radians(90), Point(0, 1)),
        (Point(1, 2), Point(1, 1), math.radians(180), Point(1, 0)),
        (Point(1, 2), Point(1, 1), math.radians(270), Point(2, 1)),
        (Point(1, 2), Point(1, 1), math.radians(360), Point(1, 2)),
    ],
)
def test__point_can_be_rotated(
    point_to_rotate: Point,
    point_of_rotation: Point,
    angle: Number,
    expected: Point,
):
    """
    Points can be rotated.
    """
    assert (
        point_to_rotate.rotate(by=angle, around=point_of_rotation) == expected
    )
