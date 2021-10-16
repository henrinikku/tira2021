from collections import namedtuple

Node = namedtuple("Node", ["left", "right"])


def count(node: Node):
    raise NotImplementedError()


if __name__ == "__main__":
    tree = Node(Node(None, None), Node(Node(None, None), Node(None, None)))
    print(count(tree))  # 8
