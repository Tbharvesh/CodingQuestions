# Linear search approach
# class Solution:
#     def findKthPositive(self, arr: List[int], k: int) -> int:

#         for i in range(1,k+len(arr)+1):
#             if i not in arr and k!=0:
#                 k -= 1
#             if k == 0:
#                 return i
  
# Binary serach approach : elem in list of 1...len(arr)+k+1 must be on index arr[i-1] 
# i.e 7 is on index 6 , since list starts from 1 
# so difference between the expected index of 7 and org index is the no. of missing elems
class Solution:
    def findKthPositive(self, arr, k):
        beg, end = 0, len(arr)
        while beg < end:
            mid = (beg + end) // 2
            if arr[mid] - mid - 1 < k:   #cnt of missing no.s upto mid index
                beg = mid + 1
            else:
                end = mid
        return end + k  #end:ind , k: added to end to find actual missing no.