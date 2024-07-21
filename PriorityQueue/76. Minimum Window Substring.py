from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        map = defaultdict(int)
        count = len(t)
        start = 0
        min_len = float('inf')
        min_start = 0
        
        for c in t:
            map[c] += 1
        
        for end in range(len(s)):
            if map[s[end]] > 0:
                count -= 1
            map[s[end]] -= 1
            
            while count == 0:
                if end - start + 1 < min_len:
                    min_start = start
                    min_len = end - start + 1
                
                map[s[start]] += 1
                if map[s[start]] > 0:
                    count += 1
                start += 1
        
        return "" if min_len == float('inf') else s[min_start:min_start + min_len]

        