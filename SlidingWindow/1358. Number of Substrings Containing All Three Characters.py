class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hp = { 'a' : 0, 'b' : 0 ,'c' : 0}
        cnt = 0
        l , r = 0 , 0
        n = len(s)
        for r in range(n):
            hp[s[r]] += 1
            while all(hp[char] > 0 for char in 'abc') :
                cnt += n - r 
                hp[s[l]] -= 1
                l += 1
        
        return cnt
# class Solution:
#     def numberOfSubstrings(self, s: str) -> int:
#         # hp = { 'a' : 0, 'b' : 0 ,'c' : 0}
#         s1 = ''
#         cnt = 0
#         l , r = 0 , 0
#         n = len(s)
#         for r in range(n):
#             s1 += s[r]
#             while all(char in s1 for char in 'abc') :
#                 cnt += n - r
#                 s1= s1.replace(s1[l],'x')
#                 l += 1
#         return cnt

