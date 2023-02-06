import sys


def mySqrt(x: int) -> int:
    if x == 0:
        return 0
    left, right = 1, sys.maxsize
    while True:
        mid = left + (right - left) / 2
        if mid > x / mid:
            right = mid - 1
        else:
            if mid + 1 > x / (mid + 1):
                return int(mid)
            left = mid + 1


if __name__ == '__main__':
    print(mySqrt(4))
    print(mySqrt(8))
