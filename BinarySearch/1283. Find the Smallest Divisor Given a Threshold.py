import math
from typing import List
class Solution:
    def divide(self,nums,mid):
        tot = 0
        for i in nums:
            tot += math.ceil(i/mid)
        return tot
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l , h = 1, max(nums)
       
        while(l <= h):
            m = (l + h)//2
            tempAns =self.divide(nums,m)
            if tempAns > threshold :
                l = m + 1
            else:
                h = m - 1
        return l


        