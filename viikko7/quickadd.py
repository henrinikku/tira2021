import heapq
from typing import List, Tuple

class QuickAdd:
    def __init__(self):
        self.heap: List[Tuple[int, int]] = []

    def add(self, k, x):
        heapq.heappush(self.heap, (x, k))

    def remove(self, k):
        out = 0
        while k > 0:
            cur_x, cur_k = heapq.heappop(self.heap)
            taken = min(k, cur_k)
            out += taken * cur_x
            k -= taken
            cur_k -= taken
            if cur_k:
                heapq.heappush(self.heap, (cur_x, cur_k))

        return out


if __name__ == "__main__":
    q = QuickAdd()
    q.add(5, 3)
    print(q.remove(2))  # 6
    q.add(8, 1)
    print(q.remove(4))  # 4
    print(q.remove(7))  # 13
    q.add(10 ** 9, 123)
    print(q.remove(10 ** 9))  # 123000000000
