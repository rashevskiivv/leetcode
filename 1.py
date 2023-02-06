class Solution(object):
    def twoSum(self, nums, target):
        # time - O(n)
        # space - O(n)
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - value
            if remaining in seen:
                return [seen[remaining], i]
            seen[value] = i


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))  # 0,1
    print(Solution().twoSum([3, 2, 4], 6))  # 1,2
    print(Solution().twoSum([3, 3], 6))  # 0,1
