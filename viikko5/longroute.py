def _add_step(c: str, x: int, y: int, visited: set):
    if c == "L":
        x -= 1
    elif c == "R":
        x += 1
    elif c == "D":
        y -= 1
    elif c == "U":
        y += 1

    visited.add((x, y))
    return x, y, visited


def count(s: str, k: int):
    x, y = 0, 0
    visited = set([(x, y)])
    lengths = []
    test_tries = max(len(s), 2)
    for i, c in enumerate(s * test_tries):
        x, y, visited = _add_step(c, x, y, visited)
        if i <= 0 or i % len(s) == 0:
            lengths.append(len(visited))

    per_round = lengths[-1] - lengths[-2]
    return len(visited) + (per_round * (k - test_tries))


if __name__ == "__main__":
    print(count("UR", 100), 201)  # 201
    print(count("UD", 100), 2)  # 2
    print(count("UURRDDL", 500), 1506)  # 1506
    print(count("UUDLRR", 50), 152)  # 152
    print(count("L", 10 ** 9), 1000000001)  # 1000000001
    print(count("DLUR", 10 ** 9), 4)  # 4
