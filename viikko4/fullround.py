def count(n: int):
    if n % 2 == 0:
        return n
    else:
        return (n // 2) * ((n + 1) // 2)


if __name__ == "__main__":
    print(count(2))  # 2
    print(count(4))  # 4
    print(count(5))  # 6
    print(count(31))  # 240
    print(count(1234567))  # 381038919372
