def searchInsert(nums: [int], target: int) -> int:
    # minimum, positions, flag = 9999, [], False
    # if target in nums:
    #     return nums.index(target)
    # for i in range(len(nums)):
    #     a = max(target - nums[i], nums[i] - target)
    #     if a < minimum:
    #         minimum = a
    #         flag = target >= nums[i]
    #         positions.clear()
    #         positions.append(i)
    #     elif a == minimum:
    #         positions.append(i)
    # if flag:
    #     return positions[0] + 1
    # else:
    #     return positions[0]

    # Binary search
    low, high, mid = 0, len(nums) - 1, False
    while low <= high:  # include '=' to solve error when len(nums) = 1
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if nums[mid] > target:
        return mid
    else:
        return mid + 1


if __name__ == '__main__':
    print(searchInsert([1, 3, 5, 6], 5))
    print(searchInsert([1, 3, 5, 6], 2))
    print(searchInsert([1, 3, 5, 6], 7))
    print(searchInsert([1, 3, 5, 6], 0))
    print(searchInsert([3, 6, 7, 8, 10], 5))
