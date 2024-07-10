class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        m = 0
        j = 0
        for i in range(len(arr)-1):
            if arr[i] % 2 != 0 and arr[i+1] % 2 != 0:
                cnt += 1
                j = i + 1
                m = max(cnt, m)
            else:
                cnt = 0
        
        if j == len(arr) - 2 and arr[j+1] % 2 != 0:
            m += 1
        
        return m >= 2
            