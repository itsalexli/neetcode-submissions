class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        target = len(nums) - 1
        def dfs(curr):
            if curr > target:
                return 0
            
            if curr == target:
                return nums[target]
            
            if curr in memo:
                return memo[curr]
            
            memo[curr] = nums[curr] + max(dfs(curr + 2), dfs(curr + 3))
            return memo[curr]
        
        return max(dfs(0), dfs(1))


            