from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        arr = [bool]*len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= m:
                arr[i] = True # type: ignore
            else:
                arr[i] = False # type: ignore
        return arr

