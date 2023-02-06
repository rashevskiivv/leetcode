def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    prefix = ""
    for i, el in enumerate(strs):
        if i == 0:
            prefix = el
        else:
            long = max(len(prefix), len(el))
            if long == len(prefix):
                long_obj = prefix
                short_obj = el
            else:
                long_obj = el
                short_obj = prefix
            for j in range(long):
                cond = short_obj.find(long_obj)
                if cond == 0:
                    prefix = long_obj
                    break
                else:
                    prefix = ""
                    long_obj = long_obj[:len(long_obj) - 1]
    return prefix


if __name__ == '__main__':
    print(longestCommonPrefix(["aca", "cba"]))
    print(longestCommonPrefix(["flower", "flow", "flight"]))
    print(longestCommonPrefix(["dog", "racecar", "car"]))
