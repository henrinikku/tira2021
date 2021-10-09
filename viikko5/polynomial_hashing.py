STRINGS = [
    "maanantai",
    "tiistai",
    "keskiviikko",
    "torstai",
    "perjantai",
    "lauantai",
    "sunnuntai",
]

A = 19
N = 10 ** 6


def hash(s: str):
    return sum((A ** (len(s) - i - 1)) * ord(c) for i, c in enumerate(s)) % N


if __name__ == "__main__":
    print(*[(s, hash(s)) for s in STRINGS], sep="\n")
