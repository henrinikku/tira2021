from collections import deque


def solve(n: int, k: int):
    l = deque(range(1, n + 1))
    for _ in range(k):
        a, b = l.popleft(), l.popleft()
        l.extend([b, a])
    return l.popleft()


if __name__ == "__main__":
    print(solve(4, 3))  # 4
    print(solve(12, 5))  # 11
    print(solve(99, 555))  # 11
    print(solve(12345, 54321))  # 9875
