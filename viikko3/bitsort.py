def solve(s: str):
    ones = 0
    result = 0
    for c in s:
        if c == "1":
            ones += 1
        else:
            result += ones
    return result


if __name__ == "__main__":
    print(solve("000100"))  # 2
    print(solve("111000"))  # 9
    print(solve("101010"))  # 6
