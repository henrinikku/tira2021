def calculate(s: str):
    distance = 0
    occurrences = 0
    result = 0
    for i, c in enumerate(s):
        if c == "1":
            result += (occurrences * i) - distance
            occurrences += 1
            distance += i

    return result


if __name__ == "__main__":
    print(calculate("10110"))  # 6
    print(calculate("10"))  # 0
    print(calculate("10010110"))  # 20
    print(calculate("0011110111101010"))  # 214
