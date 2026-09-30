class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit = 0

        currBuyIndex = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[currBuyIndex]:
                profit = prices[i] - prices[currBuyIndex]
                totalProfit += profit
                currBuyIndex = i
            else:
                currBuyIndex = i

        return totalProfit
