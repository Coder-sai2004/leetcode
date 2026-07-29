class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        d={}
        mx=0
        vowels={'a','e','i','o','u'}
        for i in range(k):
            if s[i] in vowels:
                d[s[i]]=d.get(s[i],0)+1
        mx=max(mx,sum(d.values()))
        
        for i in range(k,len(s)):
            if s[i] in vowels:
                d[s[i]]=d.get(s[i],0)+1

            if s[i-k] in vowels:
                if d[s[i-k]]==1:
                    del d[s[i-k]]
                else:
                    d[s[i-k]]-=1

            val=sum(d.values())

            mx=max(mx,val)

        return mx