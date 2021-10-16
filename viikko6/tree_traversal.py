from collections import namedtuple
from typing import List

Node = namedtuple("Node", ["value", "left", "right"])


def construct_tree(preorder: List, inorder: List):
    if not (preorder and inorder):
        return None

    current = preorder.pop(0)
    index = inorder.index(current)
    return Node(
        current,
        construct_tree(preorder, inorder[0:index]),
        construct_tree(preorder, inorder[index + 1 :]),
    )


def traverse(node: Node):
    if node is None:
        return

    yield from traverse(node.left)
    yield from traverse(node.right)
    yield node.value


if __name__ == "__main__":
    tree = construct_tree(
        [6, 10, 12, 4, 5, 2, 1, 7, 11, 3, 8, 9],
        [4, 12, 5, 10, 6, 7, 1, 11, 8, 3, 2, 9],
    )
    print(list(traverse(tree)))
