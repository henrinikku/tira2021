from collections import Counter
from typing import List


def count(t: List[int], k: int):
    left_iter, right_iter = map(iter, [range(len(t) - k + 1), range(k - 1, len(t))])
    window = Counter(t[next(left_iter) : next(right_iter) + 1])
    out = [len(window)]
    for left, right in zip(left_iter, right_iter):
        if window[t[left - 1]] == 1:
            window.pop(t[left - 1])
        else:
            window[t[left - 1]] -= 1

        window[t[right]] += 1
        out.append(len(window))

    return out


if __name__ == "__main__":
    print(count([1, 1, 2, 2], 2))  # [1,2,1]
    print(count([1, 1, 1, 1], 4))  # [1]
    print(count([1, 2, 3, 2, 2, 2], 3))  # [3,2,2,1]
