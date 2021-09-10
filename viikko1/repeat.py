
def find(s: str):
    result = (s * 2).find(s, 1)
    return result if result > 0 else len(s)


if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7