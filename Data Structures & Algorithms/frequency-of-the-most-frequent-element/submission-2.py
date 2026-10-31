class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True) 
        l = 0
        max_count = 0
        window_sum = 0
        for r in range(len(nums)):
            window_sum += nums[r]
            while nums[l] * (r - l + 1) - window_sum > k:
                window_sum -= nums[l]
                l += 1
            
            max_count = max(max_count, r - l + 1)
        
        return max_count
            



            


        
            
            



        
        