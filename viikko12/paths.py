from collections import deque
from typing import List, Tuple


def count_paths(t: List[Tuple[int, int]], start: int = 1, end: int = 100):
    g = {a: [] for a in range(start, end + 1)}
    for a, b in t:
        g[a].append(b)

    paths = set()
    queue = deque([((start,), start)])
    while queue:
        path, v = queue.popleft()
        if v == end:
            paths.add(path)
        queue.extend((path + (e,), e) for e in g[v])
    return len(paths)


def create(x: int):
    if x == 1:
        return [(1, 100)]

    paths = 2
    out = [(1, 3), (3, 2), (2, 100), (3, 100)]
    mem = [(2, 1)]
    next_node, next_new_paths = None, None
    while paths < x:
        next_node = 5 if next_node is None else next_node + 2
        next_new_paths = 2 if next_new_paths is None else next_new_paths * 2
        paths += 1
        out += [(1, next_node), (next_node, 100)]
        for prev_node, new_paths in reversed(mem):
            if paths + new_paths <= x:
                paths += new_paths
                out.append((next_node, prev_node))

        mem.append((next_node, next_new_paths))

    return out


if __name__ == "__main__":
    print(count_paths(create(2)))  # esim. [(1,2),(1,100),(2,100)]
    print(count_paths(create(5)))
    print(count_paths(create(10)))
