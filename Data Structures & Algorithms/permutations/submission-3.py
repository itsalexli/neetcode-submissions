class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        #set up

        res = []
        combo = []
        used = [False] * len(nums)

        def dfs():

            #base case

            if len(combo) >= len(nums):
                res.append(combo.copy())

            #loop through
            for i in range(len(nums)):
                if used[i] == True: #if used, skip
                    continue
                
                combo.append(nums[i])
                used[i] = True

                dfs()

                combo.pop()
                used[i] = False
        dfs()
        return res
            

        