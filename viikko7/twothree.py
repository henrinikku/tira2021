import heapq


def smallest(n: int):
    heap = [1]
    for __ in range(n):
        smallest = heapq.heappop(heap)
        heapq.heappush(heap, smallest * 2)
        heapq.heappush(heap, smallest * 3)
    return heapq.heappop(heap)


if __name__ == "__main__":
    print(smallest(1))  # 2
    print(smallest(5))  # 6
    print(smallest(123))  # 288
    print(smallest(55555))  # 663552
