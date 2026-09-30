class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # temp and index
        res = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                lastItem = stack.pop()
                res[lastItem[1]] = i - lastItem[1]
            stack.append((t, i))
        return res
            

            
                

                




