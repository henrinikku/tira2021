from collections import namedtuple
from typing import List
from string import ascii_uppercase


Point = namedtuple("Point", ["y", "x"])
Matrix = List[List[str]]


def print_matrix(matrix: Matrix):
    out = [" ".join([col if col else "." for col in row]) for row in matrix]
    print(*out, sep="\n")
    print("-----------------")


def fill_matrix(
    n: int, m: int, y: int, x: int, point: Point, fill: str, matrix: Matrix
):
    return [
        [
            matrix[row][col]
            or (
                fill
                if (
                    point.x <= col
                    and point.y <= row
                    and point.x + x >= col
                    and point.y + y >= row
                )
                else ""
            )
            for col in range(m)
        ]
        for row in range(n)
    ]


def count(n: int, m: int, k: int):
    out = [0]
    alphabet = "".join(reversed(ascii_uppercase[:k]))
    initial_matrix = [["" for col in range(m)] for row in range(n)]

    def search(n: int, m: int, k: int, matrix: Matrix):
        # Get the top-leftmost empty point
        point = next(
            (
                Point(row, col)
                for row in range(n)
                for col in range(m)
                if not matrix[row][col]
            ),
            None,
        )

        if point is None:
            out[0] += 1
            return

        if k == 0:
            return

        # Try all rectangles starting from point
        end_y = n - point.y
        end_x = m - point.x
        for y in range(end_y):
            for x in range(end_x):
                if matrix[y + point.y][x + point.x]:
                    end_x = x
                    break

                filled = fill_matrix(n, m, y, x, point, alphabet[k - 1], matrix)
                search(n, m, k - 1, filled)

    search(n, m, k, initial_matrix)
    return out[0]


if __name__ == "__main__":
    print(count(2, 2, 4))  # 8
    print(count(2, 3, 3))  # 13
    print(count(4, 4, 1))  # 1
    print(count(3, 3, 6))  # 259
    print(count(4, 3, 10))  # 3146
    print(count(4, 4, 16))  # 70878
