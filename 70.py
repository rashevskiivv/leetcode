def climbStairs(n: int) -> int:
    # https://www.youtube.com/watch?v=Y0lT9Fck7qI&t=2s
    # DFS
    # DP
    one, two = 1, 1
    for i in range(n - 1):
        temp = one
        one += two
        two = temp
    return one
    # Fibonacci
    # return int(round(1 / 5 ** 0.5 * (((1 + 5 ** 0.5) / 2.0) ** (n + 1) - ((1 - 5 ** 0.5) / 2.0) ** (n + 1))))


if __name__ == '__main__':
    print(climbStairs(2))  # 11, 2
    print(climbStairs(3))  # 111, 21, 12
    print(climbStairs(4))  # 1111, 211, 121, 112, 22
    print(climbStairs(5))  # 11111, 2111, 1211, 1121, 1112, 221, 212, 122
