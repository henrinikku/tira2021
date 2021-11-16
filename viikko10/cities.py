from collections import deque


class Cities:
    def __init__(self, n: int):
        self.graph = {city: [] for city in range(1, n + 1)}

    def add_road(self, a: int, b: int):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def has_route(self, a: int, b: int):
        seen = set()
        queue = deque(self.graph[a])
        while queue:
            city = queue.popleft()
            if city in seen:
                continue
            if city == b:
                return True
            seen.add(city)
            queue.extend(self.graph[city])
        return False


if __name__ == "__main__":
    c = Cities(5)
    c.add_road(1, 2)
    c.add_road(1, 3)
    c.add_road(4, 5)
    print(c.has_route(1, 5))  # False
    c.add_road(3, 4)
    print(c.has_route(1, 5))  # True
