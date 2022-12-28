import math

# Dummy solution:
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles_num = len(piles)
        for i in range(k):
            piles = sorted(piles)
            piles[-1] = math.ceil(piles[-1] / 2)
        return sum(piles)

# Python heap solution:
import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-num for num in piles]
        heapq.heapify(heap)
        
        for _ in range(k):
            curr = -heapq.heappop(heap)
            remove = curr // 2
            heapq.heappush(heap, -(curr - remove))
        
        return -sum(heap)
