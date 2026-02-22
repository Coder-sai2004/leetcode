class Solution:
    def binaryGap(self, n: int) -> int:
        s=bin(n)[2:]
        c=0
        i=0
        j=1
        while j<len(s):
            if s[i]==s[j]:
                c=max(c,j-i)
                i=j
            j+=1
        return c