"""
@Description : Implementation of Point class
@Author: Eden Tamari
"""
import math

class Point:
    """
    The Point class represents a point on the plane, according to the Cartesian axis system

    Attributes:

        _x (int): represents the position on the X axis.
        _y (int): represents the position on the Y axis.
    """
    def __init__(self, x=0, y=0):
        """
                Initialize a Point
                Args:
                    _x (int): represents the position on the X axis.
                    _y (int): represents the position on the Y axis.
        """
        self._x = x
        self._y = y

    def get_x(self):
        """
                Display the value of the x coordinate.
                @Returns:
                    int: Value of x.
        """
        return self._x

    def get_y(self):
        """
                Display the value of the y coordinate.
                @Returns:
                    int: Value of y.
        """
        return self._y

    def set_x(self, num):
        """
                Changes the value of the x coordinate to num.
                @param:
                num (int): The new value of x
                @Returns:
                    void
        """
        self._x = num

    def set_y(self, num):
        """
                Changes the value of the y coordinate to num .
                @param:
                num (int): The new value of Y
                @Returns:
                    void
        """
        self._y = num

    def __str__(self):
        """
                Display The content of the object as a string of characters
                according to the accepted mathematical representation (x,y).
                @Returns:
                    str: (Value of x, Value of y).
        """
        return '(' + str(self._x) + ',' + str(self._y) + ')'

    def __eq__(self, other):
        """
                A method that implements the equality operator (==)
                that accepts a point as a parameter
                @param:
                other (Point): the point to be compared
                @Returns:
                    bool: True if equal, False otherwise.
        """
        return self._x == other._x and self._y == other._y

    def is_above(self, other):
        """
        The method checks if the point on which the method was
        invoked is above the point received as a parameter

        @param:
            other (Point): the point to be compared
        @Returns:
            bool: True if above the point, False otherwise.
        """

        return self._y > other._y

    def is_under(self, other):
        """
        The method checks whether the point on which the method was
        invoked is below the point received as a parameter

        @param:
            other (Point): the point to be compared
        @Returns:
            bool: True if under the point, False otherwise.
        """
        return self._y < other._y

    def is_left(self, other):
        """
        The method checks if the point on which the method was
        invoked is to the left of the point received as a parameter

        @param:
            other (Point): the point to be compared
        @Returns:
            bool: True if to the left of the point, False otherwise.
        """
        return self._x < other._x

    def is_right(self, other):
        """
           The method checks if the point on which the method was
           invoked is to the right of the point received as a parameter

           @param:
               other (Point): the point to be compared
           @Returns:
               bool: True if to the right of the point, False otherwise.
        """
        return self._x > other._x

    def distance(self, p):
        """
           Checks the distance between the points

           @param:
               p (Point): the point to be compared
           @Returns:
               int: distance between the points.
        """
        return math.sqrt((self._y - p.get_y())**2 + (self._x - p.get_x())**2)

    def distance00(self):
        """
           Checks the distance between the point on which the function
           was activated to the origin of the axes.

           @Returns:
               int: distance between the point to the origin of the axes.
        """
        return self.distance(Point(0, 0))

    def middle(self, p):
        """
           The method calculates the midpoint between the points

           @param:
               p (Point): the point to be compared
           @Returns:
               Point: the midpoint between the points.
        """
        return Point((self._x + p.get_x()) / 2, (self._y + p.get_y()) / 2)

    def move(self, dx, dy):
        """
           Moves the point on which the method is invoked
           by dx on the X-axis and dy on the Y-axis.

           @param:
               dx (int): Move X by DX
               dy (int): Move Y by DY
           @Returns:
               point: point after move
        """
        self.set_x(self._x + dx)
        self.set_y(self._y + dy)
        return self


