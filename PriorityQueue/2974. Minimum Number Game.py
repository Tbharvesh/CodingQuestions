import heapq
from typing import List
# Both methods have O(nlogn) but list is more preferred here bec of priority q overheads
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        st = []
        nums.sort()
        for i in range(0,len(nums),2):
            temp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = temp
        return nums

        # Using priorityQ
        pq = []
        arr = []
        for i in range(len(nums)):
            heapq.heappush(pq , nums[i])
        while pq:
            first = heapq.heappop(pq)
            sec =  heapq.heappop(pq)
            arr.append(sec)
            arr.append(first)
        return arr



