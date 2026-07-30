class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        l=0
        r=0
        mx=0
        while r<len(s):
            if s[r] in d and d[s[r]]>=l:
                l=d[s[r]]+1
            d[s[r]]=r
            mx=max(mx,(r-l)+1)
            r+=1
        return mx