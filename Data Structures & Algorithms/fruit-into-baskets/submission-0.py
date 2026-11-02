from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        fruit_types = defaultdict(int)
        max_fruits =  0
        for r in range(len(fruits)):
            fruit_types[fruits[r]] += 1
            last = fruits[l]
            while len(fruit_types) > 2:
                fruit_types[fruits[l]] -= 1
                if fruit_types[fruits[l]] == 0:
                    deleted = fruit_types.pop(fruits[l])
                l += 1
            max_fruits = max(max_fruits, r - l + 1)
        
        return max_fruits


       



        