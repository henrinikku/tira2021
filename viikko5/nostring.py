import itertools
import string


def find(s: str):
    return next(
        r
        for r in itertools.count(start=1)
        if any(
            "".join(p) not in s
            for p in itertools.permutations(string.ascii_lowercase, r)
        )
    )


if __name__ == "__main__":
    print(find("zzz"))  # 1
    print(find("aybabtu"))  # 1
    print(find("abcdefghijklmnopqrstuvwxyz"))  # 2
