from collections import deque


class Network:
    def __init__(self, n: int):
        self.graph = {node: [] for node in range(1, n + 1)}

    def add_link(self, a: int, b: int):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def best_route(self, a: int, b: int):
        seen = set()
        queue = deque((node, 1) for node in self.graph[a])
        while queue:
            node, length = queue.popleft()
            if node in seen:
                continue
            if node == b:
                return length
            seen.add(node)
            queue.extend((neighbour, length + 1) for neighbour in self.graph[node])
        return -1


if __name__ == "__main__":
    w = Network(5)
    w.add_link(1, 2)
    w.add_link(2, 3)
    w.add_link(1, 3)
    w.add_link(4, 5)
    print(w.best_route(1, 5))  # -1
    w.add_link(3, 5)
    print(w.best_route(1, 5))  # 2
