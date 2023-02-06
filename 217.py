class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # time - O(n) - loop
        # space - O(n) - set
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

        # time - O(nlogn) - O(nlogn) sort + O(n) loop
        # space - O(1)
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i-1] == nums[i]:
        #         return True
        # return False

        # time - O(n^2) - O(n) loop * O(n) access in d
        # space - O(1)
        # d = {}
        # for i in range(len(nums)):
        #     if nums[i] in d:
        #         return True
        #     d[nums[i]] = i
        # return False


if __name__ == '__main__':
    print(Solution().containsDuplicate([1, 2, 3, 1]))  # True
    print(Solution().containsDuplicate([1, 2, 3, 4]))  # False
    print(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
