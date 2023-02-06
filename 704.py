class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            if nums[m] > target:
                r = m - 1
        return -1


if __name__ == '__main__':
    print(Solution().search([2, 5], 5))  # 1
    print(Solution().search([5], -5))  # -1
    print(Solution().search([5], 5))  # 0
    print(Solution().search([-1, 0, 3, 5, 9, 12], 9))  # 4
    print(Solution().search([-1, 0, 3, 5, 9, 12], 2))  # -1
