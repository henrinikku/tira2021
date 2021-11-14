def count(n: int, a: int, b: int):
    [a, b] = sorted((a, b))

    # Up to a
    mem = [0 for _ in range(a)]
    mem += [1]

    # Up to b
    mem += [1 if i % a == 0 else 0 for i in range(a + 1, b)]
    mem += [2 if b % a == 0 else 1]

    # Up to n
    for i in range(b + 1, n + 1):
        mem.append(mem[i - a] + mem[i - b])

    return mem[n]


if __name__ == "__main__":
    print(count(3, 1, 3))  # 2
    print(count(4, 1, 2))  # 5
    print(count(10, 2, 5))  # 2
    print(count(10, 6, 7))  # 0
    print(count(30, 3, 5))  # 58
    print(count(50, 2, 3))  # 525456
