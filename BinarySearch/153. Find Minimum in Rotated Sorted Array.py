from typing import List


class Solution:
    def findMin(self, arr: List[int]) -> int:
        rotated_ind = -1
       
        for i in range(len(arr)-1):
            if arr[i] > arr[i + 1]:
                rotated_ind = i
        if rotated_ind == len(arr)-1:
            return arr[0]
        else:
            return arr[rotated_ind + 1]