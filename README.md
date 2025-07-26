### Point & Polygon Geometry in Python

This project demonstrates object-oriented programming (OOP) concepts through two core geometry classes: `Point` and `Polygon`.

### `Point` Class

Represents a 2D Cartesian point with the following capabilities:

- Get/set X and Y coordinates
- Calculate distance to another point or the origin
- Check spatial relationships (above, below, left, right)
- Find the midpoint between two points
- Move the point by delta X and Y
- String representation: `(x,y)`

### `Polygon` Class

Represents a convex polygon using a list of `Point` instances. Key features include:

- Add and retrieve vertices
- Calculate perimeter and area
- Compare polygon sizes
- Find the highest vertex
- Return the bounding box
- Get next vertex in order

### Tester

Includes a `tester.py` script to validate functionality via `assert` statements.  
If all tests pass, you’ll see:

```bash
✅ All tests passed!
