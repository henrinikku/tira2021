import itertools


class Mex:
    def __init__(self):
        self.smallest = 0
        self.nums = set()

    def add(self, x):
        self.nums.add(x)
        if x == self.smallest:
            self.smallest = next(i for i in itertools.count(x) if i not in self.nums)
        return self.smallest


if __name__ == "__main__":
    m = Mex()
    print(m.add(1))  # 0
    print(m.add(3))  # 0
    print(m.add(4))  # 0
    print(m.add(0))  # 2
    print(m.add(5))  # 2
    print(m.add(2))  # 6
