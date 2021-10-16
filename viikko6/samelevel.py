from collections import Counter, namedtuple

Node = namedtuple("Node", ["left", "right"])


def count(node: Node, level: int):
    counter = Counter()

    def _count(current_node: Node, current_level: int):
        if current_node is None:
            return

        counter[current_level] += 1
        _count(current_node.left, current_level + 1)
        _count(current_node.right, current_level + 1)

    _count(node, 1)
    return counter[level]


if __name__ == "__main__":
    tree = Node(None, Node(Node(None, None), Node(None, None)))
    print(count(tree, 1))  # 1
    print(count(tree, 2))  # 1
    print(count(tree, 3))  # 2
    print(count(tree, 4))  # 0
