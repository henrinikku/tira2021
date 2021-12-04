from collections import deque


class LongPath:
    def __init__(self, n: int):
        self.G = {i: [] for i in range(1, n + 1)}
        self.prev = {i: [] for i in range(1, n + 1)}

    def add_edge(self, a: int, b: int):
        a, b = min(a, b), max(a, b)
        self.G[a].append(b)
        self.prev[b].append(a)

    def calculate(self):
        dist = {node: 0 for node in self.G.keys()}
        for node in self.topological_sort():
            if not self.prev[node]:
                continue
            dist[node] = max(dist[prev] + 1 for prev in self.prev[node])

        return max(dist.values())

    def topological_sort(self):
        result = []
        seen = set()
        for start in self.G.keys():
            if start in seen:
                continue
            queue = deque([start])
            while queue:
                node = queue.pop()
                seen.add(node)

                neighbours = [
                    neighbour for neighbour in self.G[node] if neighbour not in seen
                ]
                if neighbours:
                    queue.append(node)
                    queue.extend(neighbours)
                else:
                    result.append(node)

        return list(reversed(result))


if __name__ == "__main__":
    l = LongPath(4)
    l.add_edge(1, 2)
    l.add_edge(1, 3)
    l.add_edge(2, 4)
    l.add_edge(3, 4)
    print(l.calculate())  # 2
    l.add_edge(3, 2)
    print(l.calculate())  # 3

    l = LongPath(50)
    l.add_edge(1, 2)
    l.add_edge(2, 3)
    l.add_edge(3, 4)
    l.add_edge(4, 5)
    l.add_edge(5, 6)
    l.add_edge(6, 7)
    l.add_edge(7, 8)
    l.add_edge(8, 9)
    l.add_edge(9, 10)
    l.add_edge(10, 11)
    l.add_edge(11, 12)
    l.add_edge(12, 13)
    l.add_edge(13, 14)
    l.add_edge(14, 15)
    l.add_edge(15, 16)
    l.add_edge(16, 17)
    l.add_edge(17, 18)
    l.add_edge(18, 19)
    l.add_edge(19, 20)
    l.add_edge(20, 21)
    l.add_edge(21, 22)
    l.add_edge(22, 23)
    l.add_edge(23, 24)
    l.add_edge(24, 25)
    l.add_edge(25, 26)
    l.add_edge(26, 27)
    l.add_edge(27, 28)
    l.add_edge(28, 29)
    l.add_edge(29, 30)
    l.add_edge(30, 31)
    l.add_edge(31, 32)
    l.add_edge(32, 33)
    l.add_edge(33, 34)
    l.add_edge(34, 35)
    l.add_edge(35, 36)
    l.add_edge(36, 37)
    l.add_edge(37, 38)
    l.add_edge(38, 39)
    l.add_edge(39, 40)
    l.add_edge(40, 41)
    l.add_edge(41, 42)
    l.add_edge(42, 43)
    l.add_edge(43, 44)
    l.add_edge(44, 45)
    l.add_edge(45, 46)
    l.add_edge(46, 47)
    l.add_edge(47, 48)
    l.add_edge(48, 49)
    l.add_edge(49, 50)
    l.add_edge(1, 3)
    l.add_edge(2, 4)
    l.add_edge(3, 5)
    l.add_edge(4, 6)
    l.add_edge(5, 7)
    l.add_edge(6, 8)
    l.add_edge(7, 9)
    l.add_edge(8, 10)
    l.add_edge(9, 11)
    l.add_edge(10, 12)
    l.add_edge(11, 13)
    l.add_edge(12, 14)
    l.add_edge(13, 15)
    l.add_edge(14, 16)
    l.add_edge(15, 17)
    l.add_edge(16, 18)
    l.add_edge(17, 19)
    l.add_edge(18, 20)
    l.add_edge(19, 21)
    l.add_edge(20, 22)
    l.add_edge(21, 23)
    l.add_edge(22, 24)
    l.add_edge(23, 25)
    l.add_edge(24, 26)
    l.add_edge(25, 27)
    l.add_edge(26, 28)
    l.add_edge(27, 29)
    l.add_edge(28, 30)
    l.add_edge(29, 31)
    l.add_edge(30, 32)
    l.add_edge(31, 33)
    l.add_edge(32, 34)
    l.add_edge(33, 35)
    l.add_edge(34, 36)
    l.add_edge(35, 37)
    l.add_edge(36, 38)
    l.add_edge(37, 39)
    l.add_edge(38, 40)
    l.add_edge(39, 41)
    l.add_edge(40, 42)
    l.add_edge(41, 43)
    l.add_edge(42, 44)
    l.add_edge(43, 45)
    l.add_edge(44, 46)
    l.add_edge(45, 47)
    l.add_edge(46, 48)
    l.add_edge(47, 49)
    l.add_edge(48, 50)
    print(l.calculate())  # 49
    l = LongPath(5)
    print(l.calculate())  # 0
    l.add_edge(3, 5)
    print(l.calculate())  # 1
    print(l.calculate())
    l.add_edge(3, 4)
    print(l.calculate())
    l.add_edge(5, 4)
    l.add_edge(1, 2)
    l.add_edge(3, 1)
    print(l.calculate())
