class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        min_time = 0
        survivor = neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                min_time += min(survivor, neededTime[i])
                survivor = max(survivor, neededTime[i])
            else:
                survivor = neededTime[i]
        return min_time