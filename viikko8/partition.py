from typing import List


def check(t: List[int], selected: List[bool] = []):
    if len(t) == len(selected):
        a = [t[i] for i in range(len(t)) if selected[i]]
        b = [t[i] for i in range(len(t)) if not selected[i]]
        return sum(a) == sum(b)

    return check(t, selected + [False]) or check(t, selected + [True])


if __name__ == "__main__":
    print(check([3, 4, 5]))  # False
    print(check([16, 8, 4, 4]))  # True
    print(check([9, 4, 8, 7, 6]))  # True
    print(check([1, 2, 3, 4, 5, 6]))  # False
    print(check([1, 2, 3, 4, 5, 6, 7]))  # True
    print(check([4, 4, 4, 6, 6]))  # True
