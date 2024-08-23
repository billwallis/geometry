"""
Define a line between two points.
"""

from __future__ import annotations

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
        else:
            return NotImplemented

    def __add__(self, other: Number | Point) -> Line:
        if isinstance(other, Line):
            raise TypeError("Cannot add two lines together.")
        elif isinstance(other, (Number, Point)):
            return Line(self.start + other, self.end + other)
        else:
            return NotImplemented

    def __radd__(self, other: Number | Point) -> Line:
        return self.__add__(other)

    def __sub__(self, other: Number | Point) -> Line:
        if isinstance(other, Line):
            raise TypeError("Cannot subtract two lines.")
        elif isinstance(other, (Number, Point)):
            return Line(self.start - other, self.end - other)
        else:
            return NotImplemented

    def rotate(self, angle: Number) -> Line:
        """
        Rotate the line anticlockwise by an angle about its starting
        point.

        :param angle: The angle to rotate by, in radians.

        :return: A new rotated line.
        """
        return Line(self.start, self.start + (self.end - self.start).rotate(angle))

    def as_vector(self) -> Point:
        """
        Return the line as a vector.
        """
        return self.end - self.start
