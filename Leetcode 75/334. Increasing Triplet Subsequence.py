class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3 :
            return False
        f , s = float('inf') , float('inf')
        for i in range(len(nums)):
            if nums[i] <= f :
                f = nums[i]
            elif nums[i] <= s and nums[i] >f  :
                s = nums[i]
            else :
                return True
        return False
            