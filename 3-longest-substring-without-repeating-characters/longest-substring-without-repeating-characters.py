class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        l=0
        r=0
        mx=0
        while r<len(s):
            while d and  s[r] in d:
                del d[s[l]]
                l+=1
            d[s[r]]=d.get(s[r],0)+1
            mx=max(mx,len(d.keys()))
            r+=1
        return mx