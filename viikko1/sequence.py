import itertools


def generate(n):
    return next(
        itertools.islice(
            (i for i in itertools.count() if len(str(i)) != len(set(str(i)))),
            n - 1,
            None,
        )
    )


if __name__ == "__main__":
    print(generate(1))  # 11
    print(generate(2))  # 22
    print(generate(3))  # 33
    print(generate(10))  # 100
    print(generate(123))  # 505
