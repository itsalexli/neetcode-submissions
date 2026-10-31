class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        min_diff = float("inf")
        for r in range(k - 1, len(nums)):
            min_diff = min(nums[r] - nums[l], min_diff) 
            if min_diff == 0:
                return 0
            l += 1
            
        return min_diff


        