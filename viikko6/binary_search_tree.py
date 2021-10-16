import random
from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def add(node: Node[T], value: T):
    if node is None:
        return Node(value)

    elif value < node.value:
        node.left = add(node.left, value)

    elif node.value < value:
        node.right = add(node.right, value)

    return node


def height(node: Optional[Node]) -> int:
    if node is None:
        return -1
    else:
        return 1 + max(map(height, [node.left, node.right]))


class BinarySearchTree(Generic[T]):
    def __init__(self, *args):
        self.root: Optional[Node] = None
        if args:
            self.extend(args)

    def add(self, value: T):
        self.root = add(self.root, value)

    def extend(self, values: List[T]):
        for value in values:
            self.add(value)

    def height(self):
        return height(self.root)


if __name__ == "__main__":
    nums = list(range(1, 10 ** 5 + 1))
    random.shuffle(nums)
    tree = BinarySearchTree(*nums)
    print("Height is:", tree.height())
