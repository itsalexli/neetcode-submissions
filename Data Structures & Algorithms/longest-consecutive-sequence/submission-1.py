class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        largestSeq = 1
        for num in nums:
            seq = 1
            s = num-1
            while s in count:
                seq += 1
                s-=1
            largestSeq = max(largestSeq, seq)
        return largestSeq
            

                
                
            



        
            

            

        