from collections import deque


class FlipList:
    def __init__(self):
        self.deque = deque()
        self.flipped = False

    def push_last(self, x):
        if self.flipped:
            self.deque.appendleft(x)
        else:
            self.deque.append(x)

    def push_first(self, x):
        if self.flipped:
            self.deque.append(x)
        else:
            self.deque.appendleft(x)

    def pop_last(self):
        if self.flipped:
            return self.deque.popleft()
        else:
            return self.deque.pop()

    def pop_first(self):
        if self.flipped:
            return self.deque.pop()
        else:
            return self.deque.popleft()

    def flip(self):
        self.flipped = not self.flipped


if __name__ == "__main__":
    f = FlipList()
    f.push_last(1)
    f.push_last(2)
    f.push_last(3)
    print(f.pop_first())  # 1
    f.flip()
    print(f.pop_first())  # 3
