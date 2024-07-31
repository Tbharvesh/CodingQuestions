class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            
            return 0
        
        l, r = 0, 0
        max_length = 0
        char_set = set()
  
        while r < n:
            if s[r] not in char_set:
                char_set.add(s[r])
                r += 1
                max_length = max(max_length, r - l)
            else:
                
                char_set.remove(s[l])
                l += 1

        return max_length
