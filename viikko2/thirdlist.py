from typing import List


def create(a: List[int], b: List[int]):
    c = list(range(1, len(a) + 1))
    not_working = []
    for i in range(len(a)):
        if c[i] in (a[i], b[i]):
            not_working.append(i)

    found = False
    while not found and not_working:
        for index, not_found_i in enumerate(not_working):
            for i in range(len(a)):
                if (
                    i != not_found_i
                    and c[not_found_i] not in (a[i], b[i])
                    and c[i] not in (a[not_found_i], b[not_found_i])
                ):
                    c[i], c[not_found_i] = c[not_found_i], c[i]
                    found = True
                    break

        if not found:
            other_i = not_working[(index + 1) % len(not_working)]
            c[not_found_i], c[other_i] = c[other_i], c[not_found_i]

    return c


if __name__ == "__main__":
    create(
        [2, 4, 3, 5, 6, 7, 1],
        [5, 2, 7, 1, 4, 6, 3],
    )
    create(
        [3, 5, 4, 2, 1],
        [1, 2, 3, 5, 4],
    )
    create(
        [3, 4, 2, 1],
        [2, 3, 1, 4],
    )
    create(
        [1, 2, 3],
        [3, 1, 2],
    )
    create(
        [1, 3, 2, 4],
        [4, 1, 3, 2],
    )
    create(
        [1, 7, 3, 6, 2, 8, 4, 5],
        [6, 1, 5, 4, 3, 2, 7, 8],
    )
    create(
        [1, 2, 5, 4, 3],
        [5, 4, 3, 1, 2],
    )
    create(
        [1, 3, 4, 2],
        [2, 4, 3, 1],
    )
