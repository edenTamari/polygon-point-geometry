"""
@Description : The Polygon class represents a convex polygon in a plane
@Author: Eden_Tamari
"""
import math

from Point import Point
class Polygon:
    """
    The Polygon class represents a convex polygon on the plane

    Attributes:

        _vertics (list): A list that stores the list of vertices.
    """
    def __init__(self):
        """
                Initialize a Polygon instance.
                Args:
                    _vertics (list): A list that stores the list of vertices.
        """
        self._vertics = list()

    def add_vertex(self, p):
        """
                A Boolean method that adds a vertex to a polygon.

                @param:
                    p (point): A vertex we will add to the list
                @Returns:
                    bool: True if the vertex was added, False otherwise.
        """
        if self.find_vertex(p) == -1:
            self._vertics.append(p)
            return True
        return False

    def highest_vertex(self):
        """
                Checking which vertex is the highest

                @Returns:
                (point) the highest vertex
        """
        if not self._vertics:
            return None
        highest_point = self._vertics[0]
        for point in self._vertics:
            if point.is_above(highest_point):
                highest_point = point
        return highest_point

    def __str__(self):
        """
                A character string representing the polygon.

                @Returns:
                (str) A character string representing the polygon.
        """
        if self._vertics:
            str_ver = '('
            for point in self._vertics:
                if point == self._vertics[-1]:
                    str_ver += point.__str__()
                else:
                    str_ver += point.__str__() + ', '
            str_ver += ')'
            return "The polygon has " + str(len(self._vertics)) + " vertices:\n" + str_ver
        return "The polygon has " + str(len(self._vertics)) + " vertices."

    def calc_perimeter(self):
        """
                Calculates the perimeter of the polygon

                @Returns:
                int: perimeter of the polygon
        """
        if len(self._vertics) == 0 or len(self._vertics) == 1:
            return 0
        if len(self._vertics) == 2:
            return self._vertics[0].distance(self._vertics[1])
        perimeter = 0.0
        for i in range(len(self._vertics)):
            if i == len(self._vertics) - 1:
                perimeter += self._vertics[i].distance(self._vertics[0])
            else:
                perimeter += self._vertics[i].distance(self._vertics[i+1])
        return perimeter

    def calc_area(self):
        """
                Calculates the area of the polygon

                @Returns:
                int: area of the polygon
        """
        if len(self._vertics) < 3:
            return 0
        area = 0
        for i in range(1, len(self._vertics) - 1):
            area += self.__calc_triangular_area__(self._vertics[0], self._vertics[i], self._vertics[i+1])
        return area

    def __calc_triangular_area__(self, p1, p2, p3):
        """
                Calculate the area of the triangle.

                @param:
                    p1 (point): A vertex of the triangle
                    p2 (point): A vertex of the triangle
                    p3 (point): A vertex of the triangle
                @Returns:
                    int: area of the triangle
        """
        a = p1.distance(p2)
        b = p2.distance(p3)
        c = p3.distance(p1)
        s = (a + b + c)/2
        return math.sqrt(s * (s-a) * (s-b) * (s-c))

    def is_bigger(self, other):
        """
                Checking which polygon is bigger

                @param:
                    other (Polygon): A Polygon
                @Returns:
                    polygon
        """
        return self.calc_area() > other.calc_area()

    def find_vertex(self, p):
        """
                Checks if the point belongs to the polygon and if so in which index in the list

                @param:
                    p (Point): A Point
                @Returns:
                    int: index of the point in the polygon or -1
        """
        if p not in self._vertics:
            return -1
        return self._vertics.index(p)

    def get_next_vertex(self, p):
        """
                Check which point appears after the point we received as a parameter

                @param:
                    p (Point): A Point
                @Returns:
                    point: next point in the polygon
        """
        if self.find_vertex(p) == -1:
            return None
        if p in self._vertics and len(self._vertics) == 1:
            return p
        index_p = self.find_vertex(p)
        if index_p == len(self._vertics) - 1:
            return self._vertics[0]
        else:
            return self._vertics[index_p + 1]


    def get_bounding_rect(selfs):
        """
                   Calculate the rectangle that borders the polygon

                   @Returns:
                       Polygon: rectangle that borders the polygon
           """
        if len(selfs._vertics) < 3:
            return None
        leftmost, rightmost, highest, lowest = selfs._vertics[0], selfs._vertics[0], selfs._vertics[0], selfs._vertics[0]
        for point in selfs._vertics:
            if point.is_left(leftmost):
                leftmost = point
            if point.is_right(rightmost):
                rightmost = point
            if point.is_above(highest):
                highest = point
            if point.is_under(lowest):
                lowest = point
        p1 = Point(leftmost.get_x(), lowest.get_y())
        p2 = Point(rightmost.get_x(), lowest.get_y())
        p3 = Point(rightmost.get_x(), highest.get_y())
        p4 = Point(leftmost.get_x(), highest.get_y())
        points = [p1, p2, p3, p4]
        rect = Polygon()
        for point in points:
            rect.add_vertex(point)
        return rect