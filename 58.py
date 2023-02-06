def lengthOfLastWord(s: str) -> int:
    s = s.strip()
    a = s.split()
    return len(a[len(a) - 1])


if __name__ == '__main__':
    print(lengthOfLastWord("hello world"))