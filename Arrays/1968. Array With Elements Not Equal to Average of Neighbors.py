class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums1 = nums[:len(nums)//2]
        nums2 = nums[len(nums)//2:]
        j , k = 0 , 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = nums2[j]
                j+=1
            else:
                nums[i] = nums1[k]
                k+=1
        return nums

        # for i in range(1,len(nums),2):


        # for i in range(1,len(nums)-1):
        #     if abs(nums[i]-nums[i-1]) == abs(nums[i]-nums[i+1]):
        #         temp = nums[i-1]
        #         nums[i-1] = nums[i]
        #         nums[i] = temp
        # return nums