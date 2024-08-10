from typing import List


class Solution:
    def possible(self,nums,days,m,k):
        cnt = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i]<=days:
                cnt += 1

            else:
                ans += cnt//k
                cnt  = 0 
        ans += cnt//k
        if ans>=m:
            return True
        else:
            return False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)< m*k :
            return -1
        mini , maxi = min(bloomDay) , max(bloomDay)

        while(mini <= maxi):
            mid = (mini + maxi)//2
            # print(self.possible(bloomDay,mid,m,k),mid)
            if self.possible(bloomDay,mid,m,k) ==False:
                mini = mid + 1
            else:
            
                maxi = mid - 1
        return mini
        
        
        
        