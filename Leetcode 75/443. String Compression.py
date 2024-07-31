from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        ind , i = 0 , 0
        # ind : index of the updated chars 
        # i : index of current chars 
        while i < len(chars):
            letter = chars[i]
            cnt = 0
            while i < len(chars) and chars[i] == letter:
                cnt += 1
                i += 1
            chars[ind] = letter
            ind += 1
            if cnt > 1 :
                for char in str(cnt):
                    chars[ind] = char
                    ind += 1
        return ind


        
        
      