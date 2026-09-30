class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0
        for i in range(len(prices)):
            if prices[i] <= prices[l]:
                l = i
            else:
                profit = prices[i] - prices[l]
                maxProfit = max(maxProfit, profit)
            
        return maxProfit

        