from typing import List


def check(t: List[int]):
    stack = []
    result = []
    for i in t:
        if (i - 1) == len(result):
            result.append(i)
        else:
            stack.append(i)

        while stack and result and stack[-1] == (result[-1] + 1):
            result.append(stack.pop())

    return not stack


if __name__ == "__main__":
    print(check([1, 2, 3, 4]))  # True
    print(check([4, 3, 2, 1]))  # True
    print(check([3, 4, 1, 2]))  # False
    print(check([1]))  # True
    print(check([5, 4, 3, 1, 2, 6]))  # True
