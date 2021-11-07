def _create(n: int, s: str):
    if len(s) == n:
        yield s
    else:
        for c in "ABC":
            if not s or c != s[-1]:
                yield from _create(n, s + c)


def create(n: int):
    return list(_create(n, ""))


if __name__ == "__main__":
    print(create(1))  # [A,B,C]
    print(create(2))  # [AB,AC,BA,BC,CA,CB]
    print(len(create(5)))  # 48
