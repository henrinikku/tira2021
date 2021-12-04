from typing import Dict


class CycleError(BaseException):
    ...


class Cycles:
    def __init__(self, n: int):
        self.G = {i: [] for i in range(1, n + 1)}

    def add_edge(self, a: int, b: int):
        self.G[a].append(b)

    def check(self):
        done = {}
        for node in self.G.keys():
            try:
                self.traverse(node, done)
            except CycleError:
                return True
        return False

    def traverse(self, node: int, done: Dict[int, bool]):
        done[node] = False
        for neighbour in self.G[node]:
            if done.get(neighbour, True) == False:
                raise CycleError()
            else:
                self.traverse(neighbour, done)

        done[node] = True


if __name__ == "__main__":
    c = Cycles(4)
    c.add_edge(1, 2)
    c.add_edge(2, 3)
    c.add_edge(1, 3)
    c.add_edge(3, 4)
    print(c.check())  # False
    c.add_edge(4, 2)
    print(c.check())  # True
