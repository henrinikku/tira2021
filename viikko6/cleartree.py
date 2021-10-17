import operator
import functools
from collections import Counter, namedtuple

Node = namedtuple("Node", ["left", "right"])


def mul(n: int):
    return functools.reduce(operator.mul, range(1, n + 1))


def calc(a, b: int):
    return mul(a) // (mul(b) * mul(a - b))


def _count(node: Node):
    if node.left is None and node.right is None:
        return 1, 1

    if node.left:
        left = _count(node.left)
    else:
        left = 0, 0

    if node.right:
        right = _count(node.right)
    else:
        right = 0, 0

    cnt = left[0] + right[0]
    if node.left and node.right:
        return cnt + 1, calc(cnt, max(left[0], right[0])) * left[1] * right[1]

    elif right[0]:
        return cnt + 1, right[1]

    else:
        return cnt + 1, left[1]


def count(node: Node):
    return int(_count(node)[1])


if __name__ == "__main__":
    tree = Node(Node(None, None), Node(Node(None, None), Node(None, None)))
    print(count(tree))  # 8
    print(
        count(
            Node(
                left=Node(
                    left=Node(left=None, right=None),
                    right=Node(
                        left=Node(left=None, right=None),
                        right=Node(
                            left=Node(
                                left=None,
                                right=Node(
                                    left=None, right=Node(left=None, right=None)
                                ),
                            ),
                            right=None,
                        ),
                    ),
                ),
                right=Node(
                    left=Node(
                        left=Node(
                            left=Node(
                                left=Node(left=None, right=None),
                                right=Node(
                                    left=Node(left=None, right=None), right=None
                                ),
                            ),
                            right=Node(left=None, right=None),
                        ),
                        right=Node(
                            left=Node(
                                left=None,
                                right=Node(
                                    left=Node(left=None, right=None),
                                    right=Node(
                                        left=None, right=Node(left=None, right=None)
                                    ),
                                ),
                            ),
                            right=Node(left=Node(left=None, right=None), right=None),
                        ),
                    ),
                    right=Node(
                        left=Node(left=None, right=Node(left=None, right=None)),
                        right=None,
                    ),
                ),
            )
        )
    )  # 179933898714570000
