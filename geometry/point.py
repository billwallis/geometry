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
        else:
            return NotImplemented

    def __add__(self, other: Number | Point) -> Point:
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, Number):
            return Point(self.x + other, self.y + other)
        else:
            return NotImplemented

    def __radd__(self, other: Number | Point) -> Point:
        return self.__add__(other)

    def __sub__(self, other: Number | Point) -> Point:
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        elif isinstance(other, Number):
            return Point(self.x - other, self.y - other)
        else:
            return NotImplemented

    def __rsub__(self, other: Number | Point) -> Point:
        return self.__sub__(other)

    def __mul__(self, other: Number | Point) -> Point:
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        elif isinstance(other, Number):
            return Point(self.x * other, self.y * other)
        else:
            return NotImplemented

    def __rmul__(self, other: Number | Point) -> Point:
        return self.__mul__(other)

    def __imul__(self, other: Number | Point) -> Point:
        return self.__mul__(other)

    def rotate(self, angle: Number) -> Point:
        """
        Rotate the point anticlockwise by an angle.

        :param angle: The angle to rotate by, in radians.

        :return: A new rotated point.
        """
        return Point(
            round(self.x * math.cos(angle) - self.y * math.sin(angle), 8),
            round(self.x * math.sin(angle) + self.y * math.cos(angle), 8),
        )
