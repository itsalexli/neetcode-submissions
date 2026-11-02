class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def find_k_subarrays(k):

            l = 0
            odd_count = 0
            res = 0  
            for r in range(len(nums)):
                if nums[r] % 2 != 0:
                    odd_count += 1
                while odd_count > k:
                    if nums[l] % 2 != 0:
                        odd_count -= 1
                    l += 1
                res += r - l + 1
            return res
        
        return find_k_subarrays(k) - find_k_subarrays(k - 1)
        

