from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum , rsum = 0 , 0
        msum = 0
        for i in range(k):
            lsum += cardPoints[i]
        msum = lsum
        r = len(cardPoints) - 1
        for i in range(k-1,-1,-1):
            lsum = lsum - cardPoints[i]
            rsum = rsum + cardPoints[r]
            r -= 1
            msum = max(msum,lsum+rsum)
        return msum