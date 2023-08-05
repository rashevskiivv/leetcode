class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        result = []
        count = {}
        for i in range(len(nums)):
            if nums[i] not in count.keys():
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        ascending = sorted(count.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            result.append(ascending[i][0])
        return result


if __name__ == '__main__':
    print(Solution.topKFrequent(Solution(), [3, 1, 1, 1, 2, 2], 2))
    print(Solution.topKFrequent(Solution(), [1], 1))
