from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st=[]
        res = [-1] * len(nums)
        for i in range(len(nums)*2 -1, -1, -1):
            while(len(st)>0 and nums[st[-1]]<= nums[i%len(nums)]):
                st.pop()
            if len(st)>0 :

                res[i % len(nums)] = nums[st[-1]]
            else:
                res[i % len(nums)] = -1
            st.append(i%len(nums))
        return res