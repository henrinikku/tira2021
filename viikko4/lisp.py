from collections import deque
from functools import reduce
from operator import add, mul
from typing import Callable, Deque, Dict, Iterable


OPERATOR_MAP: Dict[str, Callable[[int, int], int]] = {
    "+": add,
    "*": mul,
}


def _eval(tokens: Deque[str]):
    token = tokens.popleft()

    if token == "(":
        operator = OPERATOR_MAP[tokens.popleft()]
        values = []
        while tokens and tokens[0] != ")":
            values.append(_eval(tokens))
        tokens.popleft()
        return reduce(operator, values)

    else:
        return int(token)


def eval(s: str):
    tokens = s.replace("(", " ( ").replace(")", " ) ").split()
    return _eval(deque(tokens))


if __name__ == "__main__":
    print(eval("(+ 1 2 3 4 5)"))  # 15
    print(eval("(+ 5 (* 3 2) 7)"))  # 18
    print(eval("(* (+ (+ 1 2) 3) (+ (* 4 5) 6 2))"))  # 168
