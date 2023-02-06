def isValid(s):
    if len(s) == 0:
        return True
    if len(s) % 2 != 0:
        return False
    while True:
        old = s
        s = s.replace("()", "")
        s = s.replace("{}", "")
        s = s.replace("[]", "")
        if old == s:
            return s == ""


if __name__ == '__main__':
    print(isValid("(]"))  # False
    print(isValid("([)]{}"))  # False
    print(isValid("()"))  # True
    print(isValid("()[]{}"))  # True
    print(isValid("([])"))  # True
