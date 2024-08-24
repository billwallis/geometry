"""
Define a point in n-dimensional space.
"""

from __future__ import annotations

import math
from typing import NamedTuple

Number = int | float  # Consider using the `numbers` module


class Point(NamedTuple):
    """
    A coordinate in 2-dimensional space.
    """

    x: Number
    y: Number

    def __eq__(self, other: Point) -> bool:
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y

        return NotImplemented

    def __add__(self, other: Number | Point) -> Point:
        """
        Add a point to another point or a number.

        Adding a point to a point will add the x and y coordinates. Adding a
        number to a point will add the number to both coordinates.

        :param other: The point or number to add.

        :return: A new point.
        """
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        if isinstance(other, Number):
            return Point(self.x + other, self.y + other)

        return NotImplemented

    def __radd__(self, other: Number | Point) -> Point:
        return self.__add__(other)

    def __sub__(self, other: Number | Point) -> Point:
        """
        Subtract a point or a number from a point.

        Subtracting a point from a point will subtract the x and y coordinates.
        Subtracting a number from a point will subtract the number from the
        coordinates.

        :param other: The point or number to subtract.

        :return: A new point.
        """
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        if isinstance(other, Number):
            return Point(self.x - other, self.y - other)

        return NotImplemented

    def __rsub__(self, other: Number | Point) -> Point:
        return -self.__sub__(other)

    def __neg__(self) -> Point:
        return Point(-self.x, -self.y)

    def __mul__(self, other: Number | Point) -> Point:
        """
        Multiply a point with another point or a number.

        Multiplying a point with a point will multiply the x and y coordinates.
        Multiplying a point with a number will multiply the number with the
        coordinates.

        :param other: The point or number to multiply.

        :return: A new point.
        """
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        if isinstance(other, Number):
            return Point(self.x * other, self.y * other)

        return NotImplemented

    def __rmul__(self, other: Number | Point) -> Point:
        return self.__mul__(other)

    def __imul__(self, other: Number | Point) -> Point:
        return self.__mul__(other)

    def rotate(self, angle: Number) -> Point:
        """
        Rotate the point anticlockwise around (0, 0) by an angle.

        :param angle: The angle to rotate by, in radians.

        :return: A new rotated point.
        """
        return Point(
            round(self.x * math.cos(angle) - self.y * math.sin(angle), 8),
            round(self.x * math.sin(angle) + self.y * math.cos(angle), 8),
        )
