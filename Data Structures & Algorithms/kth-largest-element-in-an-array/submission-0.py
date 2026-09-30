
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pop = len(nums) - k
        heapq.heapify(nums)
        for i in range(pop):
            heapq.heappop(nums)
        
        return nums[0]
            
            


        