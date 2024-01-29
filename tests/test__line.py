"""
Tests for the ``geometry/line.py`` module.
"""

from __future__ import annotations

import math

import pytest

from geometry.line import Line
from geometry.point import Number, Point


@pytest.mark.parametrize(
    "line, start, end",
    [
        (Line(1, 2), 1, 2),
        (Line(1.0, 2.0), 1.0, 2.0),
    ],
)
def test__line__initialisation__numbers(line: Line, start: Number, end: Number):
    """
    Test the ``Line.__init__()`` method with numbers.
    """
    assert line.start == Point(start, start)
    assert line.end == Point(end, end)


def test__line__initialisation__points():
    """
    Test the ``Line.__init__()`` method with points.
    """
    line = Line(Point(1, 2), Point(3, 4))

    assert line.start == Point(1, 2)
    assert line.end == Point(3, 4)


def test__line__initialisation__mixed():
    """
    Test the ``Line.__init__()`` method with mixed types.
    """
    line = Line(1, Point(3, 4))

    assert line.start == Point(1, 1)
    assert line.end == Point(3, 4)


def test__line__string():
    """
    Test the ``Line.__str__()`` method.
    """
    line = Line(1, Point(3, 4))

    assert str(line) == "Line(Point(x=1, y=1), Point(x=3, y=4))"


def test__line__representation():
    """
    Test the ``Line.__repr__()`` method.
    """
    line = Line(1, Point(3, 4))

    assert repr(line) == "Line(Point(x=1, y=1), Point(x=3, y=4))"
    assert eval(repr(line)) == line


def test__line__equal__not_implemented():
    """
    Test that ``Line.__eq__()`` is ``False``.
    """
    assert (Line(1, 2) == "3") is False


@pytest.mark.parametrize(
    "line, other, expected",
    [
        (Line(1, 2), 3, Line(4, 5)),
        (Line(1, 2), Point(3, 4), Line(Point(4, 5), Point(5, 6))),
    ],
)
def test__line__addition(line: Line, other: Number | Point, expected: Line):
    """
    Test the ``Line.__add__()`` and ``Line.__radd__()`` method.
    """
    assert (line + other) == expected
    assert line.__radd__(other) == expected


@pytest.mark.parametrize(
    "line, other",
    [
        (Line(1, 2), "3"),
        (Line(1, 2), Line(3, 4)),
    ],
)
def test__line__addition__not_implemented(line: Line, other: str | Line):
    """
    Test that ``Line.__add__()`` fails.
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
def test__line__addition_inplace(points: list[Number | Point], expected: Line):
    """
    Test the ``Line.__iadd__()`` method.
    """
    actual = Line(0, 0)
    for point in points:
        actual += point

    assert actual == expected


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
def test__line__rotate(line: Line, angle: Number, expected: Line):
    """
    Test the ``Line.rotate()`` method.
    """
    assert line.rotate(angle) == expected


def test__line__as_vector():
    """
    Test the ``Line.rotate()`` method.
    """
    line = Line(1, 2)
    assert line.as_vector() == Point(1, 1)
