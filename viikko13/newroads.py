import heapq

class NewRoads:
    def __init__(self, n: int):
        self.n = n
        self.edges = []

    def root(self, x: int):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def add_road(self, a: int, b: int, x: int):
        heapq.heappush(self.edges, (x, a, b))

    def connect(self, a: int, b: int):
        a, b = self.root(a), self.root(b)
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]

    def min_cost(self):
        self.parent = {x: x for x in range(1, self.n + 1)}
        self.size = {x: 0 for x in range(1, self.n + 1)}

        total_cost = 0
        edges = self.edges.copy()
        while edges:
            x, a, b = heapq.heappop(edges)
            if self.root(a) != self.root(b):
                total_cost += x
                self.connect(a, b)

        if sum(k == v for k, v in self.parent.items()) > 1:
            return -1
        
        return total_cost



if __name__ == "__main__":
    n = NewRoads(4)
    n.add_road(1, 2, 2)
    n.add_road(1, 3, 5)
    print(n.min_cost())  # -1
    n.add_road(3, 4, 4)
    print(n.min_cost())  # 11
    n.add_road(2, 3, 1)
    print(n.min_cost())  # 7
