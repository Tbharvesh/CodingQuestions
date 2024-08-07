from typing import List


class Solution:
    def search(self, arr: List[int], target: int) -> int:
        rotated_ind = -1
       
        for i in range(len(arr)-1):
            if arr[i] > arr[i + 1]:
                rotated_ind = i
        if rotated_ind == -1:
            return arr.index(target) if target in arr else -1

        arr1 = arr[:rotated_ind+1]
        arr2 = arr[rotated_ind+1:]
        print(arr1,arr2)
        l , h = 0 , len(arr1) -1
        while(l <= h):
            m = l + (h-l)//2
            if arr1[m] == target:
                return m
            elif arr1[m] < target :
                l = m + 1
            else:
                h = m - 1
        l , h = 0, len(arr2) -1
        # print(arr2[l:h])
        while(l <= h):
            m = l + (h-l)//2
            if arr2[m] == target:
                # print('l')
                return m + rotated_ind + 1
            elif arr2[m] < target :
                l = m + 1
            else:
                h = m - 1
        return -1
        











        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1