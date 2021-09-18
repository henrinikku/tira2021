def count(s: str):
    chars = {}
    for c in s:
        chars[c] = chars.get(c, 0) + 1

    return sum((n * (n + 1)) / 2 for n in chars.values())


if __name__ == "__main__":
    print(count("aaa"))  # 6
    print(count("abcd"))  # 4
    print(count("ababca"))  # 10
