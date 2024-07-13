from typing import List


class Solution:
    def buyChoco(self, nums: List[int], money: int) -> int:
        nums.sort()
        cnt= 0
        m=money
        for i in range(len(nums)):
            if money-nums[i]>=0  and cnt<2:
                cnt+=1
                money=money-nums[i]
        if cnt<2:
            return m
        else:
            return money