from collections import namedtuple

Node = namedtuple("Node", ["left", "right"])


def same(a: Node, b: Node):
    return (a is None and b is None) or (
        a is not None
        and b is not None
        and same(a.left, b.left)
        and same(a.right, b.right)
    )


if __name__ == "__main__":
    tree1 = Node(None, Node(Node(None, None), Node(None, None)))
    tree2 = Node(Node(Node(None, None), Node(None, None)), None)
    tree3 = Node(None, Node(Node(None, None), Node(None, None)))
    print(same(tree1, tree2))  # False
    print(same(tree1, tree3))  # True
    print(same(tree2, tree3))  # False
