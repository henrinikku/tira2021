from typing import Tuple


def attacking(queen: Tuple[int, int], knight: Tuple[int, int]):
    return (
        # Same row
        queen[0] == knight[0]
        # Same col
        or queen[1] == knight[1]
        # Same diagonal
        or abs(queen[0] - knight[0]) == abs(queen[1] - knight[1])
        # Knight can attack queen
        or (
            (abs(queen[0] - knight[0]), abs(queen[1] - knight[1]))
            in ((1, 2), (2, 1))
        )
    )


def count(n: int):
    positions = [(x, y) for y in range(n) for x in range(n)]
    return sum(
        not attacking(queen, knight)
        for knight in positions
        for queen in positions
    )


if __name__ == "__main__":
    print(count(3))  # 0
    print(count(4))  # 40
    print(count(5))  # 184
