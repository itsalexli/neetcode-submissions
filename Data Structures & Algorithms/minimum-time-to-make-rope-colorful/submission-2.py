class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        min_time = 0
        curr = 0
        n = len(colors)
        while curr < n:
            group_count = 0
            group_max = neededTime[curr]
            next_col = curr + 1
            
            while (next_col) < n and colors[next_col] == colors[curr]:
                group_count += min(group_max, neededTime[next_col])
                group_max = max(group_max, neededTime[next_col])
                next_col += 1

            min_time += group_count
            curr = next_col
        
        return min_time
            






        
