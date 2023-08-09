class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
        #NOT DONE YET
        if len(nums) == 0:
            return 0
        res = 1
        val = min(nums)
        for i in range(len(nums)):
            if val + 1 in nums:
                val += 1
                res += 1
            else:
                return res
        return res


if __name__ == '__main__':
    print(Solution.longestConsecutive(Solution(), [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]) == 7)
    print(Solution.longestConsecutive(Solution(), []) == 0)
    print(Solution.longestConsecutive(Solution(), [100, 4, 200, 1, 3, 2]) == 4)
    print(Solution.longestConsecutive(Solution(), [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9)
