class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d=set()
        l=0
        r=0
        mx=0
        while r<len(s):
            while d and  s[r] in d:
                d.remove(s[l])
                l+=1
            d.add(s[r])
            mx=max(mx,len(d))
            r+=1
        return mx