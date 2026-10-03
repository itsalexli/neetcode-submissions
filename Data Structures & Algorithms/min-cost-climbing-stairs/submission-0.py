class Solution:
    min_cost = float("inf")
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        end = len(cost)

        def dfs(curr):

            if curr >= end:
                return 0
            
            if curr in memo:
                return memo[curr]
            
            memo[curr] = cost[curr] + min(dfs(curr + 1), dfs(curr + 2))
            return memo[curr]
        
        return min(dfs(0), dfs(1))
            


        
            

        