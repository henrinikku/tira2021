from typing import List


def check(t: List[int]):
    left_cursor = 0
    right_cursor = len(t) - 1
    while left_cursor < right_cursor:
        if not (
            (t[left_cursor] < t[left_cursor + 1])
            == (t[right_cursor - 1] < t[right_cursor])
        ):
            return False

        if not (
            (t[left_cursor] == left_cursor + 1) == (t[right_cursor] == right_cursor + 1)
        ):
            return False

        left_cursor += 1
        right_cursor -= 1

    half = len(t) // 2
    if t[half - 1] + 1 == t[half] and t[half - 1] != half:
        return False

    return True


if __name__ == "__main__":
    print(check([3, 1, 4, 2]))  # True
    print(check([3, 1, 2, 4]))  # False
    print(check([1, 2]))  # True
    print(check([4, 5, 6, 1, 2, 3]))  # True
    print(check([4, 5, 6, 3, 2, 1]))  # False
    print(check([5, 8, 13, 1, 3, 6, 11, 4, 9, 12, 14, 2, 7, 10]))  # True
    print(check([8, 7, 3, 4, 5, 6, 2, 1]))  # True
    print(
        check([6, 20, 8, 4, 18, 11, 19, 5, 9, 7, 14, 12, 16, 2, 10, 3, 17, 13, 1, 15])
    )  # True
    print(check([5, 7, 4, 3, 8, 2, 6, 1]))  # False
    print(
        check([14, 5, 6, 8, 15, 18, 12, 9, 4, 13, 1, 10, 11, 7, 16, 2, 17, 3])
    )  # False
    print(check([2, 3, 7, 6, 5, 1, 4, 8]))  # False
    print(check([3, 1, 4, 5, 6, 2]))  # False WRONG
    # print(check([3, 4, 5, 6, 2, 1]))  # ?

    # print_permutations([1, 2, 3, 4, 5, 6], 10000)
