from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxLen = 0
        l , r = 0 , 0

        hp = dict()
        while(r < len(fruits)):
            if fruits[r] in hp :
                hp[fruits[r]] += 1
            else:
                hp[fruits[r]] = 1
            if len(hp) > 2:
                while(len(hp) > 2):
                    hp[fruits[l]] -= 1 
                    if hp[fruits[l]] == 0:
                        del hp[fruits[l]]
                    l += 1
            else:
                maxLen = max(maxLen , r-l+1)
            r += 1
        return maxLen