class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        countList = {}
        for num in nums:
            countList[num] = countList.get(num,0) + 1
        longestSeq = 0
        for num in nums:
            currSeq = 1
            while (num-1) in countList:
                currSeq += 1
                num -= 1
            longestSeq = max(longestSeq, currSeq)
        return longestSeq

        