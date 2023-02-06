class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l = 0
        result = 0
        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                if profit > result:
                    result = profit
            else:
                l = r
        return result


if __name__ == '__main__':
    print(Solution().maxProfit([1, 2, 1, 2, 1, 3, 5, 1]))  # 4
    print(Solution().maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]))  # 9
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 5
    print(Solution().maxProfit([7, 6, 4, 3, 1]))  # 0
