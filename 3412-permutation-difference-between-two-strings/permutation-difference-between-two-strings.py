class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        l,r,add={},{},0
        for i in range(len(s)):
            l[s[i]]=i
            r[t[i]]=i
        for i in l.keys():
            add+=abs(l[i]-r[i])
        return add