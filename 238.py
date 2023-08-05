class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        result = []
        prefix = 1
        for i in range(len(nums)):
            result.append(prefix)
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result


if __name__ == '__main__':
    print(Solution.productExceptSelf(Solution(), [1, 2, 3, 4]))
    print(Solution.productExceptSelf(Solution(), [-1, 1, 0, -3, 3]))
