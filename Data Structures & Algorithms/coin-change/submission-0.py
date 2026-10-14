class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        
        def dfs(rem):
            if rem in memo:
                return memo[rem]

            if rem == 0:
                return 0
            
            if rem < 0:
                return float("inf")
        
            best = float("inf")
            for coin in coins:
                num_coins = 1 + dfs(rem - coin)
                best = min(best, num_coins)
            
            memo[rem] = best
            return best
        
        ans = dfs(amount)
        return ans if ans != float("inf") else -1

            
                    



