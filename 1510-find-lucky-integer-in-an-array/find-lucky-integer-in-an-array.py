from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        x=Counter(arr)
        res=[]
        for i,j in x.items():
            if i==j:
                res.append(i)
        if res:
            return max(res)
        return -1