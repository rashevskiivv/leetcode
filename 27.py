def removeElement(nums: [int], val: int):
    count = nums.count(val)
    for i in range(count):
        nums.remove(val)
    return len(nums), nums


if __name__ == '__main__':
    print(removeElement([3, 2, 2, 3], 3))
    print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
