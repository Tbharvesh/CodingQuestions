import math
from typing import List
# As the deno. is getting inc --> ans is dec 

class Solution:
    def divide(self,nums,mid):
        tot = 0
        for i in nums:
            tot += math.ceil(i/mid)
        return tot
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l , h = 1, max(nums)
        # Here we are not working exactly on the arr ,but applying Binary serach on a range which lies between 1 and max elem
        while(l <= h):
            m = (l + h)//2
            tempAns =self.divide(nums,m) #If tempAns > threshold , we need to inc the denominator so that ans will dec
            if tempAns > threshold :
                l = m + 1
            else:
                h = m - 1
        return l


        