def create(n):
    left = sorted(range(1, n + 1, 2), reverse=True)
    right = list(range(2, n + 1, 2))
    return left + right

if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(2)) # [1,2]
    print(create(3)) # [3,1,2]
    print(create(4)) # [3,1,2,4]
    print(create(5)) # [5,3,1,2,4]