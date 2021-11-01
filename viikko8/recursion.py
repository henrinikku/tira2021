import timeit

def f(n):
    if n <= 2:
        return n
    return f(n - 1) + f(n - 2) + f(n - 3)

if __name__ == "__main__":
    start = timeit.default_timer()
    result = f(30)
    end = timeit.default_timer()
    print(f"Result = {result}, took {end - start} seconds.")