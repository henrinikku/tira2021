from collections import Counter, namedtuple

Node = namedtuple("Node", ["left", "right"])


def _diff(node: Node):
    if node is None:
        return 0, 0

    left_count, left_diff = _diff(node.left)
    right_count, right_diff = _diff(node.right)
    return (
        left_count + right_count + 1,
        max(left_diff, right_diff, abs(left_count - right_count)),
    )


def diff(node: Node):
    return _diff(node)[1]


if __name__ == "__main__":
    tree = Node(None, Node(Node(None, None), Node(None, None)))
    print(diff(tree))  # 3
