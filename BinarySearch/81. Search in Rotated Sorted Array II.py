from typing import List


class Solution:
    def search(self, arr: List[int], target: int) -> bool:

        rotated_ind = -1
       
        for i in range(len(arr)-1):
            if arr[i] > arr[i + 1]:
                rotated_ind = i
                break
        
        arr1 = arr[:rotated_ind+1]
        arr2 = arr[rotated_ind+1:]
        l , h = 0 , len(arr1)-1
        while(l<=h):
            m = l + (h-l)//2
            if arr1[m] == target:
                return True
            elif arr1[m] < target :
                l = m + 1
            else:
                h = m - 1
        l , h = 0 , len(arr2)-1
        while(l<=h):
            m = l + (h-l)//2
            if arr2[m] == target:
                return True
            elif arr2[m] < target :
                l = m + 1
            else:
                h = m - 1
        return False
        

        