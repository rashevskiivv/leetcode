def removeDuplicates(nums: [int]):
    # last = 0
    # i = 0
    # while True:
    #     if i >= len(nums):
    #         return len(nums), nums
    #     if i == 0:
    #         last = nums[i]
    #         i += 1
    #         continue
    #     if nums[i] == last:
    #         nums.remove(last)
    #     else:
    #         last = nums[i]
    #         i += 1
    insertIndex = 1
    for i in range(1, len(nums)):
        # Found unique element
        if nums[i - 1] != nums[i]:
            # Updating insertIndex in our main array
            nums[insertIndex] = nums[i]
            # Incrementing insertIndex count by 1
            insertIndex = insertIndex + 1
    return insertIndex


if __name__ == '__main__':
    print(removeDuplicates([1, 1, 2]))
    print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
