"""
Tests for the ``geometry/line.py`` module.
"""

from __future__ import annotations

import math

import pytest

from geometry.line import Line
from geometry.point import Number, Point


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 2, Line(1, 2)),
        (1.0, 2.0, Line(1.0, 2.0)),
        (1.0, 2.0, Line(1.0, 2.0)),
        (1, Point(2, 3), Line(1, Point(2, 3))),
        (Point(1, 2), Point(3, 4), Line(Point(1, 2), Point(3, 4))),
    ],
)
def test__line_can_be_initialised(
    start: Number | Point,
    end: Number | Point,
    expected: Line,
):
    """
    Test that a line can be initialised with numbers, points, and a mix of
    both.
    """
    line = Line(start, end)

    assert expected.start == line.start
    assert expected.end == line.end


def test__line_is_represented_correctly():
    """
    Test the string and representation of a line.
    """
    line = Line(1, Point(3, 4))

    assert str(line) == "Line(Point(x=1, y=1), Point(x=3, y=4))"
    assert repr(line) == "Line(Point(x=1, y=1), Point(x=3, y=4))"
    assert eval(repr(line)) == line  # noqa: S307


@pytest.mark.parametrize(
    "line, other, expected",
    [
        (Line(1, 2), Line(1, 2), True),
        (Line(1, 2), Line(1.0, 2.0), True),
        (Line(1, 2), Line(1, 3), False),
        (Line(1, 2), 3, False),
        (Line(1, 2), "3", False),
    ],
)
def test__line_can_be_compared_for_equality(
    line: Line,
    other: Line | str,
    expected: bool,
):
    """
    Test that lines can be compared for equality, and that comparisons with
    non-lines return ``False``.
    """
    assert (line == other) is expected


@pytest.mark.parametrize(
    "line, other, expected",
    [
        (Line(1, 2), 3, Line(4, 5)),
        (Line(1, 2), Point(3, 4), Line(Point(4, 5), Point(5, 6))),
    ],
)
def test__line_can_be_added_to_points_and_numbers(
    line: Line,
    other: Number | Point,
    expected: Line,
):
    """
    Test that lines can be added to points and numbers.
    """
    assert (line + other) == expected
    assert (other + line) == expected


@pytest.mark.parametrize(
    "line, other",
    [
        (Line(1, 2), "3"),
        (Line(1, 2), Line(3, 4)),
    ],
)
def test__line_addition_is_not_implemented_with_non_numbers(
    line: Line,
    other: str | Line,
):
    """
    Test that lines cannot be added to non-numerics.
    """
    with pytest.raises(TypeError):
        line + other


@pytest.mark.parametrize(
    "points, expected",
    [
        ([Point(1, 2), 3], Line(Point(4, 5), Point(4, 5))),
        ([Point(1, 2), Point(3, 4)], Line(Point(4, 6), Point(4, 6))),
    ],
)
def test__line_can_be_added_inplace(
    points: list[Number | Point],
    expected: Line,
):
    """
    Test that lines can be added together and to points/numbers in place.
    """
    actual = Line(0, 0)
    for point in points:
        actual += point

    assert actual == expected


@pytest.mark.parametrize(
    "line, other, expected",
    [
        (Line(4, 5), 3, Line(1, 2)),
        (Line(5, 6), Point(3, 4), Line(Point(2, 1), Point(3, 2))),
    ],
)
def test__line_can_subtract_points_and_numbers(
    line: Line,
    other: Number | Point,
    expected: Line,
):
    """
    Test that points and numbers can be subtracted from lines.
    """
    assert (line - other) == expected


def test__line_subtraction_is_not_implemented_with_non_numerics():
    """
    Test that lines and non-numerics cannot be subtracted from lines.
    """
    with pytest.raises(TypeError):
        Line(1, 2) - Line(1, 2)

    with pytest.raises(TypeError):
        Line(1, 2) - "3"


@pytest.mark.parametrize(
    "line, expected",
    [
        (Line(0, 0), 0),
        (Line(0, Point(1, 0)), 1),
        (Line(Point(0, 1), 0), 1),
        (Line(1, 2), math.sqrt(2)),
    ],
)
def test__line_has_length(line: Line, expected: Number):
    """
    Test that a line's length is calculated correctly.
    """
    assert math.isclose(line.length, expected)


@pytest.mark.parametrize(
    "line, expected",
    [
        (Line(0, 0), math.inf),
        (Line(1, 2), 1),
        (Line(0, Point(1, 0)), 0),
        (Line(Point(0, 1), 0), math.inf),
    ],
)
def test__line_has_slope(line: Line, expected: Number):
    """
    Test that a line's slope is calculated correctly.
    """
    assert line.slope == expected


@pytest.mark.parametrize(
    "line, expected",
    [
        (Line(0, 0), None),
        (Line(1, 2), 0),
        (Line(0, Point(1, 0)), 0),
        (Line(Point(0, 1), 0), None),
    ],
)
def test__line_has_intercept(line: Line, expected: Number):
    """
    Test that a line's intercept is calculated correctly.
    """
    assert line.intercept == expected


@pytest.mark.parametrize(
    "line, angle, expected",
    [
        (Line(1, 2), math.radians(0), Line(1, 2)),
        (Line(1, 2), math.radians(90), Line(1, Point(0, 2))),
        (Line(1, 2), math.radians(180), Line(1, Point(0, 0))),
        (Line(1, 2), math.radians(270), Line(1, Point(2, 0))),
        (Line(1, 2), math.radians(360), Line(1, 2)),
    ],
)
def test__line_can_be_rotated(line: Line, angle: Number, expected: Line):
    """
    Test that lines can be rotated.
    """
    assert line.rotate(angle) == expected


@pytest.mark.parametrize(
    "line, point, expected",
    [
        (Line(0, 1), Point(0, 0), True),
        (Line(0, 1), Point(1, 1), True),
        (Line(0, 1), Point(0.5, 0.5), True),
        (Line(0, 1), Point(0.25, 0.75), False),
        (Line(0, 1), Point(2, 2), False),
        (Line(0, 1), Point(-1, 0), False),
        (Line(0, 1), Point(0, -1), False),
        (Line(0, Point(0, 1)), Point(0, 1), True),
        (Line(0, Point(0, 1)), Point(0, 2), False),
        (Line(0, Point(1, 0)), Point(1, 0), True),
        (Line(0, Point(1, 0)), Point(2, 0), False),
    ],
)
def test__line_contains_points(line: Line, point: Point, expected: bool):
    """
    Test that a line determines whether it contains a point.
    """
    assert line.contains(point) == expected


def test__line_can_be_turned_into_a_vector():
    """
    Test that a line can be represented as a vector.
    """
    line = Line(1, 2)
    assert line.as_vector() == Point(1, 1)
