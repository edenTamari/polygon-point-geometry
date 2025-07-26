import math
from Point import Point


def main():
    # Test __init__
    p1 = Point(2, 3)
    p2 = Point()
    assert p1._x == 2 and p1._y == 3, f"Expected (2, 3), got ({p1._x}, \
        {p1._y})"
    assert p2._x == 0 and p2._y == 0, f"Expected (0, 0), got ({p2._x}, \
        {p2._y})"

    # Test get_x and get_y
    assert p1.get_x() == 2, f"Expected 2, got {p1.get_x()}"
    assert p1.get_y() == 3, f"Expected 3, got {p1.get_y()}"

    # Test set_x and set_y
    p1.set_x(5)
    p1.set_y(6)
    assert p1._x == 5, f"Expected 5, got {p1._x}"
    assert p1._y == 6, f"Expected 6, got {p1._y}"

    # Test __str__
    assert str(p1) == "(5,6)", f"Expected '(5,6)', got {str(p1)}"
    assert str(p2) == "(0,0)", f"Expected '(0,0)', got {str(p2)}"

    # Test __eq__
    p3 = Point(5, 6)
    assert p1 == p3, f"Expected True, got {p1 == p3}"
    assert p1 != p2, f"Expected False, got {p1 != p2}"

    # Test is_above
    assert p1.is_above(p2), f"Expected True, got {p1.is_above(p2)}"
    assert not p2.is_above(p1), f"Expected False, got {not p2.is_above(p1)}"

    # Test is_under
    assert p2.is_under(p1), f"Expected True, got {p2.is_under(p1)}"
    assert not p1.is_under(p2), f"Expected False, got {not p1.is_under(p2)}"

    # Test is_left
    p4 = Point(7, 6)
    assert p1.is_left(p4), f"Expected True, got {p1.is_left(p4)}"
    assert not p4.is_left(p1), f"Expected False, got {not p4.is_left(p1)}"

    # Test is_right
    assert p4.is_right(p1), f"Expected True, got {p4.is_right(p1)}"
    assert not p1.is_right(p4), f"Expected False, got {not p1.is_right(p4)}"

    # Test distance
    assert p1.distance(p2) == math.sqrt(61), f"Expected {math.sqrt(61)}, got \
        {p1.distance(p2)}"
    assert p2.distance(p1) == math.sqrt(61), f"Expected {math.sqrt(61)}, got \
        {p2.distance(p1)}"

    # Test distance00
    assert p1.distance00() == math.sqrt(61), f"Expected {math.sqrt(61)}, got \
        {p1.distance00()}"
    assert p2.distance00() == 0, f"Expected 0, got {p2.distance00()}"

    # Test middle
    assert p1.middle(p2) == Point(2.5, 3.0), f"Expected (2.5, 3.0), got \
        {p1.middle(p2)}"
    assert p2.middle(p1) == Point(2.5, 3.0), f"Expected (2.5, 3.0), got \
        {p2.middle(p1)}"

    # Test move
    p1.move(1, -1)
    assert p1._x == 6 and p1._y == 5, f"Expected (6, 5), got \
        ({p1._x}, {p1._y})"
    p2.move(-1, 1)
    assert p2._x == -1 and p2._y == 1, f"Expected (-1, 1), got \
        ({p2._x}, {p2._y})"
    print("All tests passed!")

if __name__ == "__main__":
    main()
