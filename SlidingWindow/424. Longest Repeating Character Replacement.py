from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = defaultdict(int)
        maxLength = 0
        for r in range(len(s)):
            count[s[r]] += 1
            if (r - l + 1) <= (max(count.values()) + k):
                maxLength = r - l + 1
            else:
                count[s[l]] -= 1
                l += 1

        return maxLength
