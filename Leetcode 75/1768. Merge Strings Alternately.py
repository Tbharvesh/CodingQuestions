class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        st =''
        if len(word1)<len(word2):
            for i in range(len(word1)):
                st += word1[i]
                st += word2[i]
            st += word2[i+1 : ]
        else:
            for i in range(len(word2)):
                st += word1[i]
                st += word2[i]
            st += word1[i+1 : ]

        return st
        
        