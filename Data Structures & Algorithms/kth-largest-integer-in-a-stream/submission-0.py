import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.stream = nums
        heapq.heapify(self.stream)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)
        pops = len(self.stream) - self.k

        removed = []
        for _ in range(pops):
            removed.append(heapq.heappop(self.stream))

        kth = heapq.heappop(self.stream)

        # restore everything (including kth)
        heapq.heappush(self.stream, kth)
        for x in removed:
            heapq.heappush(self.stream, x)

        return kth
