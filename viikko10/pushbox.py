from collections import deque, namedtuple
from typing import List

Graph = List[str]
State = namedtuple("State", ["my_y", "my_x", "box_y", "box_x", "steps"])

WALL = "#"
FLOOR = "."
BOX = "B"
SELF = "X"
TARGET = "Y"


class Pushbox:
    def __init__(self, r: Graph):
        self.r = r
        self.n = len(r)
        self.m = len(r[0])
        self.target = self._find(TARGET)

    def _neighbours(self, state: State):
        moves = []
        if state.my_y > 0 and self.r[state.my_y - 1][state.my_x] != WALL:
            moves.append((state.my_y - 1, state.my_x, state.box_y - 1, state.box_x))

        if state.my_x > 0 and self.r[state.my_y][state.my_x - 1] != WALL:
            moves.append((state.my_y, state.my_x - 1, state.box_y, state.box_x - 1))

        if state.my_y < self.n - 1 and self.r[state.my_y + 1][state.my_x] != WALL:
            moves.append((state.my_y + 1, state.my_x, state.box_y + 1, state.box_x))

        if state.my_x < self.m - 1 and self.r[state.my_y][state.my_x + 1] != WALL:
            moves.append((state.my_y, state.my_x + 1, state.box_y, state.box_x + 1))

        for my_y, my_x, box_y, box_x in moves:
            if (my_y, my_x) == (state.box_y, state.box_x):
                if (
                    not (box_y < 0 or box_y >= self.n or box_x < 0 or box_y >= self.m)
                    and self.r[box_y][box_x] != WALL
                ):
                    yield State(my_y, my_x, box_y, box_x, state.steps + 1)

            else:
                yield State(my_y, my_x, state.box_y, state.box_x, state.steps + 1)

    def _find(self, point: str):
        return next(
            (y, x)
            for y in range(self.n)
            for x in range(self.m)
            if self.r[y][x] == point
        )

    def _starting_point(self):
        my_y, my_x = self._find(SELF)
        box_y, box_x = self._find(BOX)
        return State(my_y, my_x, box_y, box_x, 0)

    def shortest_path_length(self):
        seen = set()
        queue = deque([self._starting_point()])
        while queue:
            state = queue.popleft()
            position = state.my_y, state.my_x, state.box_y, state.box_x
            if position in seen:
                continue
            if (state.box_y, state.box_x) == self.target:
                return state.steps
            seen.add(position)
            queue.extend(self._neighbours(state))

        return -1


def count(r: Graph):
    return Pushbox(r).shortest_path_length()


if __name__ == "__main__":
    r = [
        "########",
        "#......#",
        "#.#.Y#.#",
        "#.#B.#.#",
        "#..X.#.#",
        "#.#..#.#",
        "########",
    ]
    print(count(r))  # 18
