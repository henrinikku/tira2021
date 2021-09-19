def _count(s: str, n: int):
    char_count = {}
    result = 0
    subs_i = 0
    subs_l = n
    for i, c in enumerate(s):
        if char_count.get(c, 0) == 0:
            subs_l -= 1

        char_count[c] = char_count.get(c, 0) + 1

        while subs_l < 0:
            subs_c = s[subs_i]
            char_count[subs_c] = char_count.get(subs_c, 0) - 1
            if char_count[subs_c] == 0:
                subs_l += 1

            subs_i += 1

        result += i - subs_i + 1

    return result


def count(s: str):
    return _count(s, 2) - _count(s, 1)


if __name__ == "__main__":
    print(count("aaaa"))  # 0
    print(count("abab"))  # 6
    print(count("aabacba"))  # 8
    print(count("abacaadbaacaa"))  # 21
