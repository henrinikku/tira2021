

def count(s: str):
    stack = []
    result = 0
    for c in s:
        if c == "(":
            stack.append(c)

        elif stack:
            stack.pop()
            
        else:
            result += 1

    return result + len(stack)

if __name__ == "__main__":
    print(count("(()())"))  # 0
    print(count(")))))"))  # 5
    print(count("((())("))  # 2
    print(count("(()()())()()"))  # 0
    print(count("))))))(((((("))  # 12
