from collections import Counter
from operator import itemgetter

class Mode:
    def __init__(self):
        self.counter = Counter()
        self.mode = 0

    def add(self, x):
        self.mode = self.mode or x
        self.counter[x] += 1

        if self.counter[self.mode] < self.counter[x]:
            self.mode = x
            
        elif self.counter[self.mode] == self.counter[x]:
            self.mode = min(self.mode, x)
        
        return self.mode

if __name__ == "__main__":
    m = Mode()
    print(m.add(1))  # 1
    print(m.add(2))  # 1
    print(m.add(2))  # 2
    print(m.add(1))  # 1
    print(m.add(3))  # 1
    print(m.add(3))  # 1
    print(m.add(3))  # 3
