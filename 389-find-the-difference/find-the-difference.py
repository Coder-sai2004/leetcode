from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x=Counter(s)
        y=Counter(t)
        for i in t:
            if y[i]-x[i]==1:
                return i