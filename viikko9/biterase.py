from functools import lru_cache


@lru_cache(None)
def count(s: str):
    if len(s) == 0:
        return 1
    if len(s) % 2 != 0:
        return 0
    return sum(
        count(
            s[:i] + s[i + 2 :],
        )
        for i in range(len(s) - 1)
        if s[i] == s[i + 1]
    )


if __name__ == "__main__":
    print(count("1100"))  # 2
    print(count("1001"))  # 1
    print(count("100111"))  # 5
    print(count("11001"))  # 0
    print(count("1100110011100111"))  # 113925
