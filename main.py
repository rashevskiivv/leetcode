if __name__ == '__main__':
    s = 'MCMXCIV'
    i = 0
    result = 0
    skip = False
    for char in s:
        if skip:
            skip = False
            continue
        else:
            i += 1
            if i < len(s):
                if char == 'I' and s[i] == 'V':
                    result += 4
                    i += 1
                    skip = True
                    continue
                if char == 'I' and s[i] == 'X':
                    result += 9
                    i += 1
                    skip = True
                    continue
                if char == 'X' and s[i] == 'L':
                    result += 40
                    i += 1
                    skip = True
                    continue
                if char == 'X' and s[i] == 'C':
                    result += 90
                    i += 1
                    skip = True
                    continue
                if char == 'C' and s[i] == 'D':
                    result += 400
                    i += 1
                    skip = True
                    continue
                if char == 'C' and s[i] == 'M':
                    result += 900
                    i += 1
                    skip = True
                    continue
            if char == 'I':
                result += 1
                continue
            if char == 'V':
                result += 5
                continue
            if char == 'X':
                result += 10
                continue
            if char == 'L':
                result += 50
                continue
            if char == 'C':
                result += 100
                continue
            if char == 'D':
                result += 500
                continue
            if char == 'M':
                result += 1000
                continue
    print(result)
