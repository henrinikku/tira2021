import itertools


def create(s: int):
    return sorted(list(set(map("".join, itertools.permutations(s)))))


if __name__ == "__main__":
    print(create("ab"))  # [ab,ba]
    print(
        create("abac")
    )  # [aabc,aacb,abac,abca,acab,acba,baac,baca,bcaa,caab,caba,cbaa]
    print(len(create("aybabtu")))  # 1260
