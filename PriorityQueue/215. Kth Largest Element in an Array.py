import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for i in range(len(nums)):
            heapq.heappush(pq , -nums[i])
        for i in range(k):
            ans = heapq.heappop(pq)
        return -ans # type: ignore
        
