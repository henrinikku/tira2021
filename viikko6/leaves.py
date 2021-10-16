from collections import namedtuple

Node = namedtuple("Node", ["left", "right"])


def count(node: Node):
    if node is None:
        return 0

    elif node.left is None and node.right is None:
        return 1

    else:
        return count(node.left) + count(node.right)


if __name__ == "__main__":
    tree = Node(
        None,
        Node(
            Node(None, None),
            Node(None, None),
        ),
    )
    print(count(tree))  # 2
