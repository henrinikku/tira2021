from functools import partial
from itertools import combinations
from typing import Iterable

pairs = partial(combinations, r=2)


class Rectangle:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.left = x1
        self.right = x2
        self.top = y1
        self.bottom = y2

    def area(self):
        return abs(self.left - self.right) * abs(self.top - self.bottom)

    def overlaps(self, other):
        return not (
            other.right < self.left
            or self.right < other.left
            or other.top < self.bottom
            or self.top < other.bottom
        )


def overlapping_area(rectangles: Iterable[Rectangle]):
    """
    Calculate the area where all given rectangles overlap.
    """
    if not all(a.overlaps(b) for a, b in pairs(rectangles)):
        return 0

    x = min(rec.right for rec in rectangles) - max(rec.left for rec in rectangles)
    y = min(rec.top for rec in rectangles) - max(rec.bottom for rec in rectangles)
    return x * y


def area(*args):
    recs = [Rectangle(*arg) for arg in args]
    total_area = sum(rec.area() for rec in recs)
    total_overlapping_area = sum(overlapping_area(pair) for pair in pairs(recs))
    duplicate_overlapping_area = overlapping_area(recs)
    return total_area - (total_overlapping_area - duplicate_overlapping_area)


if __name__ == "__main__":
    rec1 = (-1, 1, 1, -1)
    rec2 = (0, 3, 2, 0)
    rec3 = (0, 2, 3, -2)
    print(area(rec1, rec2, rec3))  # 16
