class Solution:
    count = 0
    def climbStairs(self, n: int) -> int:
    
        memo = {}

        #defs
        def dfs(curr):
            if curr == n:
                return 1
            if curr > n:
                return 0
            
            if curr in memo:
                return memo[curr]
    
            memo[curr] = dfs(curr + 1) + dfs(curr + 2)
            return memo[curr]

        return dfs(0)
            




        