def count(s: str):
    curr = ""
    result = 0
    for c in s:
        if curr and curr[0] == c:
            curr += c
        else:
            result += (len(curr) * (len(curr) + 1)) / 2
            curr = c
    
    return result + (len(curr) * (len(curr) + 1)) / 2

if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5