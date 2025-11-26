class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        add=0
        i=0
        l=len(s)-1
        while i<=l:
            if s[i]=='I' and i!=l and s[i+1]=='V':
                add+=4
                i+=2
            elif s[i]=='I' and i!=l and s[i+1]=='X':
                add+=9
                i+=2
            elif s[i]=='X' and i!=l and  s[i+1]=='L':
                add+=40
                i+=2
            elif s[i]=='X' and i!=l and  s[i+1]=='C':
                add+=90
                i+=2
            elif s[i]=='C' and i!=l and s[i+1]=='D':
                add+=400
                i+=2
            elif s[i]=='C' and i!=l and s[i+1]=='M':
                add+=900
                i+=2
            else:
                add+=d[s[i]]
                i+=1
        return add