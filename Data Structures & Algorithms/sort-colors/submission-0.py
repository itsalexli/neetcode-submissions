class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0] * 3
        for num in nums:
            freq[num] += 1
        
        # Replace entire contents using slice assignment
        nums[:] = [0] * freq[0] + [1] * freq[1] + [2] * freq[2]


            



        