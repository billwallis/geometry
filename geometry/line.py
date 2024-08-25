"""
Define a line between two points.
"""

from __future__ import annotations

import math

from geometry.point import Number, Point


class Line:
    """
    A line between two points.
    """

    start: Number | Point
    end: Number | Point

    def __init__(self, start: Number | Point, end: Number | Point):
        self.start = start if isinstance(start, Point) else Point(start, start)
        self.end = end if isinstance(end, Point) else Point(end, end)

    def __str__(self):
        return f"Line({self.start}, {self.end})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other: Line) -> bool:
        if isinstance(other, Line):
            return self.start == other.start and self.end == other.end

        return NotImplemented

    def __add__(self, other: Number | Point) -> Line:
        """
        Add a line to a number or point.

        Adding a number to a line will add the number to both the start and end
        points. Adding a point to a line will add the point to both the start
        and end points.

        :param other: The number or point to add.

        :return: A new line.

        :raises TypeError: If adding two lines together.
        """
        if isinstance(other, Line):
            raise TypeError("Cannot add two lines together.")
        if isinstance(other, Number | Point):
            return Line(self.start + other, self.end + other)

        return NotImplemented

    def __radd__(self, other: Number | Point) -> Line:
        return self.__add__(other)

    def __sub__(self, other: Number | Point) -> Line:
        """
        Subtract a number or point from a line.

        Subtracting a number from a line will subtract the number from both the
        start and end points. Subtracting a point from a line will subtract the
        point from both the start and end points.

        :param other: The number or point to subtract.

        :return: A new line.

        :raises TypeError: If subtracting two lines.
        """
        if isinstance(other, Line):
            raise TypeError("Cannot subtract two lines.")
        if isinstance(other, Number | Point):
            return Line(self.start - other, self.end - other)

        return NotImplemented

    def rotate(self, angle: Number) -> Line:
        """
        Rotate the line anticlockwise by an angle about its starting
        point.

        :param angle: The angle to rotate by, in radians.

        :return: A new rotated line.
        """
        return Line(
            self.start,
            self.start + (self.end - self.start).rotate(angle),
        )

    def as_vector(self) -> Point:
        """
        Return the line as a vector.
        """
        return self.end - self.start

    @property
    def length(self) -> Number:
        """
        Return the length of the line.
        """
        return math.sqrt(
            (self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2
        )

    @property
    def slope(self) -> Number:
        """
        Return the slope of the line.

        If the line is vertical, return infinity.
        """
        if self.end.x == self.start.x:
            return math.inf

        return (self.end.y - self.start.y) / (self.end.x - self.start.x)

    @property
    def intercept(self) -> Number:
        """
        Return the y-intercept of the line.

        If the line is vertical, return ``None``.
        """
        if self.slope == math.inf:
            return None

        return self.start.y - self.slope * self.start.x
