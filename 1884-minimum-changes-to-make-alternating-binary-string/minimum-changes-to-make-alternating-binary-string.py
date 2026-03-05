class Solution:
    def minOperations(self, s: str) -> int:
        c1=0
        c2=0
        for i in range(len(s)):
            if i%2==0 and s[i]=='1':
                c1+=1
            if i%2!=0 and s[i]=='0':
                c1+=1
        for j in range(len(s)):
            if j%2==0 and s[j]=='0':
                c2+=1
            if j%2!=0 and s[j]=='1':
                c2+=1
        return min(c1,c2)