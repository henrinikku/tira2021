import time
import random
from typing import Callable


def slow(s: str):
    n = len(s)
    return sum(
        s[i] == "0" and s[j] == "1" for i in range(0, n - 1) for j in range(i, n - 1)
    )


def fast(s: str):
    count = 0
    zeroes = 0
    for i in range(len(s) - 1):
        if s[i] == "0":
            zeroes += 1
        else:
            count += zeroes
    return count


def time_it(fn: Callable[[str], int], s: str):
    start_time = time.time()
    fn(s)
    end_time = time.time()
    print(f"{fn.__name__}: aikaa kului {end_time - start_time} kun n = {len(s)}")


def generate_input(n: int):
    s = ""
    for _ in range(0, n):
        s += str(random.randint(0, 1))
    return s


if __name__ == "__main__":
    for exponent in range(1, 6):
        s = generate_input(10 ** exponent)
        # time_it(slow, s)
        time_it(fast, s)
