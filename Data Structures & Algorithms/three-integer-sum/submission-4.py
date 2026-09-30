class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numMap = {}
        allTrip = []
        
        for num in nums:
            numMap[num] = numMap.get(num, 0) + 1
            
        for i in range(len(nums)):
            target = 0 - nums[i]
            numMap[nums[i]] -= 1 
            
            for j in range(i + 1, len(nums)):  
                numMap[nums[j]] -= 1  
            
                third = target - nums[j]
                if third in numMap and numMap[third] > 0:
                    currTrip = [nums[i], nums[j], third]
                    currTrip.sort()
                    if currTrip not in allTrip:
                        allTrip.append(currTrip)
                
                numMap[nums[j]] += 1  # Restore second element
            
            numMap[nums[i]] += 1  # Restore first element
            
        return allTrip