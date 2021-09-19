from typing import List


def find(t: List[int]):
    return max(t) - min(t)

if __name__ == "__main__":
    print(find([4,5,2,1,2])) # 4
    print(find([1,2,3,4])) # 3
    print(find([1])) # 0
    print(find([1,2,100,5])) # 99