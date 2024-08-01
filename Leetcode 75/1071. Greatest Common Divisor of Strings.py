class Solution:
    def gcd(self,n1,n2):
        f1 = []
        f2 = []
        for i in range(1,n1+1):
            if n1 % i == 0:
                f1.append(i)
        for i in range(1,n2+1):
            if n2 % i == 0  and i in f1:
                f2.append(i)
        return max(f2)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1 :
            return ''
        maxLen = self.gcd(len(str1),len(str2))
        return str1[:maxLen]