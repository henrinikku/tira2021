import heapq
from collections import namedtuple

Task = namedtuple("Task", ["priority", "name"])


class Tasks:
    def __init__(self):
        self.heap = []

    def add(self, name, priority):
        heapq.heappush(self.heap, Task(-1 * priority, name))

    def next(self):
        return heapq.heappop(self.heap).name


if __name__ == "__main__":
    t = Tasks()
    t.add("siivous", 10)
    t.add("ulkoilu", 50)
    t.add("opiskelu", 50)
    print(t.next())  # opiskelu
    t.add("treffit", 100)
    print(t.next())  # treffit
    print(t.next())  # ulkoilu
