def plusOne(digits: [int]) -> [int]:
    s = ""
    for i in range(len(digits)):
        s += str(digits[i])
    val = int(s) + 1
    result = []
    for i in range(len(str(val))):
        result.append(int(str(val)[i]))
    return result


if __name__ == '__main__':
    print(plusOne([1,2,3]))
    print(plusOne([4,3,2,1]))
    print(plusOne([9]))
    print(plusOne([9, 9]))