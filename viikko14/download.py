from collections import deque


class Download:
    def __init__(self, n):
        self.n = n
        self.adjacent = {i: [] for i in range(self.n)}
        self.capacity = [[0] * self.n for _ in range(self.n)]

    def add_link(self, a, b, x):
        a, b = a - 1, b - 1
        self.adjacent[a].append(b)
        self.capacity[a][b] += x

    def calculate(self, a, b):
        a, b = a - 1, b - 1
        flow = 0
        self.flow = [[0] * self.n for _ in range(self.n)]
        path_flow, path = self._find_path(a, b)
        while path_flow:
            node = b
            while node != a:
                self.flow[path[node]][node] += path_flow
                self.flow[node][path[node]] -= path_flow
                node = path[node]

            flow += path_flow
            path_flow, path = self._find_path(a, b)

        return flow

    def _find_path(self, a, b):
        path = [None] * self.n
        path_flow = [2 ** 63] * self.n
        queue = deque([a])
        while queue:
            node = queue.popleft()
            if node == b:
                return path_flow[node], path

            for v in self.adjacent[node]:
                if path[v] is not None:
                    continue

                weight = self.capacity[node][v] - self.flow[node][v]
                if weight <= 0:
                    continue

                path[v] = node
                path_flow[v] = min(path_flow[node], weight)
                queue.append(v)

        return 0, []


if __name__ == "__main__":
    d = Download(4)
    print(d.calculate(1, 4))  # 0
    d.add_link(1, 2, 5)
    d.add_link(2, 4, 6)
    d.add_link(1, 4, 2)
    print(d.calculate(1, 4))  # 7
    d.add_link(1, 3, 4)
    d.add_link(3, 2, 2)
    print(d.calculate(1, 4))  # 8

    d = Download(5)
    print(d.calculate(3, 4))
    d.add_link(5, 3, 6)
    print(d.calculate(5, 4))
    print(d.calculate(4, 5))
    print(d.calculate(5, 1))
    d.add_link(5, 4, 9)
    d.add_link(1, 2, 10)
    print(d.calculate(3, 1))
    print(d.calculate(2, 4))
    print(d.calculate(5, 4))
    d.add_link(5, 2, 9)
    print(d.calculate(1, 5))
    d.add_link(3, 5, 2)
    d.add_link(1, 3, 2)
    d.add_link(5, 4, 9)
    print(d.calculate(5, 4))  # 18
#    print(d.calculate(2,3))
#    print(d.calculate(1,3))
#    print(d.calculate(3,2))
#    print(d.calculate(5,4))
#    print(d.calculate(4,5))
#    d.add_link(4,3,9)
#    print(d.calculate(4,5))
#    print(d.calculate(2,4))
#    print(d.calculate(4,5))
#    d.add_link(5,1,6)
#    d.add_link(3,5,3)
#    d.add_link(4,5,2)
#    print(d.calculate(3,4))
#    d.add_link(5,3,3)
