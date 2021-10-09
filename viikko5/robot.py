def count(s: str):
    x, y = 0, 0
    visited = set([(x, y)])
    for c in s:
        if c == "L":
            x -= 1
        elif c == "R":
            x += 1
        elif c == "D":
            y -= 1
        elif c == "U":
            y += 1

        visited.add((x, y))

    return len(visited)


if __name__ == "__main__":
    print(count("LL"))  # 3
    print(count("UUDLRR"))  # 5
    print(count("UDUDUDU"))  # 2
