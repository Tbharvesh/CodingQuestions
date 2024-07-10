from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l , r = 0 , 0
        msum = 0
        zeros = 0
        # maxi = 0
        while( r<len(nums)):
            if nums[r] == 0:
                zeros +=1
                
            while(zeros > k):
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            if zeros <= k:
                msum = max(msum,r-l+1)
            r+=1

        return msum
            

        # for i in range(len(nums)):
        #     zeros = 0 
        #     for j in range(i,len(nums)):
        #         if nums[j] == 0 :
        #             zeros +=1
        #         if  zeros <=k :
        #             maxi = max(maxi , j-i+1)
        #         else:
        #             break
        # return maxi