class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        countList = {}
        for num in nums:
            countList[num] = countList.get(num, 0) + 1
        
        newArr = []
        for item in countList:
            if countList[item] > (len(nums)/3):
                newArr.append(item)
        return newArr