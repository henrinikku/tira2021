from typing import List


def find(t: List[int]):
    longest = [1] * len(t)
    for i in range(len(t)):
        for j in range(i):
            if abs(t[j] - t[i]) == 1:
                longest[i] = max(longest[i], longest[j] + 1)
    return max(longest)


if __name__ == "__main__":
    print(find([1, 2, 3, 4, 5]))  # 5
    print(find([5, 5, 5, 5, 5]))  # 1
    print(find([5, 2, 3, 8, 2, 4, 1]))  # 4
