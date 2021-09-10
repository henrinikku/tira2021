
def count(n):
    return sum(not any(i % j == 0 for j in range(2, i)) for i in range(2, n + 1))


if __name__ == "__main__":
    print(count(2))  # 1
    print(count(10))  # 4
    print(count(11))  # 5
    print(count(100))  # 25
    print(count(1000))  # 168
