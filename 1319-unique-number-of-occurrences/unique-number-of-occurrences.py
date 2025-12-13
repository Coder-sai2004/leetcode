from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        x=Counter(arr)
        r=[]
        for i in x.values():
            r.append(i)
        s=set(r)
        if len(s)==len(r):
            return True
        return False