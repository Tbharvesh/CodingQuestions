from collections import defaultdict
import heapq
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hp = defaultdict(int)
        for i in range(len(nums)):
            hp[nums[i]] += 1
        
        pq = []
        for key,val in hp.items():
            heapq.heappush(pq, (-val , key)) #Priority , task in PQ
        
        ans = -1
        li = []
        for i in range(k):
            freq , ans = heapq.heappop(pq)
            li.append(ans)
        return li