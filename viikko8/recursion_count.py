class Counter:
    def __init__(self):
        self.count = 0


def f(n: int, counter: Counter):
    counter.count += 1
    if n <= 2:
        return n
    return f(n - 1, counter) + f(n - 2, counter) + f(n - 3, counter)


if __name__ == "__main__":
    counter = Counter()
    result = f(30, counter)
    print(f"Result = {result}. Function f was called {counter.count} times")
