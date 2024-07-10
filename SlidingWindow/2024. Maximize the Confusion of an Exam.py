class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l , r = 0 , 0
        maxC = 0
        hp ={'T':0,'F':0}
        
        while( r < len(answerKey)):
            hp[answerKey[r]] += 1
            
            # Chcek if tot len - maxFereq >= k or not?
            if (r - l + 1) - max(hp.values()) > k:
                hp[answerKey[l]] -= 1
                l += 1
            else:
                maxC = max(maxC , r-l+1)


            r += 1
        return maxC
