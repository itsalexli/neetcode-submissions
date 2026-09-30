
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heapified_stones = []
        for stone in stones:
            heapified_stones.append(stone * -1)
        
        heapq.heapify(heapified_stones)

        while len(heapified_stones) > 1:
            largest = heapq.heappop(heapified_stones)
            second = heapq.heappop(heapified_stones)
            if largest == second:
                continue
            else:
                heapq.heappush(heapified_stones, largest-second)
        
        if heapified_stones:
            return (heapified_stones[0] * -1)
        else:
            return 0


        



        